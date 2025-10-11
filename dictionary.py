'''def add_note():
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
            print("\n " + title + "\n" + content)


def delete_note():
    notes = load_data(NOTES_FILE)
    title = input("Enter the title of the note to delete: ")
    if title in notes:
        del notes[title]
        save_data(NOTES_FILE, notes)
        print("Note deleted successfully!")
    else:
        print("Note not found.")'''


'''import json
import os

DICT_FILE = "dictionary_data.json"

# Load dictionary data
def load_dictionary():
    if os.path.exists(DICT_FILE):
        with open(DICT_FILE, "r") as f:
            return json.load(f)
    return {}

# Save dictionary data
def save_dictionary(data):
    with open(DICT_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add a word and its meaning
def add_word(username, word, meaning):
    data = load_dictionary()
    if username not in data:
        data[username] = {}
    data[username][word.lower()] = meaning
    save_dictionary(data)
    print("✅ Word added successfully!")

# View all words
def view_words(username):
    data = load_dictionary()
    if username in data and data[username]:
        print("Your Personal Dictionary:")
        for w, m in data[username].items():
            print(f"{w} → {m}")
    else:
        print("No words found.")

# Search for a specific word
def search_word(username, word):
    data = load_dictionary()
    word = word.lower()
    if username in data and word in data[username]:
        print(f"{word} → {data[username][word]}")
    else:
        print("❌ Word not found!")

# Delete a word
def delete_word(username, word):
    data = load_dictionary()
    word = word.lower()
    if username in data and word in data[username]:
        del data[username][word]
        save_dictionary(data)
        print(f"🗑️ Word '{word}' deleted successfully!")
    else:
        print("❌ Word not found!")

# Example test (remove or comment later)
if __name__ == "__main__":
    add_word("tanvi", "serene", "calm and peaceful")
    add_word("tanvi", "vivid", "producing clear and strong images in the mind")
    view_words("tanvi")
    search_word("tanvi", "vivid")
    delete_word("tanvi", "serene")
    view_words("tanvi")'''






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

def add_word():
    dictionary = load_data(DICTIONARY_FILE)
    word = input("\nEnter new word: ").lower()
    meaning = input("Enter meaning: ")
    example = input("Enter example sentence: ")
    dictionary[word] = {"meaning": meaning, "example": example}
    save_data(DICTIONARY_FILE, dictionary)
    print("Word added to dictionary!")

def search_word():
    dictionary = load_data(DICTIONARY_FILE)
    word = input("\nEnter word to search: ").lower()
    if word in dictionary:
        print("\n" + word.upper())
        print("Meaning: " + dictionary[word]["meaning"])
        print("Example: " + dictionary[word]["example"])
    else:
        print("Word not found in dictionary.")

def view_dictionary():
    dictionary = load_data(DICTIONARY_FILE)
    if not dictionary:
        print("\nDictionary is empty.")
    else:
        print("\nYour Dictionary Words:")
        for word, info in dictionary.items():
            print("\n" + word.capitalize())
            print("Meaning: " + info["meaning"])
            print("Example: " + info["example"])'''




from database import load_data

def search_word(word):
    data = load_data()
    for w in data["vocabulary"]:
        if w["word"].lower() == word.lower():
            return True, w["meaning"]
    return False, "Word not found!"
