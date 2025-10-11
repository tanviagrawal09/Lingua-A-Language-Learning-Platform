'''import json
import os

PROGRESS_FILE = "data/user_progress.json"

def load_progress():
    """Load progress data from file."""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def show_progress():
    """Display user's past quiz scores."""
    progress = load_progress()
    username = input("Enter your username: ")
    user_progress = progress.get(username, [])

    if not user_progress:
        print("No progress found for this user!\n")
        return

    print("\n===== PROGRESS REPORT =====")
    total_sessions = len(user_progress)
    avg_score = sum(item["score"] for item in user_progress) / total_sessions
    print("Total Practice Sessions: {}".format(total_sessions))
    print("Average Score: {:.2f}%\n".format(avg_score))'''


'''import json
import os

PROGRESS_FILE = "data/user_progress.json"

def load_progress():
    """Load progress data from file, handling JSON errors."""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If the JSON file is empty or corrupted, return an empty dictionary
        return {}
    except Exception as e:
        # Catch other file reading errors
        print(f"An error occurred reading progress file: {e}")
        return {}


def show_progress():
    """Display user's past quiz scores."""
    progress = load_progress()
    username = input("Enter your username: ")
    user_progress = progress.get(username, [])

    if not user_progress:
        print(f"No progress found for user '{username}'!\n")
        return

    print("\n===== PROGRESS REPORT =====")
    
    total_sessions = len(user_progress)
    
    # Calculate average score
    avg_score = sum(item["score"] for item in user_progress) / total_sessions
    
    # Use f-strings for clear, modern output
    print(f"Total Practice Sessions: {total_sessions}")
    print(f"Average Score: {avg_score:.2f}%\n")

# Example execution if run directly
if __name__ == "__main__":
    show_progress()'''






from database import load_data

def get_progress(username):
    data = load_data()
    return data.get("progress", {}).get(username, {"quizzes": []})

def get_average(username):
    progress = get_progress(username)
    quizzes = progress.get("quizzes", [])
    if not quizzes:
        return 0.0
    return sum(quizzes) / len(quizzes)
