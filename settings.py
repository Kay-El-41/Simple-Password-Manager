from tkinter import *

from securityquestion import SecurityCheck
from editusermanagement import UserWindow_EditMode
from aboutme import AboutMe

# --- CODE COMPLETED --- #

class SettingWindow:
    def __init__(self) -> None:
        self.mainwindow = Tk()
        self.mainwindow.title("Settings")
        self.mainwindow.geometry("300x330")
        self.mainwindow.config(bg='white', padx=20, pady=20)
        self.mainwindow.resizable(False, False)
        
        self.initial_loading()
        self.mainwindow.mainloop()

    def initial_loading(self):
        mainheading = Label(self.mainwindow, text="Settings",bg='white', fg='#00abf7', font=('calibri', 30))
        mainheading.grid(column=0, row=0)

        self.line = horizontal =Frame(self.mainwindow, bg='#00abf7', height=2, width=260)
        self.line = horizontal.grid(column=0, row=1, pady=10)

        reset_security_question_button = Button(self.mainwindow, text="Reset Securtiy Questions",border=0, bg='white', activebackground='white', font=('calibri', 15), command=self.security_questions_change)
        reset_security_question_button.grid(column=0, row=2, sticky=W)

        reset_password_button = Button(self.mainwindow, text="Reset Password",border=0, bg='white', activebackground='white', font=('calibri', 15), command=self.reset_password)
        reset_password_button.grid(column=0, row=3, sticky=W)

        about_me_button = Button(self.mainwindow, text="About Me",border=0, bg='white', activebackground='white', font=('calibri', 15), command=self.aboutme)
        about_me_button.grid(column=0, row=4, sticky=W)

        cancel_button = Button(self.mainwindow,text="Cancel", font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.mainwindow.destroy)
        cancel_button.grid(column=0, row=5, pady=50)

    def security_questions_change(self):
        SecurityCheck('S')

    def reset_password(self):
        UserWindow_EditMode()

    def aboutme(self):
        AboutMe()