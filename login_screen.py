from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from caesar_encrypt import Cipher
from usermanagement import UserWindow_AddMode
from mainwindow import MainWindow
from aboutme import AboutMe
from securityquestion import SecurityCheck

import json

# -- NEED CODE IMPROVEMENT FOR ADD NEW USER CODE LINE 110
class LoginScreen:
    def __init__(self) -> None:
        # --- Setting Main Window And Key Cipher
        self.cipher = Cipher()
        self.mainwindow = Tk()
        self.mainwindow.geometry("786x420")
        self.mainwindow.title("Please Log In First")
        self.mainwindow.config(bg='white', pady=25)
        self.loginscreen_initial_loading()
        self.mainwindow.resizable(False, False)
        self.mainwindow.mainloop()

    def loginscreen_initial_loading(self):
        # --- Used self. for widgets that needs to change later
        # --- Initialize icons
        self.locked_icon = PhotoImage(master=self.mainwindow, file='resources/locked_icon.png')
        self.hide_password_icon = PhotoImage(master=self.mainwindow, file='resources/hide_password_eye_icon.png')
        self.show_password_icon = PhotoImage(master=self.mainwindow, file='resources/show_password_eye_icon.png')

        # --- logo placement
        logo_canvas = Canvas(width=190, height=255, bg="white", highlightthickness=0)
        logo_canvas.create_image(95, 130, image=self.locked_icon)
        logo_canvas.grid(column=0, row=1, rowspan=3, padx=25)

        # --- Label placement
        mainheading = Label(self.mainwindow, text="A PASSWORDS MANAGER", bg='white', font=('calibri',37,'normal'))
        mainheading.grid(column=1, columnspan=3, row=1)

        username_text= Label(self.mainwindow, text="Username", bg='white', font=('calibri',15,'normal'))
        username_text.grid(column=1, row=2, sticky=W)

        master_password_text= Label(self.mainwindow, text="Master Password", bg='white', font=('calibri',15,'normal'))
        master_password_text.grid(column=1, row=3, sticky=W)

        # --- Text Entry placement
        self.username_entry = ttk.Entry(font=('calibri',15,'normal'), width=33)
        self.username_entry.grid(column=2, row=2, ipady=6)

        self.password_entry = ttk.Entry(font=('calibri',15,'normal'),show='*', width=33)
        self.password_entry.grid(column=2, row=3, ipady=6)

        # --- Text Button placement
        about_me_button = Button(self.mainwindow, text='About Me', font=('calibri',12,'normal'), bg='white', border=0, activebackground='white', command=self.about_me)
        about_me_button.grid(column=2, row=0, columnspan=2, sticky='e')

        forget_password_button = Button(self.mainwindow, text='Forget Password', font=('calibri',12,'normal'), bg='white', border=0, activebackground='white', command=self.security_check)
        forget_password_button.grid(column=2, row=5)

        # --- Function Buttons
        login_button = Button(self.mainwindow, text='Login', font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.loginnow)
        login_button.grid(column=2, row=4, pady=10)

        self.show_password_button = Button(self.mainwindow, image=self.show_password_icon, bg='white', border=0, activebackground='white', command=self.show_or_hide_password)
        self.show_password_button.grid(column=3, row=3, sticky=E)

    def security_check(self):
        ''' Open security check window'''
        security_check = SecurityCheck(mode='C')

    def about_me(self):
        ''' Open about me window'''
        about_me_window = AboutMe()

    def show_or_hide_password(self):
        ''' Show ot Hide Password Entry As *'''
        if self.password_entry.cget('show') == '':
            self.password_entry.config(show='*')
            self.show_password_button.config(image=self.show_password_icon)
        else:
            self.password_entry.config(show='')
            self.show_password_button.config(image=self.hide_password_icon)

    def loginnow(self):
        ''' Check whether data entered and data exist are matched.'''
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        received_login_info = self.fetch_data()
        try:
            if entered_username == received_login_info['user'] and entered_password == received_login_info['password']:
                self.mainwindow.destroy()
                MainWindow()
            else:
                messagebox.showinfo("Notice", "Incorrect Data, Please Try Again")
        except TypeError:
            pass
               
    def fetch_data(self) -> dict:
        '''Fetches login data from data file and return as a dict'''
        try:
            with open(file='data_saved/main.json', mode='r') as file:
                fetch_data = json.load(file)['Login']
                self.login_data = {
                    'user':fetch_data['user'],
                    'password':self.cipher.caesar_cipher('Login', fetch_data['password'], 'D')
                }
                return self.login_data

        except FileNotFoundError:
            new_user = messagebox.askokcancel("Notice", "No data are found, do you want to register a new one?")
            if new_user:
                self.addmode = UserWindow_AddMode()
            else:
                self.mainwindow.quit()