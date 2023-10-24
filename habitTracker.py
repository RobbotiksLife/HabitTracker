import pickle
from typing import Optional, List

from recurrence import RecurrenceType
from habit import Habit
class HabitTracker:
    _default_habit_file_path: str = "tasks.pickle"

    def __init__(self, habits=None):
        if habits is None:
            habits = []
        self.habits = habits

    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    def get_number_of_habits(self) -> int:
        return len(self.habits)

    def list_habits_by_recurrence(self, recurrence_type: RecurrenceType):
        return [habit for habit in self.habits if habit.recurrence and habit.recurrence.recurrence_type == recurrence_type]

    def get_longest_streak_all_habits(self):
        if not self.habits:
            return 0

        longest_streak = 0

        for habit in self.habits:
            habit_streak = habit.get_longest_streak()
            longest_streak = max(longest_streak, habit_streak)

        return longest_streak

    def get_longest_streak_for_habit(self) -> Optional[int]:
        habit: Optional[Habit] = self.choose_habit()

        if habit:
            habit_longest_streak = habit.get_longest_streak()
            return habit_longest_streak
        else:
            return None

    def save_habits_to_file(self, filename: str = _default_habit_file_path, habits: Optional[List[Habit]] = None):
        if not habits:
            habits = self.habits
        try:
            with open(filename, 'wb') as file:
                pickle.dump(habits, file)
            print(f'Habits saved to {filename}')
        except Exception as e:
            print(f'Error saving habits to {filename}: {e}')

    def load_habits_from_file(self, filename: str = _default_habit_file_path):
        try:
            with open(filename, 'rb') as file:
                self.habits = pickle.load(file)
            print(f'Habits loaded from {filename}')
        except Exception as e:
            print(f'Error loading habits from {filename}: {e}')

    def defineFilePath(self) -> str:
        file_path = input("Enter file path(write 'd' if want to use default one): ")
        return None if file_path == "d" else file_path