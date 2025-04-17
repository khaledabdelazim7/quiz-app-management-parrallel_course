import tkinter as tk
import connect as conn


# view or show password function

def toggle_password():
    if show_password_var.get():  
        password_entry.config(show='')  
    else:
        password_entry.config(show='*')  


# checking login function

def login_action():
    
    username = entry_username.get()
    password = password_entry.get()
    
    # Check login values
    if username == 'admin' and password == 'admin':
        result = "Login Successful"
        fg_color = "green"
        result_label.config(text=result, fg=fg_color)
        login_button.config(state="disabled")

        # Wait for 2 seconds before showing the next options
        r.after(2000, clear_login_widgets_and_show_options)  
    else:
        result = "Invalid Username or Password"
        fg_color = "red"
        result_label.config(text=result, fg=fg_color)

# clear everything in login window and going to admin dashboard

def clear_login_widgets_and_show_options():
    username_label.grid_forget()
    entry_username.grid_forget()
    password_label.grid_forget()
    password_entry.grid_forget()
    show_password_checkbox.grid_forget()
    login_button.grid_forget()
    result_label.grid_forget()

    
    title_label.config(text="Admin Dashboard")
    add_remove_user_button.grid(row=1, column=1, pady=10, sticky='ew')
    add_questions_button.grid(row=2, column=1, pady=10, sticky='ew')
    add_subjects_button.grid(row=3, column=1, pady=10, sticky='ew')
    back_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')


# functions for add or remove user options

def show_add_remove_user_options():
    title_label.config(text="Manage Users")
    add_remove_user_button.grid_forget()
    add_questions_button.grid_forget()
    add_subjects_button.grid_forget()

    add_user_button.grid(row=1, column=1, pady=10, sticky='ew')
    remove_user_button.grid(row=2, column=1, pady=10, sticky='ew')
    back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')


# add user function

def add_user():
    title_label.config(text="Add User")
    remove_user_button.grid_forget()
    add_user_button.grid_forget()

    firstname_label_add_user = tk.Label(frame, text="firstname")
    firstname_label_add_user.grid(row=1, column=1, sticky='e', padx=5, pady=5)

    entry_firstname_add_user = tk.Entry(frame)
    entry_firstname_add_user.grid(row=1, column=2, sticky='ew', padx=5, pady=5)

    lastname_label_add_user = tk.Label(frame, text="lastname")
    lastname_label_add_user.grid(row=2, column=1, sticky='e', padx=5, pady=5)

    entry_lastname_add_user = tk.Entry(frame)
    entry_lastname_add_user.grid(row=2, column=2, sticky='ew', padx=5, pady=5)

    password_label_add_user = tk.Label(frame, text="Password")
    password_label_add_user.grid(row=3, column=1, sticky='e', padx=5, pady=5)

    entry_password_add_user = tk.Entry(frame, show='*')
    entry_password_add_user.grid(row=3, column=2, sticky='ew', padx=5, pady=5)

    add_button = tk.Button(frame, text="Add", command=lambda: execute_add_user(entry_firstname_add_user,entry_lastname_add_user, entry_password_add_user))
    add_button.grid(row=4, column=2, columnspan=3, pady=10, sticky='ew')

# function to insert users data into database
def execute_add_user(entry_firstname_add_user, entry_lastname_add_user, entry_password_add_user):
    username = entry_firstname_add_user.get() + entry_lastname_add_user.get()
    password = entry_password_add_user.get()

    # Insert the user data into the database
    try:
        conn.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.cursor.commit() 
        print('User is added')
    except Exception as e:
        print(f"Error: {e}")

    # Back button to return to the Admin Dashboard
    back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

# remove user function

