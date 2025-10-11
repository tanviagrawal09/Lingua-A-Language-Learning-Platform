'''from quiz import start_practice
from flashcards import flashcard_menu
from progress import show_progress

def main_menu():
    while True:
        print("\n===== LANGUAGE PRACTICE PLATFORM =====")
        print("1. Practice Words (Quiz Mode)")
        print("2. Flashcards Mode")
        print("3. Progress Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_practice()
        elif choice == "2":
            flashcard_menu()
        elif choice == "3":
            show_progress()
        elif choice == "4":
            print("Exiting... Thank you for using the platform!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()'''

'''print(">>>main.py started running\n")
import user_management
import vocabulary
import notes
import dictionary
import quiz
import flashcards
import progress

def main():
    print("Welcome to Language Practice Platform")
    
    current_user = None

    while True:
        if not current_user:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter new username: ")
                password = input("Enter password: ")
                user_management.register(username, password)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if user_management.login(username, password):
                    current_user = username
                    print(f"\nWelcome, {current_user}!")
                else:
                    print("Invalid login details.")

            elif choice == '3':
                print("Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")

        else:
            print(f"\nLogged in as: {current_user}")
            print("1. Vocabulary Practice")
            print("2. Notes")
            print("3. Personal Dictionary")
            print("4. Quiz")
            print("5. Flashcards")
            print("6. Progress Tracker")
            print("7. Logout")
            
            choice = input("Select an option: ")

            if choice == '1':
                print("\n-- Vocabulary Practice --")
                vocabulary.practice_vocabulary(current_user)

            elif choice == '2':
                print("\n-- Notes --")
                notes_menu(current_user)

            elif choice == '3':
                print("\n-- Personal Dictionary --")
                dictionary_menu(current_user)

            elif choice == '4':
                print("\n-- Quiz --")
                quiz.take_quiz(current_user)

            elif choice == '5':
                print("\n-- Flashcards --")
                flashcards.show_flashcards(current_user)

            elif choice == '6':
                print("\n-- Progress Tracker --")
                progress.view_progress(current_user)

            elif choice == '7':
                print(f"Logged out, {current_user}!")
                current_user = None
            else:
                print("Invalid choice, please try again.")


# ---- Helper Menus ----

def notes_menu(user):
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")
        ch = input("Enter choice: ")

        if ch == '1':
            note = input("Enter your note: ")
            notes.add_note(user, note)
        elif ch == '2':
            notes.view_notes(user)
        elif ch == '3':
            index = int(input("Enter note number to delete: ")) - 1
            notes.delete_note(user, index)
        elif ch == '4':
            break
        else:
            print("Invalid choice.")

def dictionary_menu(user):
    while True:
        print("\n1. Add Word")
        print("2. View Words")
        print("3. Search Word")
        print("4. Delete Word")
        print("5. Back")
        ch = input("Enter choice: ")

        if ch == '1':
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            dictionary.add_word(user, word, meaning)
        elif ch == '2':
            dictionary.view_words(user)
        elif ch == '3':
            word = input("Enter word to search: ")
            dictionary.search_word(user, word)
        elif ch == '4':
            word = input("Enter word to delete: ")
            dictionary.delete_word(user, word)
        elif ch == '5':
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()'''





'''from user_management import *
from vocabulary import *
from notes import *
from dictionary import *
from quiz import *
from flashcards import *
from progress import *

def main():
    print("\n=== Language Practice Platform ===")
    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Add Note")
        print("4. View Notes")
        print("5. Search Word in Dictionary")
        print("6. Start Quiz")
        print("7. Flashcards")
        print("8. View Progress")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user(input("Enter username: "), input("Enter password: "))
        elif choice == '2':
            login_user(input("Enter username: "), input("Enter password: "))
        elif choice == '3':
            add_note(input("Word: "), input("Meaning: "))
        elif choice == '4':
            view_notes()
        elif choice == '5':
            search_word(input("Enter word: "))
        elif choice == '6':
            start_practice()
        elif choice == '7':
            flashcard_menu()
        elif choice == '8':
            show_progress()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()'''


