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
        self.date = date
        self.completion = completion

    def __str__(self) -> str:
        """
        Returns a string representation of the HabitCompletionHistoryPoint.

        Returns:
            str: String representation of the completion point.
        """
        status = "Completed" if self.completion else "Not Completed"
        return f"<HabitCompletionHistoryPoint | {status} | {self.date.strftime('%Y-%m-%d')}>"


# Class for representing habits
class Habit:
    def __init__(self, name: str, description: str, first_deadline: date, recurrence: Recurrence,
                 completion_history: [HabitCompletionHistoryPoint] = [], creation_date: date = datetime.date.today()):
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
        self.name = name
        self.description = description
        self.recurrence = recurrence
        self.completion_history: [HabitCompletionHistoryPoint] = completion_history
        self.last_deadline: date = first_deadline
        self.is_broken: Optional[bool] = None
        self.creation_date: date = creation_date

    def complete(self, date: date):
        """
        Marks a habit as completed on a given date period and if user missed period or periods before than marks that
        as not completed. All dates is saved to completion_history

        Args:
            date (date): The date on which the habit is completed.
        """
        current_deadline = self.last_deadline
        is_habit_broken = False
        while True:
            next_deadline = self.recurrence.next_occurrence(current_deadline)
            if current_deadline >= date:
                self.last_deadline = next_deadline
                self.completion_history.append(HabitCompletionHistoryPoint(current_deadline, True))

                if not self.is_broken:
                    self.is_broken = is_habit_broken

                break
            else:
                current_deadline = next_deadline
                self.completion_history.append(HabitCompletionHistoryPoint(current_deadline, False))
                is_habit_broken = True


    def get_longest_streak(self, sort_history_points_by_date: bool = True) -> int:
        """
        Calculates the longest streak of completed habits.

        Args:
            sort_history_points_by_date (bool): Whether to sort completion history by date.

        Returns:
            int: The longest streak of completed habits.
        """
        if not self.completion_history:
            return 0

        # by default should be defined rite way but to make 100% sure sorting can be done
        if sort_history_points_by_date:
            date_history_points = sorted(self.completion_history, key=lambda history_point: history_point.date)
        else:
            date_history_points = self.completion_history

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
        status = "Is Broken" if self.is_broken else "Is Not Broken"
        recurrence_info = str(self.recurrence) if self.recurrence else "No Recurrence"
        history_str = "[" + ", ".join([str(point) for point in self.completion_history]) + "]"
        return f"<Habit {self.name}({self.description}) | {status} | {recurrence_info} | {history_str}>"