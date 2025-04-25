# habit.py
from datetime import date

class Habit:
    def __init__(self, name):
        self.name = name
        self.records = {}  # {date: True/False}

    def mark_complete(self, day=None):
        if not day:
            day = str(date.today())
        self.records[day] = True

    def mark_incomplete(self, day=None):
        if not day:
            day = str(date.today())
        self.records[day] = False

    def get_completion_rate(self):
        if not self.records:
            return 0
        completed = sum(1 for val in self.records.values() if val)
        return int((completed / len(self.records)) * 100)
