'''import json
import random
import os

VOCAB_FILE = "vocab.json"
PROGRESS_FILE = "data/user_progress.json"

def load_vocab():
    """Load vocabulary words from file."""
    if not os.path.exists(VOCAB_FILE):
        return {}
    try:
        with open(VOCAB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: Could not decode JSON from {VOCAB_FILE}. Returning empty vocabulary.")
        return {}
    except Exception as e:
        print(f"Error loading vocabulary: {e}")
        return {}

def load_progress():
    """Load saved progress data."""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warning: Could not decode JSON from {PROGRESS_FILE}. Returning empty progress.")
        return {}
    except Exception as e:
        print(f"Error loading progress: {e}")
        return {}

def save_progress(progress):
    """Save user progress back to file."""
    os.makedirs("data", exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=4)

def start_practice():
    """Start a quiz practice session."""
    vocab = load_vocab()
    progress = load_progress()

    if not vocab:
        print("No vocabulary available to practice!\n")
        return

    username = input("Enter your username: ")
    words = list(vocab.items())
    if len(words) < 1:
        print("Not enough words for a quiz session.\n")
        return

    random.shuffle(words)
    print("\n===== PRACTICE QUIZ =====")
    print("You will be asked meanings of up to 5 random words.\n")

    correct = 0
    total = 0
    quiz_words = words[:min(len(words),5)]

    for w, m in quiz_words:  # Ask 5 random words
        print(f"What is the meaning of '{w}'?")
        ans = input("Your answer: ").strip().lower()
        if ans in m.lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Wrong! Correct meaning: {m}\n")
        total += 1

    score = round((correct / total) * 100, 2) if total > 0 else 0
    print(f"Your Score: {score}%\n")

    # Save progress
    progress[username] = progress.get(username, [])
    progress[username].append({"score": score})
    save_progress(progress)
    print("Progress saved successfully!\n")'''





    
'''import json
import random
import os

# --- Constants for File Paths ---
VOCAB_FILE = "vocab.json"
PROGRESS_FILE = "data/user_progress.json"

# --- Data I/O Functions ---

def load_vocab():
    """Load vocabulary words from file."""
    if not os.path.exists(VOCAB_FILE):
        return {}
    try:
        with open(VOCAB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Added robust error handling for corrupted JSON
        print(f"Warning: Could not decode JSON from {VOCAB_FILE}. Returning empty vocabulary.")
        return {}


def load_progress():
    """Load saved progress data."""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Added robust error handling for corrupted JSON
        return {}


def save_progress(progress):
    """Save user progress back to file."""
    # Ensure the 'data' directory exists
    os.makedirs("data", exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=4)

# --- Main Quiz and Progress Function ---

def start_practice():
    """Start a quiz practice session and save progress."""
    vocab = load_vocab()
    progress = load_progress()

    if not vocab:
        print("No vocabulary available to practice!\n")
        return

    username = input("Enter your username: ")
    correct = 0
    total = 0
    words = list(vocab.items())
    random.shuffle(words)
    
    # Using f-strings for clean output
    print("\n===== PRACTICE QUIZ =====")
    print("You will be asked meanings of 5 random words.\n")

    # Determine how many words to quiz (up to 5)
    quiz_words = words[:min(len(words), 5)]

    for w, m in quiz_words: 
        # Using f-strings here as requested
        print(f"What is the meaning of '{w}'?")
        ans = input("Your answer: ").strip().lower()
        
        if ans in m.lower():
            print("Correct!\n")
            correct += 1
        else:
            # Using f-strings here as requested
            print(f"Wrong! Correct meaning: {m}\n")
        total += 1

    if total > 0:
        score = round((correct / total) * 100, 2)
        # Using f-strings here as requested
        print(f"Your Score: {score}%\n")

        # --- PROGRESS SAVING LOGIC (Similar to your original) ---
        
        # Initialize user's progress list if they don't exist, otherwise get existing list
        progress[username] = progress.get(username, [])
        
        # Append the current session score
        progress[username].append({"score": score})
        
        # Save progress directly within this function
        save_progress(progress)
        print("Progress saved successfully!\n")
    else:
        print("Not enough words for a quiz session.\n")'''





import random
from database import load_data, save_data

def pick_questions(level=None, n=5):
    data = load_data()
    vocab = data["vocabulary"]
    if level:
        vocab = [v for v in vocab if v["level"].lower() == level.lower()]
    if not vocab:
        return []
    return random.sample(vocab, min(n, len(vocab)))

def record_quiz_result(username, score):
    data = load_data()
    data.setdefault("progress", {})
    data["progress"].setdefault(username, {"quizzes": []})
    data["progress"][username]["quizzes"].append(score)
    save_data(data)
