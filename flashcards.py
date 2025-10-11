'''import json
import os
import random

VOCAB_FILE = "vocab.json"

def load_vocab():
    """Load words from vocab file."""
    if not os.path.exists(VOCAB_FILE):
        return {}
    with open(VOCAB_FILE, "r") as f:
        return json.load(f)

def flashcard_menu():
    """Show vocabulary using flashcards."""
    vocab = load_vocab()
    if not vocab:
        print("No words to show in flashcards!\n")
        return

    words = list(vocab.items())
    random.shuffle(words)

    print("\n===== FLASHCARD MODE =====")
    print("Press Enter to reveal meaning, 'q' to quit.\n")

    for w, m in words:
        user_input = input("Word: {}  → Press Enter for meaning: ".format(w))
        if user_input.lower() == "q":
            break
        print("Meaning: {}\n".format(m))'''



'''import json
import os
import random

VOCAB_FILE = "vocab.json"

def load_vocab():
    """Load words from vocab file."""
    if not os.path.exists(VOCAB_FILE):
        return {}
    with open(VOCAB_FILE, "r") as f:
        return json.load(f)

def flashcard_menu():
    """Show vocabulary using flashcards."""
    vocab = load_vocab()
    if not vocab:
        print("No words to show in flashcards!\n")
        return

    words = list(vocab.items())
    random.shuffle(words)

    print("\n===== FLASHCARD MODE =====")
    print("Press Enter to reveal meaning, 'q' to quit.\n")

    for w, m in words:
        user_input = input("Word: {}  → Press Enter for meaning: ".format(w))
        if user_input.lower() == "q":
            break
        print("Meaning: {}\n".format(m))'''





import random
from database import load_data

def get_flashcards(level=None, n=10):
    data = load_data()
    vocab = data["vocabulary"]
    if level:
        vocab = [v for v in vocab if v["level"].lower() == level.lower()]
    random.shuffle(vocab)
    return vocab[:min(n, len(vocab))]
