import pickle
from typing import Optional, List

from recurrence import RecurrenceType
from habit import Habit


# Class for managing habits and habit-related actions
class HabitTracker:
    _default_habit_file_path: str = "habits.pickle"

    def __init__(self, habits: Optional[List[Habit]] =None):
        if habits is None:
            habits = []
        self._habits = habits

    @staticmethod
    def default_habit_file_path() -> str:
        """
        Get the default habit file path.

        :return: The default habit file path.
        """
        return HabitTracker._default_habit_file_path

    @property
    def habits(self) -> List[Habit]:
        """
        Get the list of habits.

        :return: A list of habit strings.
        """
        return self._habits

    @habits.setter
    def habits(self, value: List[Habit]):
        """
        Set the list of habits.

        :param value: A list of new habits.
        """
        self._habits = value

    def add_habit(self, habit: Habit):
        """
        Adds a habit to the habit tracker.

        Args:
            habit (Habit): The habit to be added.
        """
        self._habits.append(habit)

    def get_number_of_habits(self) -> int:
        """
        Returns the number of habits in the tracker.

        Returns:
            int: The number of habits.
        """
        return len(self._habits)

    def list_habits_by_recurrence(self, recurrence_type: RecurrenceType):
        """
        Lists habits with a specific recurrence type.

        Args:
            recurrence_type (RecurrenceType): The recurrence type to filter habits.

        Returns:
            list: List of habits with the specified recurrence type.
        """
        return [habit for habit in self._habits if habit.recurrence and habit.recurrence.recurrence_type == recurrence_type]

    def get_longest_streak_all_habits(self):
        """
        Calculates the longest streak across all habits.

        Returns:
            int: The longest streak across all habits.
        """
        if not self._habits:
            return 0

        longest_streak = 0

        for habit in self._habits:
            habit_streak = habit.get_longest_streak()
            longest_streak = max(longest_streak, habit_streak)

        return longest_streak

    def get_longest_streak_for_habit(self, habit_index: int) -> Optional[int]:
        """
        Calculates the longest streak for a specific habit.

        Args:
            habit_index (int): index of habit in the habits array of tracker.

        Returns:
            Optional[int]: The longest streak for the chosen habit, or None if the habit is not found.
        """
        if 0 <= habit_index < len(self._habits):
            habit: Optional[Habit] = self._habits[habit_index]
            if habit:
                habit_longest_streak = habit.get_longest_streak()
                return habit_longest_streak
            else:
                return None
        else:
            return None

    def save_habits_to_file(self, filename: str = default_habit_file_path, habits: Optional[List[Habit]] = None):
        """
        Saves the habits to a file.

        Args:
            filename (str): The name of the file and path to save the habits.
            habits (list of Habit): The list of habits to be saved.
        """
        if not habits:
            habits = self._habits
        try:
            with open(filename, 'wb') as file:
                pickle.dump(habits, file)
            print(f'Habits saved to {filename}')
        except Exception as e:
            print(f'Error saving habits to {filename}: {e}')

    def load_habits_from_file(self, filename: str = default_habit_file_path):
        """
        Loads habits from a file.

        Args:
            filename (str): The name of the file pathto load habits from.
        """
        try:
            with open(filename, 'rb') as file:
                self._habits = pickle.load(file)
            print(f'Habits loaded from {filename}')
        except Exception as e:
            print(f'Error loading habits from {filename}: {e}')
