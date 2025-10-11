'''import json
import os
import sqlite3

DB_FILE = "data.json"

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "users": {},
            "vocabulary": [],
            "notes": {},
            "progress": {}
        }

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
# Connect to database
def connect_db(db_name="language_platform.db"):
    return sqlite3.connect(db_name)
# Create tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vocabulary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT,
        meaning TEXT,
        level TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        correct INTEGER DEFAULT 0,
        total INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()
    print("Database and tables created successfully!")
# Insert sample vocabulary
def insert_sample_vocabulary():
    conn = connect_db()
    cursor = conn.cursor()

    # Check if already inserted
    cursor.execute("SELECT COUNT(*) FROM vocabulary")
    count = cursor.fetchone()[0]
    if count > 0:
        print("Vocabulary already exists, skipping insertion.")
        conn.close()
        return

    # Insert 60 words (Easy, Medium, Hard)
    easy_words = [
        ("apple", "a round fruit with red or green skin", "Easy"),
        ("book", "a set of written or printed pages", "Easy"),
        ("happy", "feeling or showing pleasure", "Easy"),
        ("fast", "moving quickly", "Easy"),
        ("friend", "a person you know and like", "Easy")
    ]
    medium_words = [
        ("brave", "showing courage", "Medium"),
        ("clever", "quick to understand", "Medium"),
        ("polite", "showing good manners", "Medium"),
        ("depend", "to rely on someone", "Medium"),
        ("travel", "to go from one place to another", "Medium")
    ]
    hard_words = [
        ("benevolent", "kind and generous", "Hard"),
        ("diligent", "hard-working", "Hard"),
        ("lucid", "clear and easy to understand", "Hard"),
        ("prudent", "acting with care", "Hard"),
        ("serene", "calm and peaceful", "Hard")
    ]

    all_words = easy_words + medium_words + hard_words
    cursor.executemany("INSERT INTO vocabulary (word, meaning, level) VALUES (?, ?, ?)", all_words)

    conn.commit()
    conn.close()
    print("Sample vocabulary added successfully!")
# View vocabulary by level
def get_words(level):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT word, meaning FROM vocabulary WHERE level=?", (level,))
    words = cursor.fetchall()
    conn.close()
    return words'''


import json
import os

DB_FILE = "database.json"

# Preloaded global vocabulary dataset
DEFAULT_VOCAB = [
    {"word": "hello", "meaning": "a greeting", "level": "Easy"},
    {"word": "beautiful", "meaning": "pleasing the senses or mind", "level": "Easy"},
    {"word": "complicated", "meaning": "consisting of many interconnecting parts", "level": "Medium"},
    {"word": "appreciate", "meaning": "to recognize the full worth of something", "level": "Medium"},
    {"word": "benevolent", "meaning": "well meaning and kindly", "level": "Hard"},
    {"word": "meticulous", "meaning": "showing great attention to detail", "level": "Hard"},
    {"word": "serene", "meaning": "calm, peaceful, and untroubled", "level": "Easy"},
    {"word": "ambiguous", "meaning": "open to more than one interpretation", "level": "Medium"},
    {"word": "arduous", "meaning": "involving or requiring strenuous effort", "level": "Hard"},
    {"word": "eloquent", "meaning": "fluent or persuasive in speaking", "level": "Hard"},
    {"word": "innovate", "meaning": "to make changes in something established", "level": "Medium"},
    {"word": "diligent", "meaning": "showing care in one’s work", "level": "Medium"},
    {"word": "optimistic", "meaning": "hopeful and confident about the future", "level": "Easy"},
    {"word": "pragmatic", "meaning": "dealing with things sensibly and realistically", "level": "Medium"},
    {"word": "reliable", "meaning": "consistently good in quality or performance", "level": "Easy"},
    {"word": "versatile", "meaning": "able to adapt to many functions or activities", "level": "Medium"},
    {"word": "vulnerable", "meaning": "susceptible to physical or emotional harm", "level": "Hard"},
    {"word": "grateful", "meaning": "feeling or showing appreciation", "level": "Easy"},
    {"word": "ambition", "meaning": "a strong desire to achieve something", "level": "Easy"},
    {"word": "curiosity", "meaning": "a strong desire to know or learn something", "level": "Easy"}
]

def _ensure():
    """Ensure DB file exists with structure and preload dataset."""
    if not os.path.exists(DB_FILE):
        base = {
            "users": {},
            "vocabulary": DEFAULT_VOCAB,
            "notes": {},
            "progress": {},
            "flashcards": []
        }
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(base, f, indent=4)
    else:
        with open(DB_FILE, "r+", encoding="utf-8") as f:
            data = json.load(f)
            existing = [v["word"].lower() for v in data.get("vocabulary", [])]
            for w in DEFAULT_VOCAB:
                if w["word"].lower() not in existing:
                    data["vocabulary"].append(w)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

def load_data():
    _ensure()
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