'''#filepath: d:\abcd\main.py
print("main.py is running")
from user_management import *
from vocabulary import *
from notes import *
from dictionary import *
from quiz import *
from flashcards import *
from progress import *

def main():
    print("=== Language Practice Platform ===")
    username = None

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Add Vocabulary Word")
        print("4. View Vocabulary")
        print("5. Add Note")
        print("6. View Notes")
        print("7. Search Word")
        print("8. Start Quiz")
        print("9. Flashcards")
        print("10. View Progress")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            username=login_user()
        elif choice == '3':
            if username:
                add_word()
            else:
                print("Please login first.")
        elif choice == '4':
            if username:
                view_by_level()
            else:
                print("Please login first.")
        elif choice == '5':
            if username:
                add_note()
            else:
                print("Please login first.")
        elif choice == '6':
            if username:
                view_notes()
            else:
                print("Please login first.")
        elif choice == '7':
            search_word()
        elif choice == '8':
            if username:
                start_practice()
            else:
                print("Please login first.")
        elif choice == '9':
            flashcard_menu()
        elif choice == '10':
            if username:
                show_progress()
            else:
                print("Please login first.")
        elif choice == '11':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()'''






# main_gui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import user_management
import vocabulary
import notes
import dictionary
import quiz
import flashcards
import progress

APP_TITLE = "Language Practice Platform"

