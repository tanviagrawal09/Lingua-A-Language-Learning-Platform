import json
import os

DB_FILE = "database.json"

def load_database():
    """Loads data from the JSON file if it exists, otherwise creates a new one."""
    if not os.path.exists(DB_FILE):
        data = {"users": {}, "vocabulary": [], "notes": {}, "progress": {}, "flashcards": []}
        save_database(data)
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_database(data):
    """Saves data to the JSON file."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

