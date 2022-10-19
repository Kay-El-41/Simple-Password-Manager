from tkinter import *
from tkinter import messagebox
from addedit import AddEditUI

import json
import pyperclip
#--- MAY REQUIRE EDITING IN GO_EDIT FUNCTION LINE 100

HEADING_FONT = ('calibri', 20, 'bold')
FONT = ('calibri', 18, 'normal')

class ViewData():
    ''' Required Name, websiteName, UserName, Password'''
    def __init__(self, name, websitename, username, password) -> None:
        # --- Variables
        self.password_mode = "hidden"
        self.data_name = name
        self.data_website = websitename
        self.data_username = username
        self.data_password = password

        # --- Setting Main Window
        self.mainwindow = Tk()
        self.mainwindow.geometry("530x570")
        self.mainwindow.config(bg='white', padx=40, pady=20)
        self.mainwindow.title("Info")
        self.mainwindow.resizable(False, False)
        self.initial_loading()
        self.mainwindow.mainloop()

    def initial_loading(self):
        # --- Big Heading
        mainheading = Label(self.mainwindow, text="You Saved As", bg='white', fg='#00abf7', font=('calibri', 40))
        mainheading.grid(column=0, row=0, columnspan=5, sticky=W)

        # --- Line
        horizontal =Frame(self.mainwindow, bg='#00abf7', height=2, width=450)
        horizontal.grid(column=0, row=1, columnspan=5, pady=20)

        # --- Main Labels
        name_label = Label(self.mainwindow, text="Name", bg='white', fg='#00abf7', font=HEADING_FONT)
        name_label.grid(column=0, row=2, sticky=W, columnspan=2)

        website_name_label = Label(self.mainwindow, text="Website", bg='white', fg='#00abf7', font=HEADING_FONT)
        website_name_label.grid(column=0, row=4, sticky=W, columnspan=2)

        login_with_label = Label(self.mainwindow, text="Login With", bg='white', fg='#00abf7', font=HEADING_FONT)
        login_with_label.grid(column=0, row=6, sticky=W, columnspan=2)

        password_label = Label(self.mainwindow, text="Password", bg='white', fg='#00abf7', font=HEADING_FONT)
        password_label.grid(column=0, row=8, sticky=W, columnspan=2)

        # --- Data Labels
        self.name_data_label = Label(self.mainwindow, text=self.data_name, bg='white', font=FONT)
        self.name_data_label.grid(column=0, row=3, sticky=W, columnspan=2)

        self.website_name_data_label = Label(self.mainwindow, text=self.data_website, bg='white', font=FONT)
        self.website_name_data_label.grid(column=0, row=5, sticky=W, columnspan=2)

        self.login_with_data_label = Label(self.mainwindow, text=self.data_username, bg='white', font=FONT)
        self.login_with_data_label.grid(column=0, row=7, sticky=W, columnspan=2)

        self.password_data_label = Label(self.mainwindow, text="********", bg='white', font=FONT)
        self.password_data_label.grid(column=0, row=9, sticky=W, columnspan=2)

        # --- Placing Buttons
        edit_button = Button(self.mainwindow,text="Edit", font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.go_edit)
        edit_button.grid(column=1, row=10,pady=60, padx=40)

        delete_button = Button(self.mainwindow,text="Delete", font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.delete)
        delete_button.grid(column=2, row=10,pady=60, sticky=E)

        # --- Show Hide Password Button
        self.hide_password_icon = PhotoImage(master=self.mainwindow, file='resources/hide_password_eye_icon.png')
        self.show_password_icon = PhotoImage(master=self.mainwindow, file='resources/show_password_eye_icon.png')

        self.show_password_button = Button(self.mainwindow, image=self.show_password_icon, bg='white', border=0, activebackground='white', command=self.show_hide_password)
        self.show_password_button.grid(column=3, row=9, sticky=W)

        # --- Copy Buutton
        self.copy_icon = PhotoImage(master=self.mainwindow, file='resources/copy_clip_iocn.png')

        self.copy_website_button = Button(self.mainwindow, image=self.copy_icon, bg='white', border=0, activebackground='white', command=self.copy_website_to_clipboard)
        self.copy_website_button.grid(column=4, row=5, sticky=E, padx=5)

        self.copy_username_button = Button(self.mainwindow, image=self.copy_icon, bg='white', border=0, activebackground='white', command=self.copy_username_to_clipboard)
        self.copy_username_button.grid(column=4, row=7, sticky=E, padx=5)

        self.copy_password_button = Button(self.mainwindow, image=self.copy_icon, bg='white', border=0, activebackground='white', command=self.copy_password_to_clipboard)
        self.copy_password_button.grid(column=4, row=9, sticky=E, padx=5)

    def copy_website_to_clipboard(self):
        pyperclip.copy(self.data_website)
    def copy_username_to_clipboard(self):
        pyperclip.copy(self.data_username)
    def copy_password_to_clipboard(self):
        pyperclip.copy(self.data_password)

    def show_hide_password(self):
        ''' Show Or Hide Password'''
        if self.password_mode == 'hidden':
            self.password_data_label.config(text=self.data_password)
            self.password_mode = 'show'
        else:
            self.password_data_label.config(text="********")
            self.password_mode = 'hidden'

    def delete(self):
        ''' Delete The Data'''
        if messagebox.askokcancel("Notice", "The data will be lost."):
        # --- Delete Password Data
            with open(file='data_saved/main.json') as file:
                new_data = json.load(file)
                new_data.pop(self.data_name)
            with open(file='data_saved/main.json', mode='w') as file:
                json.dump(new_data, file, indent=4)

            # --- Delete Key Data
            with open(file='data_saved/cipher_cache.json') as file2:
                data2 = json.load(file2)
                data2.pop(self.data_name)
            with open(file='data_saved/cipher_cache.json', mode='w') as file2:
                json.dump(data2, file2, indent=4)
            self.mainwindow.destroy()

    def go_edit(self):
        ''' Open Edit UI InterFace'''
        self.mainwindow.destroy()
        self.editmode = AddEditUI(mode='U', to_edit_name=self.data_name)

# -- TO TEST UNCOMMENT THIS
# new_view = ViewData('Pubg', 'www.test.com', 'User123', 'mypassword')