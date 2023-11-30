from datetime import date
from typing import Optional, List

from recurrence import Recurrence, RecurrenceType
from habit import Habit
from habitTracker import HabitTracker


# Class for the HabitTrackerApp, a user interface for managing habits
class HabitTrackerApp(HabitTracker):
    class _ChosenHabit:
        def __init__(self, habit_index: Optional[int], habit: Optional[Habit]):
            self._habit_index = habit_index
            self._habit = habit

        @property
        def habit_index(self) -> Optional[int]:
            """
            Get the habit_index.

            Returns:
                Optional[int]: The habit_index value.
            """
            return self._habit_index

        @habit_index.setter
        def habit_index(self, habit_index: Optional[int]) -> None:
            """
            Set the habit_index.

            Args:
                habit_index (Optional[int]): The new habit_index value.
            """
            self._habit_index = habit_index

        @property
        def habit(self) -> Optional[Habit]:
            """
            Get the habit.

            Returns:
                Optional[Habit]: The habit object.
            """
            return self._habit

        @habit.setter
        def habit(self, habit: Optional[Habit]) -> None:
            """
            Set the habit.

            Args:
                habit (Optional[Habit]): The new habit object.
            """
            self._habit = habit

    def __init__(self, habits: Optional[List[Habit]] = None):
        super().__init__(habits=habits)
        self.run_main_program_loop()

    def run_main_program_loop(self):
        # Main program loop with menu choices
        menu_choices = {
            1: ("List Habits", self.print_habits),
            2: ("Create Habit", self.define_habit),
            3: ("Complete Habit", self.action_complete_habit),
            4: ("List Habits by Recurrence", self.define_list_habits_by_recurrence),
            5: ("List Longest Streak for All Habits", self.define_longest_streak_all_habits),
            6: ("List Longest Streak for a Habit", self.define_longest_streak_for_habit),
            7: ("Load Habits from File", self.action_load_habits_from_file),
            8: ("Save Habits to File", self.action_save_habits_to_file),
            9: ("Delete Habit", self.delete_habit),
            10: ("Exit", None)
        }

        try:
            while True:
                print("-" * 50, "\nHabit Tracker Menu:")
                for key, value in menu_choices.items():
                    print(f"{key}. {value[0]}")

                choice = int(input("\nEnter your choice: "))
                print()

                if choice in menu_choices:
                    function = menu_choices[choice][1]
                    if function is None:
                        break
                    function()
                else:
                    menu_choices_int = {key: value for key, value in menu_choices.items()}
                    first_key = min(menu_choices_int.keys())
                    last_key = max(menu_choices_int.keys())
                    print(f"Invalid choice. Please select a valid option ({first_key}-{last_key}).")

                print()
        except Exception as e:
            print(f'Error: {e}\n')
            self.run_main_program_loop()

    def create_and_add_new_habit(self):
        """
        Prompts the user to define a new habit and adds it to the habit tracker.
        """
        new_habit = self.define_habit()
        if new_habit is not None:
            self._habits.append(new_habit)
            print("Habit created successfully!")
        else:
            print("Habit was not added!")

    def define_habit(self) -> Optional[Habit]:
        """
        Prompts the user to define a new habit.
        """
        name = input("Habit name: ")
        description = input("Habit description: ")
        first_deadline = self.define_date("Habit first_deadline")
        recurrence_type = self.input_not_none_recurrence_type()
        recurrence_interval = int(input("Recurrence interval (default is 1): "))
        return Habit(
            name,
            description,
            first_deadline,
            Recurrence(recurrence_type=recurrence_type, interval=recurrence_interval)
        )

    def print_habits(self, habits: Optional[List[Habit]] = None):
        """
        Prints a list of habits.

        Args:
            habits (list of Habit): The list of habits to be printed.
        """
        if not habits:
            habits = self._habits
        for i, habit in enumerate(habits):
            print(f"{i + 1}. {habit}")

    def choose_habit(self) -> _ChosenHabit:
        """
        Prompts the user to choose a habit from the list.

        Returns:
            ChosenHabit: An object representing the chosen habit.
        """
        self.print_habits()
        habit_index = int(input("Enter habit number: ")) - 1

        if 0 <= habit_index < self.get_number_of_habits():
            return HabitTrackerApp._ChosenHabit(habit_index=habit_index, habit=self._habits[habit_index])
        else:
            return ChosenHabit(None, None)

    def delete_habit(self):
        """
        Prompts the user to choose a habit to delete and removes it from the habit tracker.
        """
        habit: Habit = self.choose_habit().habit

        if habit:
            self._habits.remove(habit)
        else:
            print(f"Couldn't remove habit")

    def input_not_none_recurrence_type(self) -> RecurrenceType:
        """
        Prompts the user to input a recurrence type, ensuring it is not None.

        Returns:
            RecurrenceType: The selected recurrence type.
        """
        recurrence_type = self.input_recurrence_type()
        while recurrence_type is None:
            print("Recurrence is None. Choose a non-None Recurrence.")
            recurrence_type = self.input_recurrence_type()
        return recurrence_type

    def define_list_habits_by_recurrence(self):
        """
        Prompts the user to choose a recurrence type and lists habits with that recurrence type.
        """
        recurrence_type = self.input_recurrence_type()
        habits = self.list_habits_by_recurrence(recurrence_type)
        self.print_habits(habits)

    def define_longest_streak_all_habits(self):
        """
        Calculates and displays the longest streak across all habits.
        """
        longest_streak = self.get_longest_streak_all_habits()
        print(f"The longest streak for all habits is {longest_streak}.")

    def define_longest_streak_for_habit(self):
        """
        Prompts the user to choose a habit and calculates and displays its longest streak.
        """
        habit_habit_index: Optional[int] = self.choose_habit().habit_index
        if habit_habit_index is not None:
            habit_longest_streak = self.get_longest_streak_for_habit(habit_habit_index)
            print(f"Habit longest streak is: {habit_longest_streak}")

    def action_load_habits_from_file(self):
        """
        Prompts the user for a file path and loads habits from the specified file.
        """
        file_path = self.define_file_path()
        self.load_habits_from_file(file_path)

    def action_save_habits_to_file(self):
        """
        Prompts the user for a file path and saves habits to the specified file.
        """
        file_path = self.define_file_path()
        self.save_habits_to_file(file_path)

    def action_complete_habit(self):
        """
        Prompts the user to choose a habit and marks it as completed for a specific date.
        """
        habit_index: int = self.choose_habit().habit_index
        completion_date: date = self.define_date("Habit completion_date")

        if habit_index:
            self._habits[habit_index].complete(completion_date)
            print(f"Habit completed. Next deadline is set to {self._habits[habit_index].last_deadline}")
        else:
            print(f"Couldn't complete habit")

    def define_file_path(self) -> str:
        """
        Prompts the user to enter a file path and name with the .pickle type.

        Returns:
            str: The user-entered file path and name with the .pickle type or None if the default path
            and name with the .pickle type is used.
        """
        file_path = input("Enter file path and name with the .pickle type(write 'd' if want to use default one): ")
        return self._default_habit_file_path if file_path == "d" else file_path

    @staticmethod
    def input_recurrence_type() -> Optional[RecurrenceType]:
        """
        Prompts the user to choose a recurrence type and returns the selected type.

        Returns:
            Optional[RecurrenceType]: The selected recurrence type or None if it's not recognized.
        """
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

    @staticmethod
    def define_date(info: str) -> date:
        """
        Static method for defining a date based on user input.

        Args:
            info (str): A string describing what the date represents (e.g., "Habit first_deadline").

        Returns:
            date: The date entered by the user in the format YYYY-MM-DD.

        Note:
            This method prompts the user to input a date in the format YYYY-MM-DD and returns it as a 'date' object.
        """
        return date.fromisoformat(input(f"{info} (YYYY-MM-DD): "))
