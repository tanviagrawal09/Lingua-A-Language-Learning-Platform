'''import json
import os

VOCAB_FILE = "vocabulary.json"


# Load vocabulary (Improved with error handling)

def load_vocabulary():
    """Load vocabulary list from file, handling JSON errors."""
    if not os.path.exists(VOCAB_FILE):
        return []
    try:
        with open(VOCAB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle the error if the file is empty or corrupted
        print(f"Warning: Could not decode JSON from {VOCAB_FILE}. Returning empty list.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading vocabulary: {e}")
        return []


# Save vocabulary

def save_vocabulary(vocab_list):
    """Save the updated vocabulary list back to file."""
    # Ensure all data is saved as a list of dictionaries
    with open(VOCAB_FILE, "w") as f:
        json.dump(vocab_list, f, indent=4)


# Add new vocabulary word
 
def add_word():
    """Prompts user for word details and adds it to the vocabulary list."""
    vocab = load_vocabulary()
    word = input("Enter word: ").strip()
    meaning = input("Enter meaning: ").strip()
    level = input("Enter level (Easy/Medium/Hard): ").strip()
    
    # Optional: Prevent duplicate entries (a good check to add)
    if any(v['word'].lower() == word.lower() for v in vocab):
        print(f"Word '{word}' already exists in the list.")
        return
        
    vocab.append({
        "word": word, 
        "meaning": meaning, 
        "level": level
    })
    save_vocabulary(vocab)
    print(f"Word '{word}' added successfully!")


# View vocabulary by level
 
def view_by_level():
    """Displays vocabulary words filtered by a user-specified level."""
    vocab = load_vocabulary()
    if not vocab:
        print("Vocabulary list is empty. Add some words first!\n")
        return

    level_input = input("Enter level to view (Easy/Medium/Hard): ").strip().lower()
    
    # Use list comprehension for efficient filtering
    filtered_words = [v for v in vocab if v["level"].lower() == level_input]

    if not filtered_words:
        print(f"No words found in the '{level_input}' level.")
        return

    print(f"\n Words in {level_input.capitalize()} level:")
    for v in filtered_words:
        # Using f-strings for clear output
        print(f"- {v['word']}: {v['meaning']}")
    print("\n")



# Run directly

if __name__ == "__main__":
    print("\n--- Vocabulary Management Module Test ---")
    print("1. Add Word\n2. View by Level")
    choice = input("Enter choice (1/2): ")
    if choice == "1":
        add_word()
    elif choice == "2":
        view_by_level()
    else:
        print("Invalid choice.")'''






'''import json
import os

VOCAB_FILE = "vocabulary.json"

# Load vocabulary
def load_vocabulary():
    if not os.path.exists(VOCAB_FILE):
        return []
    try:
        with open(VOCAB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: Could not decode JSON from {VOCAB_FILE}. Returning empty list.")
        return []   
    except Exception as e:
        print(f"An unexpected error occurred while loading vocabulary: {e}")
        return []
# Save vocabulary
def save_vocabulary(vocab_list):
    with open(VOCAB_FILE, "w") as f:
        json.dump(vocab_list, f, indent=4)
# Add new vocabulary word
def add_word():
    vocab = load_vocabulary()
    word = input("Enter word: ")
    meaning = input("Enter meaning: ")
    level = input("Enter level (Easy/Medium/Hard): ")
    if any(v['word'].lower() == word.lower() for v in vocab):
        print(f" Word '{word}' already exists in the list.")
        return
    vocab.append({"word": word, "meaning": meaning, "level": level})
    save_vocabulary(vocab)
    print(" Word added successfully!")
# View vocabulary by level
def view_by_level():
    vocab = load_vocabulary()
    if not vocab:
        print("vocabulary list is empty. Add some words first!\n")
        return
    level = input("Enter level (Easy/Medium/Hard): ").strip().lower()
    filtered_words=[v for v in vocab if v["level"].lower()==level.input]
    if not filtered_words:
        print(f"No words found in the '{level}' level.")
        return
    print(f"\n Words in {level} level:")
    for v in filtered_words:
        print(f"- {v['word']}: {v['meaning']}")
    print("\n")'''

from database import load_data, save_data

def add_word(word, meaning, level="Easy"):
    data = load_data()
    for w in data["vocabulary"]:
        if w["word"].lower() == word.lower():
            return False, "Word already exists!"
    data["vocabulary"].append({"word": word, "meaning": meaning, "level": level})
    save_data(data)
    return True, "Word added successfully!"

def get_words(level=None):
    data = load_data()
    if level:
        return [w for w in data["vocabulary"] if w["level"].lower() == level.lower()]
    return data["vocabulary"]

def delete_word(word):
    data = load_data()
    words = data["vocabulary"]
    new_words = [w for w in words if w["word"].lower() != word.lower()]
    if len(new_words) == len(words):
        return False, "Word not found!"
    data["vocabulary"] = new_words
    save_data(data)
    return True, "Word deleted!"