def remove_user():
    title_label.config(text="Remove User")
    remove_user_button.grid_forget()
    add_user_button.grid_forget()

    username_label_remove_user = tk.Label(frame, text="Username")
    username_label_remove_user.grid(row=1, column=1, sticky='e', padx=5, pady=5)

    entry_username_remove_user = tk.Entry(frame)
    entry_username_remove_user.grid(row=1, column=2, sticky='ew', padx=2, pady=5) 

    password_label_remove_user = tk.Label(frame, text="Password")
    password_label_remove_user.grid(row=2, column=1, sticky='e', padx=5, pady=5)

    entry_password_remove_user = tk.Entry(frame, show='*')
    entry_password_remove_user.grid(row=2, column=2, sticky='ew', padx=1, pady=5) 

    remove_button = tk.Button(frame, text="Remove", command=lambda: execute_remove_user(entry_username_remove_user))
    remove_button.grid(row=3, column=1, columnspan=2, pady=10, sticky='ew')

# Remove the user data from the database

def execute_remove_user(entry_username_remove_user):
    username = entry_username_remove_user.get()
    try:
        
        exec = conn.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.cursor.commit()  
        if exec:
            print('User is removed')
        else:
            print("user is not found")
    except Exception as e:
        print(f"Error: {e}")
    back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')



# functions for add or remove questions

def show_add_remove_questions_options():
    title_label.config(text="Manage Questions")
    add_remove_user_button.grid_forget()
    add_questions_button.grid_forget()
    add_subjects_button.grid_forget()

    add_question_button.grid(row=1, column=1, pady=10, sticky='ew')
    remove_question_button.grid(row=2, column=1, pady=10, sticky='ew')
    back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')


