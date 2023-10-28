from datetime import date

from recurrence import Recurrence, RecurrenceType
from habit import Habit, HabitCompletionHistoryPoint
from habitTrackerApp import HabitTrackerApp


if __name__ == "__main__":
    # Initializes a HabitTrackerApp with predefined habits
    tracker_app = HabitTrackerApp(
        habits=[
            Habit(
                "Daily Exercise",
                "30 minutes of exercise daily",
                date(2024, 7, 5),
                Recurrence(RecurrenceType.DAILY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 4), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 3), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 2), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 1), True
                    )
                ]
            ),
            Habit(
                "Weekly Reading",
                "Read a book for 1 hour every Week",
                date(2024, 7, 6),
                Recurrence(RecurrenceType.WEEKLY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 29), True
                    )
                ]
            ),
            Habit(
                "Meditation",
                "Practice meditation for 15 minutes daily",
                date(2024, 7, 10),
                Recurrence(RecurrenceType.DAILY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 9), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 8), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 7), True
                    )
                ]
            ),
            Habit(
                "Healthy Eating",
                "Consume a balanced meal with fruits and vegetables daily",
                date(2024, 7, 12),
                Recurrence(RecurrenceType.DAILY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 11), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 10), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 9), True
                    )
                ]
            ),
            Habit(
                "Language Learning",
                "Practice a new language for 30 minutes every day",
                date(2024, 7, 14),
                Recurrence(RecurrenceType.WEEKLY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 13), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 6), True
                    )
                ]
            )
        ]
    )

