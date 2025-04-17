import tkinter as tk
from tkinter import messagebox
import threading
import connect as conn

def open_login_window(index):
    def create_window():
        window = tk.Toplevel()
        window.title(f"Login Window {index + 1}")

        frame = tk.Frame(window, padx=10, pady=10)
        frame.pack()

        tk.Label(frame, text='Login Page', font=('Arial', 24)).grid(row=0, column=1, pady=10)

        tk.Label(frame, text='Username').grid(row=1, column=0, padx=5, sticky='e')
        entry_username = tk.Entry(frame)
        entry_username.grid(row=1, column=1, padx=5, sticky='ew')

        tk.Label(frame, text='Password').grid(row=2, column=0, padx=5, sticky='e')
        entry_password = tk.Entry(frame, show='*')
        entry_password.grid(row=2, column=1, padx=5, sticky='ew')

        def toggle_password():
            if show_password_var.get():
                entry_password.config(show='')
            else:
                entry_password.config(show='*')

        show_password_var = tk.BooleanVar()
        tk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password).grid(row=3, column=1, padx=5, sticky='w')

        result_label = tk.Label(frame, text="")
        result_label.grid(row=5, column=1, pady=10)

        def execute_login():
            username = entry_username.get().strip()
            password = entry_password.get().strip()
            if not username or not password:
                result_label.config(text="Please enter both username and password.", fg="red")
                return
            try:
                query = "SELECT username FROM users WHERE username = ? AND password = ?"
                conn.cursor.execute(query, (username, password))
                if conn.cursor.fetchone():
                    result_label.config(text="Login Successful", fg="green")
                    login_button.config(state="disabled")
                    show_subject_selection(window)
                else:
                    result_label.config(text="Invalid Username or Password", fg="red")
            except Exception as e:
                messagebox.showerror("Login Error", str(e))

        login_button = tk.Button(frame, text='Login', command=execute_login)
        login_button.grid(row=4, column=1, padx=5, pady=5)

    threading.Thread(target=create_window).start()

def show_subject_selection(parent_window):
    parent_window.destroy()
    subject_window = tk.Toplevel()
    subject_window.title("Subject Selection")

    frame = tk.Frame(subject_window, padx=20, pady=20)
    frame.pack()

    tk.Label(frame, text="Choose a Subject", font=("Arial", 18)).pack(pady=10)

    try:
        conn.cursor.execute("SELECT subject_name FROM subjects")
        subjects = conn.cursor.fetchall()

        if not subjects:
            messagebox.showinfo("No Subjects", "No subjects available in the database.")
            subject_window.destroy()
            return

        selected_subject = tk.StringVar(value=None)

        for subject in subjects:
            tk.Radiobutton(
                frame, text=subject[0], variable=selected_subject, value=subject[0], font=("Arial", 14)
            ).pack(anchor="w", padx=20, pady=5)

        def on_select_subject():
            if selected_subject.get():
                show_available_questions(subject_window, selected_subject.get())
            else:
                messagebox.showwarning("Selection Error", "Please select a subject.")

        tk.Button(frame, text="Select", command=on_select_subject).pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch subjects: {e}")

def show_available_questions(parent_window, subject_name):
    parent_window.destroy()
    question_window = tk.Toplevel()
    question_window.title(f"Questions for {subject_name}")

    frame = tk.Frame(question_window, padx=20, pady=20)
    frame.pack()

    # Set exam duration (in seconds)
    exam_duration = 7200   #5 minutes

    def update_timer():
        nonlocal exam_duration
        if exam_duration > 0:
            minutes, seconds = divmod(exam_duration, 60)
            timer_label.config(text=f"Time Remaining: {minutes:02}:{seconds:02}")
            exam_duration -= 1
            question_window.after(1000, update_timer)
        else:
            messagebox.showinfo("Time Up", "Time is up! Submitting your answers.")
            calculate_score()

    try:
        conn.cursor.execute("SELECT id FROM subjects WHERE subject_name = ?", (subject_name,))
        subject_id = conn.cursor.fetchone()

        if not subject_id:
            messagebox.showinfo("No Questions", f"No questions available for {subject_name}.")
            question_window.destroy()
            return

        conn.cursor.execute(""" 
            SELECT question_id, question, option1, option2, option3, option4, correct_option
            FROM question_bank
            WHERE subject_id = ? 
        """, (subject_id[0],))
        questions = conn.cursor.fetchall()

        if not questions:
            messagebox.showinfo("No Questions", f"No questions available for {subject_name}.")
            question_window.destroy()
            return

        tk.Label(frame, text=f"Questions for {subject_name}", font=("Arial", 18)).pack(pady=10)

        # Timer label
        timer_label = tk.Label(frame, text="", font=("Arial", 14), fg="red")
        timer_label.pack(pady=5)

        user_answers = {}

        def calculate_score():
            score = 0
            for question_id, answer in user_answers.items():
                conn.cursor.execute("SELECT correct_option FROM question_bank WHERE question_id = ?", (question_id,))
                correct_answer = conn.cursor.fetchone()
                if correct_answer and answer.get() == str(correct_answer[0]):
                    score += 1
            messagebox.showinfo("Quiz Result", f"Your score: {score}/{len(questions)}")
            question_window.destroy()

        for idx, (question_id, question, opt1, opt2, opt3, opt4, correct) in enumerate(questions):
            tk.Label(frame, text=f"Q{idx + 1}. {question}", font=("Arial", 14)).pack(anchor="w", pady=5)

            selected_answer = tk.StringVar(value=None)
            user_answers[question_id] = selected_answer

            for opt_idx, option in enumerate([opt1, opt2, opt3, opt4], start=1):
                tk.Radiobutton(
                    frame, text=option, variable=selected_answer, value=str(opt_idx), font=("Arial", 12)
                ).pack(anchor="w", padx=20)

        tk.Button(frame, text="Submit", command=calculate_score).pack(pady=10)

        # Start the timer
        update_timer()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch questions: {e}")

def count_users():
    try:
        query = "SELECT COUNT(*) FROM users"
        conn.cursor.execute(query)
        result = conn.cursor.fetchone()
        return result[0]
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None

def main_window():
    root = tk.Tk()
    root.title("User Count Check")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    tk.Label(frame, text="Number of Users:").grid(row=0, column=0, pady=5)
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, pady=5)

    def on_submit():
        try:
            user_input = int(entry.get())
            user_count = count_users()
            if user_input <= user_count:
                for i in range(user_input):
                    threading.Thread(target=open_login_window, args=(i,)).start()
                root.withdraw()
            else:
                messagebox.showerror("Error", "Insufficient number of users.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    tk.Button(frame, text="Submit", command=on_submit).grid(row=1, column=0, columnspan=2, pady=10)
    root.mainloop()

if __name__ == "__main__":
    main_window()
