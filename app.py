# app.py
import streamlit as st
from datetime import date
from habit import Habit
from utils import save_habits, load_habits

st.set_page_config(page_title="Smart Habit Tracker", page_icon="✅")

st.title("📊 Smart Habit Tracker")
st.markdown("Track your daily habits and become a better version of yourself 🚀")

habits = load_habits()

# --- Add New Habit ---
with st.form("add_habit"):
    new_habit = st.text_input("Enter a new habit:")
    submitted = st.form_submit_button("Add Habit")
    if submitted and new_habit:
        habits.append(Habit(new_habit))
        save_habits(habits)
        st.success(f"Habit '{new_habit}' added!")

# --- Daily Tracking ---
st.subheader("✅ Today's Habits")
today = str(date.today())

for habit in habits:
    status = st.checkbox(habit.name, value=habit.records.get(today, False))
    if status:
        habit.mark_complete(today)
    else:
        habit.mark_incomplete(today)

save_habits(habits)

# --- Completion Report ---
st.subheader("📈 Progress Report")
for habit in habits:
    st.write(f"**{habit.name}** – {habit.get_completion_rate()}% complete")
    st.progress(habit.get_completion_rate())
