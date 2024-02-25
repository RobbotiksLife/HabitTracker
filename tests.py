import unittest
from datetime import date
from unittest import mock

from habitTrackerApp import HabitTrackerApp
from recurrence import Recurrence, RecurrenceType
from habit import Habit, HabitCompletionHistoryPoint
from habitTracker import HabitTracker
import os

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.habit_tracker = HabitTracker(habits=[
        Habit(
            "Daily Exercise",
            "30 minutes of exercise daily",
            date(2024, 7, 5),
            Recurrence(RecurrenceType.DAILY),
            creation_date=date(2024, 6, 16),
            is_broken=False,
            completion_history=[
                HabitCompletionHistoryPoint(
                    date(2024, 6, 17), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 18), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 19), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 20), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 21), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 22), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 23), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 24), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 25), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 26), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 27), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 28), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 29), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 30), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 1), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 2), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 3), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 4), True
                )
            ]
        ),
        Habit(
            "Weekly Reading",
            "Read a book for 1 hour every Week",
            date(2024, 7, 6),
            Recurrence(RecurrenceType.WEEKLY),
            creation_date=date(2024, 4, 27),
            is_broken=False,
            completion_history=[
                HabitCompletionHistoryPoint(
                    date(2024, 5, 4), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 5, 11), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 5, 18), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 5, 25), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 1), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 8), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 15), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 22), True
                ),
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
            creation_date=date(2024, 6, 22),
            is_broken=False,
            completion_history=[
                HabitCompletionHistoryPoint(
                    date(2024, 6, 23), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 24), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 25), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 26), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 27), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 28), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 29), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 30), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 1), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 2), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 3), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 4), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 5), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 6), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 7), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 8), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 9), True
                )
            ]
        ),
        Habit(
            "Healthy Eating",
            "Consume a balanced meal with fruits and vegetables daily",
            date(2024, 7, 12),
            Recurrence(RecurrenceType.DAILY),
            creation_date=date(2024, 6, 18),
            is_broken=False,
            completion_history=[
                HabitCompletionHistoryPoint(
                    date(2024, 6, 19), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 20), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 21), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 22), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 23), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 24), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 25), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 26), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 27), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 28), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 29), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 30), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 1), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 2), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 3), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 4), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 5), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 6), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 7), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 8), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 9), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 10), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 11), True
                )
            ]
        ),
        Habit(
            "Language Learning",
            "Practice a new language for 30 minutes every day",
            date(2024, 7, 14),
            Recurrence(RecurrenceType.WEEKLY),
            creation_date=date(2024, 5, 26),
            is_broken=False,
            completion_history=[
                HabitCompletionHistoryPoint(
                    date(2024, 6, 2), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 9), False
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 16), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 23), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 6, 30), True
                ),
                HabitCompletionHistoryPoint(
                    date(2024, 7, 7), True
                )
            ]
        )
    ])

    def test_add_habit(self):
        self.assertEqual(len(self.habit_tracker.habits), 5)
        self.habit_tracker.add_habit(Habit("Exercise", "Daily workout", date(2023, 12, 31), Recurrence(RecurrenceType.DAILY)))
        self.assertEqual(len(self.habit_tracker.habits), 6)

    def test_get_number_of_habits(self):
        self.assertEqual(self.habit_tracker.get_number_of_habits(), len(self.habit_tracker.habits))

    def test_list_habits_by_recurrence(self):
        daily_habits = self.habit_tracker.list_habits_by_recurrence(RecurrenceType.DAILY)
        self.assertEqual(len(daily_habits), 3)

    def test_get_longest_streak_all_habits(self):
        streak = self.habit_tracker.get_longest_streak_all_habits()
        self.assertEqual(streak, 17)

    def test_save_and_load_habits_to_file(self):
        file_path = "test_habits.pickle"
        self.habit_tracker.save_habits_to_file(file_path)
        self.assertTrue(os.path.exists(file_path))

        new_habit_tracker = HabitTracker()
        new_habit_tracker.load_habits_from_file(file_path)
        self.assertEqual(len(new_habit_tracker.habits), len(self.habit_tracker.habits))

        os.remove(file_path)


