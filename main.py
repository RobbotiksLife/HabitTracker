from datetime import date

from recurrence import Recurrence, RecurrenceType
from habit import Habit, HabitCompletionHistoryPoint
from habitTrackerApp import HabitTrackerApp


if __name__ == "__main__":
    # Initializes a HabitTrackerApp with predefined habits
    HabitTrackerApp(
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
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 30), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 29), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 28), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 27), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 26), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 25), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 24), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 23), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 22), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 21), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 20), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 19), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 18), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 17), True
                    )
                ],
                creation_date=date(2024, 6, 16)
            ),
            Habit(
                "Weekly Reading",
                "Read a book for 1 hour every Week",
                date(2024, 7, 6),
                Recurrence(RecurrenceType.WEEKLY),
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
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 1), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 5, 25), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 5, 18), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 5, 11), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 5, 4), True
                    )
                ],
                creation_date=date(2024, 4, 27)
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
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 6), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 5), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 4), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 3), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 2), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 1), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 30), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 29), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 28), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 27), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 26), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 25), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 24), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 23), True
                    ),
                ],
                creation_date=date(2024, 6, 22)
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
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 8), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 7), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 6), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 5), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 4), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 3), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 2), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 1), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 30), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 29), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 28), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 27), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 26), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 25), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 24), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 23), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 22), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 21), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 20), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 19), True
                    ),
                ],
                creation_date=date(2024, 6, 18)
            ),
            Habit(
                "Language Learning",
                "Practice a new language for 30 minutes every day",
                date(2024, 7, 14),
                Recurrence(RecurrenceType.WEEKLY),
                completion_history=[
                    HabitCompletionHistoryPoint(
                        date(2024, 7, 7), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 30), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 23), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 16), True
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 9), False
                    ),
                    HabitCompletionHistoryPoint(
                        date(2024, 6, 2), True
                    )
                ],
                creation_date=date(2024, 5, 26)
            )
        ]
    )
