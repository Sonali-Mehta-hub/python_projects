from datetime import datetime

# File where we will store habit data
HABIT_FILE = "habits.txt"

# Load existing habits from the file
def load_habits():
    habits = {}
    try:
        with open(HABIT_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(';')
                # Ensure that all fields are correctly handled
                if len(parts) == 5:
                    name, created, category, periodicity, progress = parts
                    progress_list = progress.split(',') if progress else []
                    habits[name] = {"created": created, "category": category, "periodicity": periodicity, "progress": progress_list}
    except FileNotFoundError:
        pass
    return habits

# Save habits to the file
def save_habits(habits):
    with open(HABIT_FILE, 'w') as file:
        for habit, details in habits.items():
            progress_str = ','.join(details['progress'])
            file.write(f"{habit};{details['created']};{details['category']};{details['periodicity']};{progress_str}\n")

# Add a new habit
def add_habit(habits):
    habit_name = input("Enter the name of the new habit: ")
    if habit_name in habits:
        print(f"The habit '{habit_name}' already exists!")
    else:
        today = str(datetime.now().date())
        category = input("Enter the category of the habit (e.g., Health, Study, Work): ")
        periodicity = input("Enter the periodicity of the habit (e.g., Daily, Weekly, Monthly): ")
        habits[habit_name] = {"created": today, "category": category, "periodicity": periodicity, "progress": []}
        print(f"Habit '{habit_name}' added.")

# Mark a habit as done for today
def mark_done(habits):
    habit_name = input("Enter the habit to mark as done: ")
    if habit_name not in habits:
        print(f"The habit '{habit_name}' does not exist!")
    else:
        today = str(datetime.now().date())
        if today in habits[habit_name]['progress']:
            print(f"You have already marked '{habit_name}' as done for today.")
        else:
            habits[habit_name]['progress'].append(today)
            print(f"Habit '{habit_name}' marked as done for today.")

# View all habits and progress
def view_habits(habits):
    if not habits:
        print("No habits tracked yet.")
    else:
        for habit, details in habits.items():
            print(f"\nHabit: {habit}")
            print(f"  Created: {details['created']}")
            print(f"  Category: {details['category']}")
            print(f"  Periodicity: {details['periodicity']}")
            print(f"  Progress: {len(details['progress'])} days")
            if details['progress']:
                print(f"  Done on: {', '.join(details['progress'])}")
            else:
                print(f"  Not completed on any day yet.")

# Main menu
def main():
    habits = load_habits()
    while True:
        print("\n--- Habit Tracker ---")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_habit(habits)
            save_habits(habits)
        elif choice == '2':
            mark_done(habits)
            save_habits(habits)
        elif choice == '3':
            view_habits(habits)
        elif choice == '4':
            save_habits(habits)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