# add question function
def add_questions():
    print("Add Questions function")
    title_label.config(text="Add question")
    remove_question_button.grid_forget()
    add_question_button.grid_forget()

    question_label_add_question = tk.Label(frame, text="Question")
    question_label_add_question.grid(row=1, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_question = tk.Entry(frame)
    entry_question_add_question.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

    # enter subject name
    question_label_add_subjectname = tk.Label(frame, text="Subject Name")
    question_label_add_subjectname.grid(row=2, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_subjectname = tk.Entry(frame)
    entry_question_add_subjectname.grid(row=2, column=1, sticky='ew', padx=5, pady=5)

    # enter choice 1 info
    question_label_add_option1 = tk.Label(frame, text="Option 1")
    question_label_add_option1.grid(row=3, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_question_option1 = tk.Entry(frame)
    entry_question_add_question_option1.grid(row=3, column=1, sticky='ew', padx=5, pady=5)

    # enter choice 2 info
    question_label_add_option2 = tk.Label(frame, text="Option 2")
    question_label_add_option2.grid(row=4, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_question_option2 = tk.Entry(frame)
    entry_question_add_question_option2.grid(row=4, column=1, sticky='ew', padx=5, pady=5)

    # enter choice 3 info
    question_label_add_option3 = tk.Label(frame, text="Option 3")
    question_label_add_option3.grid(row=5, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_question_option3 = tk.Entry(frame)
    entry_question_add_question_option3.grid(row=5, column=1, sticky='ew', padx=5, pady=5)

    # enter choice 4 info
    question_label_add_option4 = tk.Label(frame, text="Option 4")
    question_label_add_option4.grid(row=6, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_question_option4 = tk.Entry(frame)
    entry_question_add_question_option4.grid(row=6, column=1, sticky='ew', padx=5, pady=5)

    # enter correct choices number
    question_label_add_correct_option = tk.Label(frame, text="Correct Option (1-4)")
    question_label_add_correct_option.grid(row=7, column=0, sticky='e', padx=5, pady=5)
    entry_question_add_question_correct_option = tk.Entry(frame)
    entry_question_add_question_correct_option.grid(row=7, column=1, sticky='ew', padx=5, pady=5)

    add_button = tk.Button(frame, text="Add", command=lambda: execute_add_question(
        entry_question_add_question,
        entry_question_add_subjectname,
        entry_question_add_question_option1,
        entry_question_add_question_option2,
        entry_question_add_question_option3,
        entry_question_add_question_option4,
        entry_question_add_question_correct_option
    ))
    add_button.grid(row=8, column=0, columnspan=2, pady=10, sticky='ew')


    # function to insert question data into database
    def execute_add_question(entry_question_add_question,entry_question_add_subjectname,entry_question_add_question_option1,entry_question_add_question_option2,entry_question_add_question_option3,entry_question_add_question_option4,entry_question_add_question_correct_option):
        try:
            
            # select the subject ID from subjects table 
            conn.cursor.execute("SELECT id FROM subjects WHERE subject_name = ?", (entry_question_add_subjectname.get(),))
            subject_id = conn.cursor.fetchone()

            if subject_id is None:
                print("Error: Subject not found.")
                return
            
            # Insert the question into the database
            conn.cursor.execute(
                "INSERT INTO question_bank (subject_id, question, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    subject_id[0],
                    entry_question_add_question.get(),
                    entry_question_add_question_option1.get(),
                    entry_question_add_question_option2.get(),
                    entry_question_add_question_option3.get(),
                    entry_question_add_question_option4.get(),
                    entry_question_add_question_correct_option.get()
                )
            )
            conn.cursor.commit() 
            print("Question added successfully!")
        except Exception as e:
            print(f"Error: {e}")
        back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

# remove questions        
def remove_questions():
        print("remove Questions function")
        title_label.config(text="Remove question")

        remove_question_button.grid_forget()
        add_question_button.grid_forget()

        question_label_remove_question = tk.Label(frame, text="Question")
        question_label_remove_question.grid(row=1, column=0, sticky='e', padx=5, pady=5)
        entry_question_remove_question = tk.Entry(frame)
        entry_question_remove_question.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

        question_label_remove_subjectname = tk.Label(frame, text="Subject Name")
        question_label_remove_subjectname.grid(row=2, column=0, sticky='e', padx=5, pady=5)
        entry_question_remove_subjectname = tk.Entry(frame)
        entry_question_remove_subjectname.grid(row=2, column=1, sticky='ew', padx=5, pady=5)


        remove_button = tk.Button(frame, text="remove", command=lambda: execute_remove_question(
        entry_question_remove_question,
        entry_question_remove_subjectname,
      
    ))
        remove_button.grid(row=8, column=0, columnspan=2, pady=10, sticky='ew')

# function to remove question data from database
def execute_remove_question(entry_question_reomve_question,entry_question_remove_subjectname,):
 try:
           
            conn.cursor.execute("SELECT id FROM subjects WHERE subject_name = ?", (entry_question_remove_subjectname.get(),))
            subject_id = conn.cursor.fetchone()

            if subject_id is None:
                print("Error: Subject not found.")
                return
            
            conn.cursor.execute(
                    "DELETE FROM question_bank WHERE subject_id = ? AND question = ?",

                (
                    subject_id[0],
                    entry_question_reomve_question.get()
                )
            )
            conn.cursor.commit()  
            print("Question removed successfully!")
 except Exception as e:
            print(f"Error: {e}")
            back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
    

# functions for add or remove subjects
def show_add_remove_subject_options():
    title_label.config(text="Manage Subjects")

    add_remove_user_button.grid_forget()
    add_questions_button.grid_forget()
    add_subjects_button.grid_forget()

    add_subject_button.grid(row=1, column=1, pady=10, sticky='ew')
    remove_subject_button.grid(row=2, column=1, pady=10, sticky='ew')
    back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

# functions to add subject
def add_subjects():
    print("Add Subjects function")


    title_label.config(text="Add Subject")

    remove_subject_button.grid_forget()
    add_subject_button.grid_forget()

    subject_label_add_subject = tk.Label(frame, text="subjectname")
    subject_label_add_subject.grid(row=1, column=1, sticky='e', padx=5, pady=5)

    entry_subjectname_add_subject = tk.Entry(frame)
    entry_subjectname_add_subject.grid(row=1, column=2, sticky='ew', padx=5, pady=5)

    add_button = tk.Button(frame, text="Add", command=lambda: execute_add_subject(entry_subjectname_add_subject))
    add_button.grid(row=4, column=2, columnspan=3, pady=10, sticky='ew')

# insert subject into database
def execute_add_subject(entry_subjectname_add_subject):
    subject_name=entry_subjectname_add_subject.get()
    try:
        conn.cursor.execute("INSERT INTO subjects (subject_name) VALUES (?)", (subject_name,))
        conn.cursor.commit()  
        print('subject is added')
    except Exception as e:
        print(f"Error: {e}")



# functions to remove subject
def remove_subjects():
    title_label.config(text="Remove Subject")
    
    add_subject_button.grid_forget()
    remove_subject_button.grid_forget()

    subject_label_remove_subject = tk.Label(frame, text="Subject Name")
    subject_label_remove_subject.grid(row=1, column=0, sticky='e', padx=5, pady=5)

    entry_subject_name_remove_subject = tk.Entry(frame)
    entry_subject_name_remove_subject.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

    confirm_remove_button = tk.Button(frame, text="Remove", command=execute_remove_subject(entry_subject_name_remove_subject))
    confirm_remove_button.grid(row=2, column=1, pady=10, sticky='ew')
    back_to_dashboard_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

# functions to remove subject from database
def execute_remove_subject(entry_subject_name_remove_subject):
    subject_name = entry_subject_name_remove_subject.get()
    try:
        exec = conn.cursor.execute("DELETE FROM subjects WHERE subject_name = ?", (subject_name,))
        conn.cursor.commit()
        if exec:
            print("Subject removed")
        else:
            print("Subject not found")
    except Exception as e:
        print(f"Error: {e}")

# functionality of back button
def go_back():

    for widget in frame.winfo_children():
        widget.grid_forget()

    title_label.config(text="Admin Dashboard")
    
    add_remove_user_button.grid(row=1, column=1, pady=10, sticky='ew')
    add_questions_button.grid(row=2, column=1, pady=10, sticky='ew')
    add_subjects_button.grid(row=3, column=1, pady=10, sticky='ew')
    
    back_button.grid(row=0, column=0, padx=5, pady=5, sticky='nw')






########################################################
# Initialize the main window
r = tk.Tk()
r.title('Quiz Platform')

# Set fixed window size
r.geometry('600x500')  
r.resizable(False, False)  # Prevent window resizing

frame = tk.Frame(r, padx=20, pady=20)
frame.grid(row=0, column=0, sticky='nsew')

frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
frame.columnconfigure([0, 1, 2], weight=1)


title_label = tk.Label(frame, text='Login page', font=('Arial', 24))
title_label.grid(row=0, column=1, pady=10, sticky='nsew')


username_label = tk.Label(frame, text='Username')
username_label.grid(row=1, column=0, sticky='e', padx=5)

entry_username = tk.Entry(frame)
entry_username.grid(row=1, column=1, sticky='ew', padx=5)

password_label = tk.Label(frame, text='Password')
password_label.grid(row=2, column=0, sticky='e', padx=5)

password_entry = tk.Entry(frame, show='*')
password_entry.grid(row=2, column=1, sticky='ew', padx=5)

# Show Password checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_checkbox.grid(row=3, column=1, sticky='w', padx=5)

# login button
login_button = tk.Button(frame, text='Login', command=login_action)
login_button.grid(row=4, column=1, sticky='ew', padx=5, pady=5)

# Label to show login result
result_label = tk.Label(frame, text="")
result_label.grid(row=5, column=1, pady=10)

# main dashboard after login

add_remove_user_button = tk.Button(frame, text="Add/Remove User",command=show_add_remove_user_options)
add_questions_button = tk.Button(frame, text="Add/Remove Questions", command=show_add_remove_questions_options)
add_subjects_button = tk.Button(frame, text="Add/Remove Subjects", command=show_add_remove_subject_options)
back_button = tk.Button(frame, text="← Back", command=go_back, relief="flat", font=('Arial', 12))


add_user_button = tk.Button(frame, text="Add User", command=add_user)
remove_user_button = tk.Button(frame, text="Remove User", command=remove_user)

add_subject_button = tk.Button(frame, text="Add Subject", command=add_subjects)
remove_subject_button = tk.Button(frame, text="Remove Subject", command=remove_subjects)

add_question_button = tk.Button(frame, text="add question", command=add_questions)
remove_question_button = tk.Button(frame, text="Remove question", command=remove_questions)
back_to_dashboard_button = tk.Button(frame, text="← Back", command=go_back, relief="flat", font=('Arial', 12))

# Start the main event loop
r.mainloop()