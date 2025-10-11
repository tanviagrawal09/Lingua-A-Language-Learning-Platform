'''import json
import os

DATA_FILE = "notes_data.json"

# Load data from file
def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save data to file
def save_notes(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add a note
def add_note(username, note):
    data = load_notes()
    if username not in data:
        data[username] = []
    data[username].append(note)
    save_notes(data)
    print("Note added successfully!")

# View all notes
def view_notes(username):
    data = load_notes()
    notes = data.get(username, [])
    if not notes:
        print("No notes found.")
    else:
        print("Your Notes:")
        for i, n in enumerate(notes, start=1):
            print(f"{i}. {n}")

# Delete a note
def delete_note(username, index):
    data = load_notes()
    if username in data and 0 <= index < len(data[username]):
        deleted = data[username].pop(index)
        save_notes(data)
        print(f"Deleted note: {deleted}")
    else:
        print("Invalid index or user.")

# Example test (remove or comment later)
if __name__ == "__main__":
    add_note("tanvi", "Complete AI project report")
    add_note("tanvi", "Revise Python basics")
    view_notes("tanvi")
    delete_note("tanvi", 0)
    view_notes("tanvi")'''






'''import json
import os

NOTES_FILE = "notes.json"
DICTIONARY_FILE = "dictionary.json"

# ---------------- Helper Functions ----------------

def load_data(filename):
    """Load data from JSON file."""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def save_data(filename, data):
    """Save data to JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ---------------- Notes Section ----------------

def add_note():
    notes = load_data(NOTES_FILE)
    title = input("\nEnter note title: ")
    content = input("Write your note:\n")
    notes[title] = content
    save_data(NOTES_FILE, notes)
    print("Note saved successfully!")

def view_notes():
    notes = load_data(NOTES_FILE)
    if not notes:
        print("\nNo notes found yet.")
    else:
        print("\nYour Notes:")
        for title, content in notes.items():
            print("\n" + title + "\n" + content)

def delete_note():
    notes = load_data(NOTES_FILE)
    title = input("Enter the title of the note to delete: ")
    if title in notes:
        del notes[title]
        save_data(NOTES_FILE, notes)
        print("Note deleted successfully!")
    else:
        print("Note not found.")'''

from database import load_data, save_data

def add_note(username, word, note_text):
    data = load_data()
    data.setdefault("notes", {})
    data["notes"].setdefault(username, [])
    for n in data["notes"][username]:
        if n["word"].lower() == word.lower():
            return False, "Note for this word already exists!"
    data["notes"][username].append({"word": word, "note": note_text})
    save_data(data)
    return True, "Note added successfully!"

def get_notes(username):
    data = load_data()
    return data.get("notes", {}).get(username, [])

def delete_note(username, word):
    data = load_data()
    notes = data.get("notes", {}).get(username, [])
    new = [n for n in notes if n["word"].lower() != word.lower()]
    if len(new) == len(notes):
        return False, "Note not found!"
    data["notes"][username] = new
    save_data(data)
    return True, "Note deleted!"
