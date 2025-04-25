# utils.py
import json
from habit import Habit

def save_habits(habits, filename='data.json'):
    json_data = {}
    for habit in habits:
        json_data[habit.name] = habit.records
    with open(filename, 'w') as f:
        json.dump(json_data, f)

def load_habits(filename='data.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        habits = []
        for name, records in data.items():
            h = Habit(name)
            h.records = records
            habits.append(h)
        return habits
    except FileNotFoundError:
        return []
