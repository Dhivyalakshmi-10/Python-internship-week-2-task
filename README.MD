# Festival Reminder Bot

Festival Reminder Bot is a Python CLI app that helps keep track of festivals, lets users add/view/delete festival reminders, and notifies when a festival is today or within the next 7 days.

## Features
- Add new festival names with dates.
- Save and load festival data from a local JSON file.
- View all saved festivals.
- Delete festivals from the list.
- Check for today's and upcoming festivals within 7 days.

## Requirements
- Python 3.x
- No additional libraries required (uses built-in modules: `datetime`, `json`, `os`).

## Usage
1. Run the script:
2. Choose from the menu:
- View All Festivals
- Add Festival
- Delete Festival
- Check Reminders
- Exit

All festival data is stored in a file called `festivals.json` in the same directory. Make sure to input dates in `YYYY-MM-DD` format.


# Nickname Combiner

Nickname Combiner is a Python script that generates creative nickname combinations from two input names using various styles.

## Features
- Multiple combination styles (first/last parts, halves, random characters, reversals).
- Interactive command-line interface.
- Maintains history of generated nicknames.
- Option to retry, and view nickname history before exit.

## Requirements
- Python 3.x
- No external dependencies (uses built-in module: `random`).

## Usage
1. Run the script:
2. Enter two names when prompted.
3. The script will display several nickname combinations.
4. Optionally retry, and on exit, view the full history of generated nicknames.
