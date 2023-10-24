from datetime import date
from typing import Optional, List

from recurrence import Recurrence, RecurrenceType
from habit import Habit
from habitTracker import HabitTracker


class HabitTrackerApp(HabitTracker):
    def __init__(self, habits: Optional[List[Habit]] = None):
        super().__init__(habits=habits)
        menu_choices = {
            "1": ("List Habits", self.print_habits),
            "2": ("Create Habit", self.define_habit),
            "3": ("List Habits by Recurrence", self.define_list_habits_by_recurrence),
            "4": ("List Longest Streak for All Habits", self.define_longest_streak_all_habits),
            "5": ("List Longest Streak for a Habit", self.define_longest_streak_for_habit),
            "6": ("Load Habits from File", self.action_load_habits_from_file),
            "7": ("Save Habits to File", self.action_save_habits_to_file),
            "8": ("Delete Habit", self.delete_habit),
            "9": ("Exit", None)
        }

        # Main program loop
        while True:
            print("-"*50, "\nHabit Tracker Menu:")
            for key, value in menu_choices.items():
                print(f"{key}. {value[0]}")

            choice = input("\nEnter your choice: ")
            print()

            if choice in menu_choices:
                function = menu_choices[choice][1]
                if function is None:
                    break
                function()
            else:
                print("Invalid choice. Please select a valid option (1-8).")

            print()

    def define_habit(self):
        name = input("Habit name: ")
        description = input("Habit description: ")
        first_deadline = date.fromisoformat(input("Habit first_deadline (YYYY-MM-DD): "))
        recurrence_type = self.input_not_none_recurrence_type()
        recurrence_interval = int(input("Recurrence interval (default is 1): "))

        new_habit = Habit(
            name,
            description,
            first_deadline,
            Recurrence(recurrence_type=recurrence_type, interval=recurrence_interval)
        )

        self.habits.append(new_habit)
        print("Habit created successfully!")

    def print_habits(self, habits: Optional[List[Habit]] = None):
        if not habits:
            habits = self.habits
        for i, habit in enumerate(habits):
            print(f"{i + 1}. {habit}")

    def choose_habit(self) -> Optional[Habit]:
        self.print_habits()
        habit_index = int(input("Enter habit number: ")) - 1

        if 0 <= habit_index < self.get_number_of_habits():
            return self.habits[habit_index]
        else:
            return None

    def delete_habit(self):
        habit: Optional[Habit] = self.choose_habit()

        if habit:
            self.habits.remove(habit)
        else:
            print(f"Couldn't removing habit")

    def input_recurrence_type(self) -> Optional[RecurrenceType]:
        print("Define recurrence type:")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")
        print("4. Yearly")
        print("5. None")
        recurrence_mapping_choice = input("Enter the number for recurrence type: ")
        recurrence_mapping = {
            "1": RecurrenceType.DAILY,
            "2": RecurrenceType.WEEKLY,
            "3": RecurrenceType.MONTHLY,
            "4": RecurrenceType.YEARLY,
            "5": None,
        }
        # Get the recurrence_type based on the user's input or default to 'None'
        recurrence_type = recurrence_mapping.get(recurrence_mapping_choice, None)
        if recurrence_mapping_choice != "5" and recurrence_type is None:
            print("Invalid choice for recurrence type. Defaulting to 'None'.")
        return recurrence_type

    def input_not_none_recurrence_type(self) -> RecurrenceType:
        recurrence_type = self.input_recurrence_type()
        while recurrence_type is None:
            print("Recurrence is None. Choose a non-None Recurrence.")
            recurrence_type = self.input_recurrence_type()
        return recurrence_type

    def define_list_habits_by_recurrence(self):
        recurrence_type = self.input_recurrence_type()
        habits = self.list_habits_by_recurrence(recurrence_type)
        self.print_habits(habits)

    def define_longest_streak_all_habits(self):
        longest_streak = self.get_longest_streak_all_habits()
        print(f"The longest streak for all habits is {longest_streak}.")

    def define_longest_streak_for_habit(self):
        habit_longest_streak = self.get_longest_streak_for_habit()
        print(f"Habit longest streak is: {habit_longest_streak}")

    def action_load_habits_from_file(self):
        file_path = self.defineFilePath()
        self.load_habits_from_file(file_path)

    def action_save_habits_to_file(self):
        file_path = self.defineFilePath()
        self.save_habits_to_file(file_path)