class TestHabitTrackerApp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        mocked_inputs = iter([
            '10',  # Exit the loop immediately
        ])
        with mock.patch('builtins.input', side_effect=lambda *args: next(mocked_inputs)):
            self.habit_tracker = HabitTrackerApp()

    def test_create_and_add_new_habit(self):
        new_habit = Habit('Exercise', 'Daily workout', date(2023, 12, 31), Recurrence(recurrence_type=RecurrenceType.DAILY, interval=1))
        with mock.patch.object(self.habit_tracker, 'define_habit', return_value=new_habit):
            self.habit_tracker.create_and_add_new_habit()
        self.assertEqual(len(self.habit_tracker.habits), 1)
        self.habit_tracker.habits.remove(new_habit)

    def test_define_habit(self):
        inputs = iter([
            'Test Habit',  # Name
            'Description of Test Habit',  # Description
            '2023-12-25',  # First deadline
            '1',  # Recurrence type (1 for Daily)
            '2',  # Recurrence interval
        ])
        expected_habit = Habit(
            'Test Habit',
            'Description of Test Habit',
            date(2023, 12, 25),
            Recurrence(RecurrenceType.DAILY, interval=2)
        )

        with mock.patch('builtins.input', side_effect=lambda *args: next(inputs)):
            defined_habit = self.habit_tracker.define_habit()

        self.assertEqual(defined_habit.name, expected_habit.name)
        self.assertEqual(defined_habit.description, expected_habit.description)
        self.assertEqual(defined_habit.last_deadline, expected_habit.last_deadline)
        self.assertEqual(defined_habit.recurrence.recurrence_type, expected_habit.recurrence.recurrence_type)
        self.assertEqual(defined_habit.recurrence.interval, expected_habit.recurrence.interval)

    def test_delete_habit(self):
        test_habit = Habit('Exercise', 'Daily workout', date(2023, 12, 31), Recurrence(recurrence_type=RecurrenceType.DAILY, interval=1))
        self.habit_tracker.habits.append(test_habit)
        with mock.patch.object(self.habit_tracker, 'choose_habit', return_value=self.habit_tracker._ChosenHabit(0, test_habit)):
            self.habit_tracker.delete_habit()
        self.assertEqual(len(self.habit_tracker.habits), 0)

class TestHabit(unittest.TestCase):
    def test_habit_completion_first(self):
        self.habit1 = Habit("Exercise", "Daily workout", date(2023, 12, 31), Recurrence(RecurrenceType.DAILY))
        self.habit1.complete(date(2023, 12, 31))
        self.assertEqual(self.habit1.completion_history[0].completion, True)

    def test_habit_completion_first_1(self):
        self.habit1 = Habit("Exercise", "Daily workout", date(2023, 12, 31), Recurrence(RecurrenceType.DAILY))
        self.habit1.complete(date(2023, 12, 31))
        self.assertEqual(self.habit1.is_broken, False)

    def test_habit_longest_streak(self):
        self.habit2 = Habit("Read", "Read a book", date(2023, 12, 25), Recurrence(RecurrenceType.WEEKLY))
        self.habit2.complete(date(2023, 12, 25))
        self.habit2.complete(date(2024, 1, 1))
        self.assertEqual(len(self.habit2.completion_history), 2)

    def test_habit_longest_streak_2(self):
        self.habit2 = Habit("Read", "Read a book", date(2023, 12, 25), Recurrence(RecurrenceType.WEEKLY))
        self.habit2.complete(date(2023, 12, 25))
        self.habit2.complete(date(2024, 1, 1))
        self.assertEqual(self.habit2.get_longest_streak(), 2)


if __name__ == '__main__':
    unittest.main()
