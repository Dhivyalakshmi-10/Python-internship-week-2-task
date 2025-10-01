import datetime
import json
import os

FESTIVAL_FILE = "festivals.json"

# Load festivals from file (if exists)
def load_festivals():
    if os.path.exists(FESTIVAL_FILE):
        with open(FESTIVAL_FILE, "r") as f:
            return json.load(f)
    return {}

# Save festivals to file
def save_festivals(festivals):
    with open(FESTIVAL_FILE, "w") as f:
        json.dump(festivals, f, indent=4)

# Add a new festival
def add_festival(festivals):
    name = input("Enter festival name: ")
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        festivals[name] = date_str
        save_festivals(festivals)
        print(f"✅ Festival '{name}' added successfully.")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

# Delete a festival
def delete_festival(festivals):
    name = input("Enter festival name to delete: ")
    if name in festivals:
        del festivals[name]
        save_festivals(festivals)
        print(f"🗑️ Festival '{name}' deleted.")
    else:
        print("❌ Festival not found.")

# View all festivals
def view_festivals(festivals):
    if not festivals:
        print("📭 No festivals saved.")
    else:
        print("\n🎉 Saved Festivals:")
        for name, date in sorted(festivals.items(), key=lambda x: x[1]):
            print(f" - {name}: {date}")

# Check reminders
def check_reminders(festivals):
    today = datetime.date.today()
    upcoming = []

    for name, date_str in festivals.items():
        fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        diff = (fest_date - today).days
        if diff == 0:
            print(f"🎊 TODAY is {name}!")
        elif 0 < diff <= 7:
            upcoming.append((name, diff, date_str))

    if upcoming:
        print("\n📅 Upcoming Festivals within 7 days:")
        for name, diff, date in upcoming:
            print(f" - {name} on {date} (in {diff} days)")
    elif not upcoming:
        print("✅ No festivals in the next 7 days.")

# Main menu
def main():
    festivals = load_festivals()
    
    while True:
        print("\n====== Festival Reminder Bot ======")
        print("1. View All Festivals")
        print("2. Add Festival")
        print("3. Delete Festival")
        print("4. Check Reminders")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_festivals(festivals)
        elif choice == "2":
            add_festival(festivals)
        elif choice == "3":
            delete_festival(festivals)
        elif choice == "4":
            check_reminders(festivals)
        elif choice == "5":
            print("👋 Exiting Festival Reminder Bot...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
