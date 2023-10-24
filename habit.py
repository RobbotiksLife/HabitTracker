from datetime import date
from typing import Optional

from recurrence import Recurrence


class HabitCompletionHistoryPoint:
    def __init__(self, date: date, completion: bool):
        self.date = date
        self.completion = completion

    def __str__(self) -> str:
        status = "Completed" if self.completion else "Not Completed"
        return f"<HabitCompletionHistoryPoint | {status} | {self.date.strftime('%Y-%m-%d')}>"

class Habit:
    def __init__(self, name: str, description: str, first_deadline: date, recurrence: Recurrence, completion_history: [HabitCompletionHistoryPoint] = []):
        self.name = name
        self.description = description
        self.recurrence = recurrence
        self.completion_history: [HabitCompletionHistoryPoint] = completion_history
        self.last_deadline: date = first_deadline
        self.is_broken: Optional[bool] = None

    def complete(self, date: date):
        # TODO: can be optimized better
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
            if completion_history_point.complition:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 0

        return max(longest_streak, current_streak)


    def __str__(self) -> str:
        status = "Is Broken" if self.is_broken else "Is Not Broken"
        recurrence_info = str(self.recurrence) if self.recurrence else "No Recurrence"
        history_str = "[" + ", ".join([str(point) for point in self.completion_history]) + "]"
        return f"<Habit {self.name}({self.description}) | {status} | {recurrence_info} | {history_str}>"