from datetime import date

from recurrence import Recurrence, RecurrenceType
from habit import Habit, HabitCompletionHistoryPoint
from habitTrackerApp import HabitTrackerApp


if __name__ == "__main__":
    tracker_app = HabitTrackerApp(
        habits=[
            Habit(
                "Daily Exercise",
                "30 minutes of exercise daily",
                date(2024, 7, 5),
                Recurrence(RecurrenceType.DAILY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 29), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 22), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 15), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 8), True
                    )
                ]
            ),
            Habit(
                "Weekly Reading",
                "Read a book for 1 hour every Week",
                date(2024, 7, 6),
                Recurrence(RecurrenceType.WEEKLY)
            )
        ]
    )

    # while True:
    #     print("Habit Tracker Menu:")
    #     print("1. List Habits")
    #     print("2. List Habits by Recurrence")
    #     print("3. List Longest Streak for All Habits")
    #     print("4. List Longest Streak for a Habit")
    #     print("5. Load Habits from File")
    #     print("6. Save Habits to File")
    #     print("7. Delete Habit")
    #     print("8. Exit")
    #
    #     choice = input("Enter your choice: ")
    #
    #     if choice == "1":
    #         tracker_app.print_habits()
    #
    #     elif choice == "2":
    #         tracker_app.define_list_habits_by_recurrence()
    #
    #     elif choice == "3":
    #         tracker_app.define_longest_streak_all_habits()
    #
    #     elif choice == "4":
    #         tracker_app.define_longest_streak_for_habit()
    #
    #     elif choice == "5":
    #         tracker_app.action_load_habits_from_file()
    #
    #     elif choice == "6":
    #         tracker_app.action_save_habits_to_file()
    #
    #     elif choice == "7":
    #         tracker_app.delete_habit()
    #
    #     elif choice == "8":
    #         break

