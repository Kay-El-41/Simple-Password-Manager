from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import json
from editusermanagement import UserWindow_EditMode

# --- CODE COMPLETED

QUESTION_FONT = ('calibri', 15, 'normal')
ANSWER_FONT = ('calibri',13,'normal')

class SecurityCheck:
    def __init__(self, mode: str) -> None:
        ''' Select Mode Upon Calling: (C)heck or (S)ave, save will also work as update'''
        self.security_mode = mode

        # --- Setting Main Window
        self.mainwindow = Tk()
        self.mainwindow.title("Who Are You?")
        self.mainwindow.geometry('664x515')
        self.mainwindow.config(bg='white', padx=40, pady=20)
        self.initial_loading()
        self.mainwindow.resizable(False, False)
        self.mainwindow.mainloop()

    def initial_loading(self):
        # --- Logo Placement
        self.mainicon = PhotoImage(master=self.mainwindow, file='resources/security_query_icon.png')
        icon_canvas = Canvas(self.mainwindow, width=88, height=100, bg='white', highlightthickness=0, border=0)
        icon_canvas.create_image(44,50, image=self.mainicon)
        icon_canvas.grid(column=0, row=0, pady=20)

        # --- Label Placement
        main_heading = Label(self.mainwindow, text="Let's Answer Some Security Questions!", font=('calibri', 20, 'bold'), bg='white')
        main_heading.grid(column=1, row=0, padx=40)

        # --- Question Labels Placement
        question_label1 = Label(self.mainwindow, text="Q1. What's the name of your hometown?", font=QUESTION_FONT, bg='white')
        question_label1.grid(column=0, row=3, columnspan=2, pady=5, sticky=W)

        question_label2 = Label(self.mainwindow, text="Q2. What's the name of your first pet?", font=QUESTION_FONT, bg='white')
        question_label2.grid(column=0, row=5, columnspan=2, pady=5, sticky=W)

        question_label3 = Label(self.mainwindow, text="Q3. What's your childhood name?", font=QUESTION_FONT, bg='white')
        question_label3.grid(column=0, row=7, columnspan=2, pady=5, sticky=W)

        # --- Entry Box Placement
        self.answer1_entry = ttk.Entry(self.mainwindow, font=ANSWER_FONT, width=63)
        self.answer1_entry.focus_force()
        self.answer1_entry.grid(column=0, row=4, ipady=6, columnspan=2, sticky=W)

        self.answer2_entry = ttk.Entry(self.mainwindow, font=ANSWER_FONT, width=63)
        self.answer2_entry.grid(column=0, row=6, ipady=6, columnspan=2, sticky=W)

        self.answer3_entry = ttk.Entry(self.mainwindow, font=ANSWER_FONT, width=63)
        self.answer3_entry.grid(column=0, row=8, ipady=6, columnspan=2, sticky=W)

        # --- Button Placement
        action_button = Button(self.mainwindow, font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15)
        if self.security_mode == "C":
            action_button.config(text="Check", command=self.check_answer)
        if self.security_mode == "S":
            action_button.config(text="Save", command=self.save_data)
        action_button.grid(column=1, row=9,padx=40, pady=40, sticky=E)

    def check_answer(self):
        '''Check whether the answers are correct of not'''
        correct_answer_count = 0
        get_answers = self.fetch_data()
        answer1 = (self.answer1_entry.get()).lower()
        answer1_state = "Incorrect"
        answer2 = (self.answer2_entry.get()).lower()
        answer2_state = "Incorrect"
        answer3 = (self.answer3_entry.get()).lower()
        answer3_state = "Incorrect"
        
        if get_answers['answer1'] == answer1:
            correct_answer_count += 1
            answer1_state = "Correct"
        if get_answers['answer2'] == answer2:
            correct_answer_count += 1
            answer2_state = "Correct"
        if get_answers['answer3'] == answer3:
            correct_answer_count += 1
            answer3_state = "Correct"
        if correct_answer_count == 3:
            self.mainwindow.destroy()
            UserWindow_EditMode()
        else:
            messagebox.showinfo("Notice", f"{correct_answer_count} out of 3 questions correct. Please try again!\nQuestion1: {answer1_state}\nQuestion2: {answer2_state}\nQuestion3: {answer3_state}")

    def fetch_data(self) -> dict:
        '''Fetches login data from data file and return as a dict'''
        with open(file='data_saved/saved_info.json', mode='r') as file:
            fetch_data = json.load(file)['Questions']
            self.answers_data = {
                'answer1':fetch_data['Q1'],
                'answer2':fetch_data['Q2'],
                'answer3':fetch_data['Q3']
            }
            return self.answers_data

    def save_data(self):
        '''Save data to a file'''
        answer1 = (self.answer1_entry.get()).lower()
        answer2 = (self.answer2_entry.get()).lower()
        answer3 = (self.answer3_entry.get()).lower()
        
        if answer1 == "" or answer2 == "" or answer3 == "":
            messagebox.showerror("Notice", "The data fields can't be empty.")
        else:
            self.answers_data = {
                'Questions':{
                    'Q1':answer1,
                    'Q2':answer2,
                    'Q3':answer3
                    }
                }
            with open(file='data_saved/saved_info.json', mode='w') as file:
                json.dump(self.answers_data, file)
            if messagebox.showinfo("Success!", "Data Saved, Please Login Again."):
                self.mainwindow.destroy()