class App:
    def __init__(self, root):
        self.root = root
        root.title(APP_TITLE)
        root.geometry("600x520")
        self.current_user = None
        self.create_login_frame()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # ----- LOGIN / REGISTER -----
    def create_login_frame(self):
        self.clear()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text="Language Practice Platform", font=("Arial", 20, "bold")).pack(pady=8)
        ttk.Label(frame, text="Username:").pack(anchor="w", pady=(8,0))
        self.username_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.username_var).pack(fill="x")

        ttk.Label(frame, text="Password:").pack(anchor="w", pady=(8,0))
        self.password_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.password_var, show="*").pack(fill="x")

        btns = ttk.Frame(frame)
        btns.pack(pady=12)
        ttk.Button(btns, text="Login", command=self.login).grid(row=0, column=0, padx=6)
        ttk.Button(btns, text="Register", command=self.register).grid(row=0, column=1, padx=6)
        ttk.Button(frame, text="Continue as Guest", command=self.continue_as_guest).pack(pady=6)

    def register(self):
        u = self.username_var.get().strip()
        p = self.password_var.get().strip()
        if not u or not p:
            messagebox.showwarning("Input", "Enter username and password.")
            return
        ok, msg = user_management.register_user(u, p)
        if ok:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)

    def login(self):
        u = self.username_var.get().strip()
        p = self.password_var.get().strip()
        ok, msg = user_management.login_user(u, p)
        if ok:
            self.current_user = u
            messagebox.showinfo("Welcome", f"Hello, {u}!")
            self.create_main_menu()
        else:
            messagebox.showerror("Login Failed", msg)

    def continue_as_guest(self):
        self.current_user = "guest"
        self.create_main_menu()

    # ----- MAIN MENU -----
    def create_main_menu(self):
        self.clear()
        frame = ttk.Frame(self.root, padding=12)
        frame.pack(expand=True, fill="both")

        ttk.Label(frame, text=f"Logged in as: {self.current_user}", font=("Arial", 12)).pack(anchor="w")
        ttk.Separator(frame).pack(fill="x", pady=6)

        buttons = [
            ("Vocabulary Manager", self.vocab_window),
            ("Take Quiz", self.quiz_window),
            ("Flashcards", self.flashcards_window),
            ("Notes & Dictionary", self.notes_window),
            ("Progress", self.progress_window),
            ("Logout", self.logout),
            ("Exit", self.root.destroy)
        ]

        for txt, cmd in buttons:
            ttk.Button(frame, text=txt, command=cmd).pack(fill="x", pady=6)

    def logout(self):
        self.current_user = None
        self.create_login_frame()

    # ----- VOCABULARY WINDOW -----
    def vocab_window(self):
        w = tk.Toplevel(self.root)
        w.title("Vocabulary Manager")
        w.geometry("520x460")
        frame = ttk.Frame(w, padding=10); frame.pack(fill="both", expand=True)

        level_var = tk.StringVar(value="Easy")
        ttk.Label(frame, text="Level:").pack(anchor="w")
        ttk.Combobox(frame, textvariable=level_var, values=["Easy","Medium","Hard"]).pack(fill="x")

        ttk.Label(frame, text="Word:").pack(anchor="w", pady=(8,0))
        word_var = tk.StringVar(); ttk.Entry(frame, textvariable=word_var).pack(fill="x")
        ttk.Label(frame, text="Meaning:").pack(anchor="w", pady=(8,0))
        meaning_var = tk.StringVar(); ttk.Entry(frame, textvariable=meaning_var).pack(fill="x")

        def add_word_action():
            word = word_var.get().strip(); meaning = meaning_var.get().strip(); level = level_var.get()
            if not word or not meaning:
                messagebox.showwarning("Input", "Enter word and meaning.")
                return
            ok, msg = vocabulary.add_word(word, meaning, level)
            if ok:
                messagebox.showinfo("Added", msg); word_var.set(""); meaning_var.set(""); refresh_list()
            else:
                messagebox.showerror("Error", msg)

        ttk.Button(frame, text="Add Word", command=add_word_action).pack(pady=8)

        listbox = tk.Listbox(frame, height=14)
        listbox.pack(fill="both", expand=True, pady=6)

        def refresh_list():
            listbox.delete(0, tk.END)
            for item in vocabulary.get_words():
                listbox.insert(tk.END, f"{item['word']} ({item['level']}) : {item['meaning']}")

        def delete_selected():
            sel = listbox.curselection()
            if not sel:
                messagebox.showwarning("Select", "Select an item to delete.")
                return
            text = listbox.get(sel[0])
            word = text.split(" (")[0]
            ok, msg = vocabulary.delete_word(word)
            if ok:
                messagebox.showinfo("Deleted", msg)
                refresh_list()
            else:
                messagebox.showerror("Error", msg)

        ttk.Button(frame, text="Refresh List", command=refresh_list).pack(pady=4)
        ttk.Button(frame, text="Delete Selected", command=delete_selected).pack(pady=4)
        refresh_list()

    # ----- QUIZ WINDOW -----
    def quiz_window(self):
        w = tk.Toplevel(self.root); w.title("Quiz"); w.geometry("420x380")
        frame = ttk.Frame(w, padding=10); frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Select level (or leave blank for mixed):").pack(anchor="w")
        level_var = tk.StringVar(value="")
        ttk.Combobox(frame, textvariable=level_var, values=["", "Easy", "Medium", "Hard"]).pack(fill="x")

        def start_quiz_action():
            level = level_var.get() or None
            questions = quiz.pick_questions(level=level, n=5)
            if not questions:
                messagebox.showinfo("No words", "No words available for the selected level.")
                return
            score = 0
            for q in questions:
                ans = simpledialog.askstring("Quiz", f"What is the meaning of '{q['word']}'?")
                if ans and ans.strip().lower() == q['meaning'].strip().lower():
                    score += 1
            if self.current_user and self.current_user != "guest":
                quiz.record_quiz_result(self.current_user, score)
            messagebox.showinfo("Result", f"Your score: {score}/{len(questions)}")
        ttk.Button(frame, text="Start Quiz", command=start_quiz_action).pack(pady=12)

    # ----- FLASHCARDS WINDOW -----
    def flashcards_window(self):
        w = tk.Toplevel(self.root); w.title("Flashcards"); w.geometry("420x380")
        frame = ttk.Frame(w, padding=10); frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Select level (optional):").pack(anchor="w")
        level_var = tk.StringVar(value=""); ttk.Combobox(frame, textvariable=level_var, values=["", "Easy", "Medium", "Hard"]).pack(fill="x")
        text = tk.Text(frame, height=14); text.pack(fill="both", expand=True, pady=6)
        def show_cards():
            lv = level_var.get() or None
            cards = flashcards.get_flashcards(level=lv, n=10)
            if not cards:
                messagebox.showinfo("No cards", "No flashcards available.")
                return
            text.delete("1.0", tk.END)
            for c in cards:
                text.insert(tk.END, f"Word: {c['word']}\nMeaning: {c['meaning']}\n\n")
        ttk.Button(frame, text="Show Flashcards", command=show_cards).pack(pady=6)

    # ----- NOTES & DICTIONARY WINDOW -----
    def notes_window(self):
        w = tk.Toplevel(self.root); w.title("Notes & Dictionary"); w.geometry("540x520")
        frame = ttk.Frame(w, padding=10); frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Word:").pack(anchor="w")
        word_var = tk.StringVar(); ttk.Entry(frame, textvariable=word_var).pack(fill="x")
        ttk.Label(frame, text="Meaning / Note:").pack(anchor="w", pady=(6,0))
        meaning_var = tk.StringVar(); ttk.Entry(frame, textvariable=meaning_var).pack(fill="x")

        def add_note_action():
            if not self.current_user or self.current_user == "guest":
                messagebox.showwarning("Login", "You must be logged in to add notes.")
                return
            ok, msg = notes.add_note(self.current_user, word_var.get(), meaning_var.get())
            if ok:
                messagebox.showinfo("Added", msg); refresh_notes()
            else:
                messagebox.showerror("Error", msg)

        def delete_note_action():
            if not self.current_user or self.current_user == "guest":
                messagebox.showwarning("Login", "You must be logged in.")
                return
            word = word_var.get().strip()
            if not word:
                messagebox.showwarning("Input", "Enter word to delete its note.")
                return
            ok, msg = notes.delete_note(self.current_user, word)
            if ok:
                messagebox.showinfo("Deleted", msg); refresh_notes()
            else:
                messagebox.showerror("Error", msg)

        ttk.Button(frame, text="Add Note", command=add_note_action).pack(pady=6)
        ttk.Button(frame, text="Delete Note (by word)", command=delete_note_action).pack(pady=2)

        ttk.Separator(frame).pack(fill="x", pady=6)
        notes_text = tk.Text(frame, height=12); notes_text.pack(fill="both", expand=True)

        def refresh_notes():
            notes_text.delete("1.0", tk.END)
            if not self.current_user or self.current_user == "guest":
                notes_text.insert(tk.END, "Login to view notes.")
                return
            notes = notes.get_notes(self.current_user)
            if not notes:
                notes_text.insert(tk.END, "No notes found.")
                return
            for n in notes:
                notes_text.insert(tk.END, f"{n['word']} : {n['note']}\n")

        ttk.Button(frame, text="Refresh Notes", command=refresh_notes).pack(pady=6)
        refresh_notes()

        ttk.Separator(frame).pack(fill="x", pady=6)
        ttk.Label(frame, text="Search Vocabulary:").pack(anchor="w")
        search_var = tk.StringVar(); ttk.Entry(frame, textvariable=search_var).pack(fill="x")
        def do_search():
            if not search_var.get().strip():
                messagebox.showwarning("Input", "Enter a word to search.")
                return
            found, resp = dictionary.search_word(search_var.get())
            if found:
                messagebox.showinfo("Found", f"{search_var.get()} → {resp}")
            else:
                messagebox.showinfo("Not found", resp)
        ttk.Button(frame, text="Search", command=do_search).pack(pady=4)

    # ----- PROGRESS WINDOW -----
    def progress_window(self):
        if not self.current_user or self.current_user == "guest":
            messagebox.showwarning("Login", "Please login to view progress.")
            return
        w = tk.Toplevel(self.root); w.title("Progress"); w.geometry("420x300")
        frame = ttk.Frame(w, padding=10); frame.pack(fill="both", expand=True)
        p = progress.get_progress(self.current_user)
        quizzes = p.get("quizzes", [])
        ttk.Label(frame, text=f"Total quiz sessions: {len(quizzes)}").pack(anchor="w", pady=4)
        ttk.Label(frame, text=f"Scores: {quizzes}").pack(anchor="w", pady=4)
        avg = progress.get_average(self.current_user)
        ttk.Label(frame, text=f"Average score: {avg:.2f}").pack(anchor="w", pady=4)

def run_app():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
