from datetime import date
from recurrence import Recurrence


class HabitCompletionHistoryPoint:
    def __init__(self, date: date, completion: bool):
        self.date = date
        self.completion = completion

class Habit:
    def __init__(self, name: str, description: str, first_deadline: date, recurrence: Recurrence, completion_history: [HabitCompletionHistoryPoint] = []):
        self.name = name
        self.description = description
        self.recurrence = recurrence
        self.completion_history: [HabitCompletionHistoryPoint] = completion_history
        self.last_deadline: date = first_deadline

    def complete(self, date: date):
        # find the next deadline
        # TODO: potentionally can be optimized
        current_deadline = self.last_deadline
        while True:
            next_deadline = self.recurrence.next_occurrence(current_deadline)
            if current_deadline >= date:
                self.last_deadline = next_deadline
                self.completion_history.append(HabitCompletionHistoryPoint(current_deadline, True))
                break
            else:
                current_deadline = next_deadline
                self.completion_history.append(HabitCompletionHistoryPoint(current_deadline, False))

    def get_longest_streak(self, sort_history_points_by_date: bool = True):
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