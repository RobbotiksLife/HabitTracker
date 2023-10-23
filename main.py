from datetime import date
from recurrence import Recurrence, RecurrenceType
from habit import Habit, HabitCompletionHistoryPoint


# TODO: create custom file for HabitTracker when all be working
class HabitTracker:
    def __init__(self):
        self.habits: [Habit] = []

    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    def list_habits(self):
        return self.habits

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

    # def load_predefined_habits(self):
    #     daily_habit = Habit("Daily Exercise", "30 minutes of exercise daily", Recurrence(RecurrenceType.DAILY))
    #     weekly_habit = Habit("Weekly Reading", "Read a book for 1 hour every Sunday", Recurrence(RecurrenceType.WEEKLY, 1))
    #
    #     today = date.today()
    #     for _ in range(4):
    #         daily_habit.create_task(today)
    #         weekly_habit.create_task(today + timedelta(days=7))
    #         today += timedelta(days=1)
    #
    #     self.habits.append(daily_habit)
    #     self.habits.append(weekly_habit)

    # Logically not needed but still for now let it be commented
    # def complete_task(self, habit_name: str, task_index: int):
    #     for habit in self.habits:
    #         if habit.name == habit_name:
    #             if 0 <= task_index < len(habit.tasks):
    #                 task = habit.tasks[task_index]
    #                 task.mark_as_completed_or_update_deadline()

if __name__ == "__main__":
    tracker = HabitTracker()
    tracker.habits = [
        Habit(
            "Daily Exercise",
            "30 minutes of exercise daily",
            date(2024, 7, 5),
            Recurrence(RecurrenceType.DAILY)
        ),
        Habit(
            "Weekly Reading",
            "Read a book for 1 hour every Week",
            date(2024, 7, 6),
            Recurrence(RecurrenceType.WEEKLY)
        )
    ]

    # TODO: continue main HabitTracker
    while True:
        print("Habit Tracker Menu:")
        print("1. List Habits")
        print("2. List Habits by Recurrence")
        print("3. List Longest Streak for All Habits")
        print("4. List Longest Streak for a Habit")
        print("5. Load Habits from File")
        print("6. Save Habits to File")
        print("7. Complete Task")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            habits = tracker.list_habits()
            for i, habit in enumerate(habits):
                print(f"{i + 1}. {habit.name}")

        elif choice == "2":
            recurrence_type = input("Enter recurrence type (daily, weekly, monthly, yearly): ")
            habits = tracker.list_habits_by_recurrence(RecurrenceType[recurrence_type.upper()])
            for i, habit in enumerate(habits):
                print(f"{i + 1}. {habit.name}")

        elif choice == "3":
            longest_streak = tracker.get_longest_streak_all_habits()
            print(f"The longest streak for all habits is {longest_streak} days.")

        elif choice == "4":
            habit_name = input("Enter habit name: ")
            longest_streak = tracker.get_longest_streak_for_habit(habit_name)
            print(f"The longest streak for {habit_name} is {longest_streak} days.")

        elif choice == "5":
            file_path = input("Enter file path: ")
            tracker.load_habits_from_file(file_path)

        elif choice == "6":
            file_path = input("Enter file path: ")
            tracker.save_habits_to_file(file_path)

        elif choice == "7":
            habit_name = input("Enter habit name: ")
            task_index = int(input("Enter task index to complete: "))
            tracker.complete_task(habit_name, task_index)

        elif choice == "8":
            break

