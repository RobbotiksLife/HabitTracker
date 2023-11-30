import datetime
from datetime import date
from typing import Optional

from recurrence import Recurrence


# Class for representing habit completion history points
class HabitCompletionHistoryPoint:
    def __init__(self, date: date, completion: bool):
        """
        Initializes a HabitCompletionHistoryPoint.

        Args:
            date (date): The date of the completion point.
            completion (bool): True if the habit was completed on the date, False otherwise.
        """
        self._date = date
        self._completion = completion

    @property
    def date(self) -> date:
        """
        Get the date of the completion point.

        Returns:
            date: The date of the completion point.
        """
        return self._date

    @date.setter
    def date(self, new_date: date):
        """
        Set the date of the completion point.

        Args:
            new_date (date): The new date of the completion point.
        """
        self._date = new_date

    @property
    def completion(self) -> bool:
        """
        Get the completion status of the habit on the date.

        Returns:
            bool: True if the habit was completed on the date, False otherwise.
        """
        return self._completion

    @completion.setter
    def completion(self, new_completion: bool):
        """
        Set the completion status of the habit on the date.

        Args:
            new_completion (bool): True if the habit was completed on the date, False otherwise.
        """
        self._completion = new_completion

    def __str__(self) -> str:
        """
        Returns a string representation of the HabitCompletionHistoryPoint.

        Returns:
            str: String representation of the completion point.
        """
        status = "Completed" if self._completion else "Not Completed"
        return f"<HabitCompletionHistoryPoint | {status} | {self._date.strftime('%Y-%m-%d')}>"


# Class for representing habits
class Habit:
    def __init__(self, name: str, description: str, first_deadline: date, recurrence: Recurrence,
                 completion_history=None, creation_date: date = datetime.date.today()):
        """
        Initializes a Habit.

        Args:
            name (str): The name of the habit.
            description (str): A description of the habit.
            first_deadline (date): The first deadline for the habit.
            recurrence (Recurrence): The recurrence pattern for the habit.
            completion_history (list of HabitCompletionHistoryPoint): History of habit completions.
            creation_date (date): The date when the habit was created (default is today).
        """
        if completion_history is None:
            completion_history = []
        self._name = name
        self._description = description
        self._recurrence = recurrence
        self._completion_history: [HabitCompletionHistoryPoint] = completion_history
        self._last_deadline: date = first_deadline
        self._is_broken: Optional[bool] = None
        self._creation_date: date = creation_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def recurrence(self):
        return self._recurrence

    @recurrence.setter
    def recurrence(self, value):
        self._recurrence = value

    @property
    def completion_history(self):
        return self._completion_history

    @property
    def last_deadline(self):
        return self._last_deadline

    @property
    def is_broken(self):
        return self._is_broken

    @property
    def creation_date(self):
        return self._creation_date

    def complete(self, date: date):
        """
        Marks a habit as completed on a given date period and if user missed period or periods before than marks that
        as not completed. All dates are saved to completion_history

        Args:
            date (date): The date on which the habit is completed.
        """
        current_deadline = self._last_deadline
        is_habit_broken = False
        while True:
            next_deadline = self._recurrence.next_occurrence(current_deadline)
            if current_deadline >= date:
                self._last_deadline = next_deadline
                self._completion_history.append(HabitCompletionHistoryPoint(current_deadline, True))

                if not self._is_broken:
                    self._is_broken = is_habit_broken

                break
            else:
                current_deadline = next_deadline
                self._completion_history.append(HabitCompletionHistoryPoint(current_deadline, False))
                is_habit_broken = True

    def get_longest_streak(self, sort_history_points_by_date: bool = True) -> int:
        """
        Calculates the longest streak of completed habits.

        Args:
            sort_history_points_by_date (bool): Whether to sort completion history by date.

        Returns:
            int: The longest streak of completed habits.
        """
        if not self._completion_history:
            return 0

        # by default should be defined rite way but to make 100% sure sorting can be done
        if sort_history_points_by_date:
            date_history_points = sorted(self._completion_history, key=lambda history_point: history_point.date)
        else:
            date_history_points = self._completion_history

        longest_streak = 0
        current_streak = 0

        for completion_history_point in date_history_points:
            if completion_history_point.completion:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 0

        return max(longest_streak, current_streak)

    def __str__(self) -> str:
        """
        Returns a string representation of the Habit.

        Returns:
            str: String representation of the habit.
        """
        status = "Is Broken" if self._is_broken else "Is Not Broken"
        recurrence_info = str(self._recurrence) if self._recurrence else "No Recurrence"
        history_str = "[" + ", ".join([str(point) for point in self._completion_history]) + "]"
        return f"<Habit {self._name}({self._description}) | {status} | {recurrence_info} | {history_str}>"
