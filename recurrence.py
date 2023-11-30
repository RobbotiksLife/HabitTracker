from enum import Enum
from datetime import date, timedelta
from typing import Optional


# Enum defining the recurrence types
class RecurrenceType(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'


# Class for handling recurrences
class Recurrence:
    _DEFAULT_INTERVAL = 1  # Default interval for recurrences

    def __init__(self, recurrence_type: RecurrenceType, interval: int = _DEFAULT_INTERVAL):
        """
        Initializes a Recurrence object.

        Args:
            recurrence_type (RecurrenceType): The type of recurrence (e.g., daily, weekly).
            interval (int): The interval between recurrences (default is 1).
        """
        if not isinstance(recurrence_type, RecurrenceType):
            raise ValueError("recurrence_type must be a valid RecurrenceType")
        self._recurrence_type = recurrence_type
        self._interval = interval  # Number of units for the recurrence (default is 1)

    @property
    def recurrence_type(self) -> RecurrenceType:
        """Getter for recurrence_type property."""
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, value: RecurrenceType) -> None:
        """
        Setter for recurrence_type property.

        Args:
            value (RecurrenceType): The new recurrence type to set.
        """
        if not isinstance(value, RecurrenceType):
            raise ValueError("recurrence_type must be a valid RecurrenceType")
        self._recurrence_type = value

    @property
    def interval(self) -> int:
        """Getter for interval property."""
        return self._interval

    @interval.setter
    def interval(self, value: int) -> None:
        """
        Setter for interval property.

        Args:
            value (int): The new interval to set.
        """
        if not isinstance(value, int):
            raise ValueError("interval must be an integer")
        self._interval = value

    def __str__(self):
        """
        Returns a string representation of the Recurrence object.

        Returns:
            str: String representation of the recurrence.
        """
        if self._interval == 1:
            return f"Recurrence: {self._recurrence_type.value}"
        else:
            return f"Recurrence: {self._interval} {self._recurrence_type.value}(s)"

    def next_occurrence(self, last_occurrence: date) -> Optional[date]:
        """
        Calculates the next occurrence date based on the last occurrence date.

        Args:
            last_occurrence (date): The last occurrence date.

        Returns:
            Optional[date]: The next occurrence date, or None if the recurrence type is not recognized.
        """
        if self._recurrence_type == RecurrenceType.DAILY:
            new_date = last_occurrence + timedelta(days=self._interval)
        elif self._recurrence_type == RecurrenceType.WEEKLY:
            new_date = last_occurrence + timedelta(weeks=self._interval)
        elif self._recurrence_type == RecurrenceType.MONTHLY:
            new_date = self.add_months(last_occurrence, self._interval)
        elif self._recurrence_type == RecurrenceType.YEARLY:
            new_date = last_occurrence.replace(year=last_occurrence.year + self._interval)
        else:
            return None

        return new_date

    @staticmethod
    def add_months(source_date, months):
        # Helper function to add months to a date
        month = source_date.month - 1 + months
        year = source_date.year + month // 12
        month = month % 12 + 1
        day = min(source_date.day, [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month])
        return source_date.replace(year=year, month=month, day=day)