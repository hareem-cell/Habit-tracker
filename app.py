# app.py

from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import date, timedelta

app = Flask(__name__)


def load_habits():
    with open("habits.json", "r") as file:
        return json.load(file)


def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)


# current week start (monday)
def get_week_start(offset=0):
    today = date.today()
    start = today - timedelta(days=today.weekday())
    return (start + timedelta(weeks=offset)).isoformat()


@app.route("/")
def home():

    week_offset = request.args.get("week", 0, type=int)

    week_key = get_week_start(week_offset)

    habits = load_habits()

    # create current week automatically if missing
    for habit in habits:

        if week_key not in habit["weeks"]:

            # copy last week's data if exists
            previous_weeks = list(habit["weeks"].keys())

            if previous_weeks:

                last_week = previous_weeks[-1]

                old_name = habit["weeks"][last_week]["name"]

                habit["weeks"][week_key] = {
                    "name": old_name,
                    "days": [0, 0, 0, 0, 0, 0, 0]
                }

            else:

                habit["weeks"][week_key] = {
                    "name": "New Habit",
                    "days": [0, 0, 0, 0, 0, 0, 0]
                }

    save_habits(habits)

    return render_template(
        "index.html",
        habits=habits,
        week_key=week_key,
        week_offset=week_offset
    )


@app.route("/add", methods=["POST"])
def add():

    habit_name = request.form["habit"]

    week_key = get_week_start()

    habits = load_habits()

    habits.append({
        "weeks": {
            week_key: {
                "name": habit_name,
                "days": [0, 0, 0, 0, 0, 0, 0]
            }
        }
    })

    save_habits(habits)

    return redirect(url_for("home"))


@app.route("/update/<int:index>/<week_key>", methods=["POST"])
def update(index, week_key):

    habits = load_habits()

    habits[index]["weeks"][week_key]["name"] = request.form["name"]

    for i in range(7):

        habits[index]["weeks"][week_key]["days"][i] = 1 if request.form.get(f"day{i}") else 0

    save_habits(habits)

    return redirect(url_for("home"))


@app.route("/delete/<int:index>")
def delete(index):

    habits = load_habits()

    habits.pop(index)

    save_habits(habits)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)