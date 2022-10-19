from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import json
from caesar_encrypt import Cipher

# --- CODE COMPLETED

class UserWindow_EditMode:
    ''' Open Edit User Window '''
    def __init__(self) -> None:
        # --- Setting Cipher
        self.caesar = Cipher()

        # --- variables Loading
        with open(file='data_saved/main.json') as file:
            my_data = json.load(file)['Login']
        self.data_username = my_data['user']
        self.data_password = my_data['password']
        self.data_password = self.caesar.caesar_cipher(forwhat='Login',text=self.data_password,action='D')

        
        # --- Setting Main Window
        self.mainwindow = Tk()
        self.mainwindow.title("Add New User")
        self.mainwindow.config(bg="white", padx=40, pady=20)
        self.mainwindow.geometry("750x450")
        self.initial_loading()
        self.mainwindow.resizable(False, False)
        self.mainwindow.mainloop()

    def initial_loading(self):
        # --- Main Label
        mainheading = Label(self.mainwindow, text="Tell Me About Youself...", bg='white', fg='#00abf7', font=('calibri', 30))
        mainheading.grid(column=0, row=0, columnspan=4, sticky=W, pady=5)
        horizontal =Frame(self.mainwindow, bg='#00abf7', height=2, width=670)
        horizontal.grid(column=0, row=1, columnspan=4, sticky=W,  pady=5)

        # --- Data Labels
        username_text= Label(self.mainwindow, text="Username", bg='white', font=('calibri',15,'normal'))
        username_text.grid(column=1, row=2, sticky='w', columnspan=2)

        master_password_text= Label(self.mainwindow, text="Master Password", bg='white', font=('calibri',15,'normal'))
        master_password_text.grid(column=1, row=4, sticky='w', columnspan=2)

        again_master_password_text= Label(self.mainwindow, text="Type Master Password Again", bg='white', font=('calibri',15,'normal'))
        again_master_password_text.grid(column=1, row=6, sticky='w', columnspan=2)

        # --- Entry Datas
        self.username_entry = ttk.Entry(self.mainwindow, font=('calibri',15,'normal'), width=40)
        self.username_entry.insert(0, self.data_username)
        self.username_entry.grid(column=1, row=3, sticky=W, ipady=6, columnspan=2)
        self.username_entry.focus_force()

        self.password_entry = ttk.Entry(self.mainwindow, font=('calibri',15,'normal'),show='*', width=40)
        self.password_entry.insert(0, self.data_password)
        self.password_entry.grid(column=1, row=5, sticky=W, ipady=6, columnspan=2)

        self.confirm_password_entry = ttk.Entry(self.mainwindow, font=('calibri',15,'normal'),show='*', width=40)
        self.confirm_password_entry.insert(0, self.data_password)
        self.confirm_password_entry.grid(column=1, row=7, sticky=W, ipady=6, columnspan=2)

        # --- Password Button
        self.hide_password_icon = PhotoImage(master=self.mainwindow, file='resources/hide_password_eye_icon.png')
        self.show_password_icon = PhotoImage(master=self.mainwindow, file='resources/show_password_eye_icon.png')

        self.show_password_button = Button(self.mainwindow, image=self.show_password_icon, font=('calibri',12,'normal'), bg='white', border=0, activebackground='white', command=self.show_or_hide_password)
        self.show_password_button.grid(column=3, row=5, sticky=E)

        self.confirm_show_password_button = Button(self.mainwindow, image=self.show_password_icon, font=('calibri',12,'normal'), bg='white', border=0, activebackground='white', command=self.confirm_show_or_hide_password)
        self.confirm_show_password_button.grid(column=3, row=7, sticky=E)

        # --- Save Button
        login_button = Button(self.mainwindow, text='Save', font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.check_data)
        login_button.grid(column=2, row=8,sticky=E, pady=30)

        # --- Icon & Text
        self.mainicon = PhotoImage(master=self.mainwindow, file='resources/add_user_lock_icon.png' )
        logo_canvas = Canvas(self.mainwindow, width=190, height=250, bg="white", highlightthickness=0)
        logo_canvas.create_image(95, 130, image=self.mainicon)
        logo_canvas.grid(column=0, row=2, rowspan=6, sticky=W, padx=25)

    def show_or_hide_password(self):
        ''' Show ot Hide Password Entry As *'''
        if self.password_entry.cget('show') == '':
            self.password_entry.config(show='*')
            self.show_password_button.config(image=self.show_password_icon)
        else:
            self.password_entry.config(show='')
            self.show_password_button.config(image=self.hide_password_icon)

    def confirm_show_or_hide_password(self):
        ''' Show ot Hide Password Entry As *'''
        if self.confirm_password_entry.cget('show') == '':
            self.confirm_password_entry.config(show='*')
            self.confirm_show_password_button.config(image=self.show_password_icon)
        else:
            self.confirm_password_entry.config(show='')
            self.confirm_show_password_button.config(image=self.hide_password_icon)

    def check_data(self):
        # --- Password Check First
        if messagebox.askokcancel("Notice", "Are you sure to save?"):
            if self.password_entry.get() == self.confirm_password_entry.get():
                self.save_login_data()
            else:
                messagebox.showerror("Notice", "Two passwords are not match. Please Try Again")

    def save_login_data(self):
        password_to_save = self.password_entry.get()
        password_encrypted = self.caesar.caesar_cipher(text=password_to_save, forwhat='Login', action='E')

        self.login_data = {
            "Login": {
                "user": self.username_entry.get(),
                "password": password_encrypted
            }
        }

        # -- Delete Existing Data & Update Login Data
        self.caesar.cipher_add_key("Login")
        
        with open(file='data_saved/main.json') as file:
            new_data = json.load(file)
            new_data.pop("Login")
            new_data.update(self.login_data)
        with open(file='data_saved/main.json', mode='w') as file:
            json.dump(new_data, file, indent=4)

        # --- Delete Key Data
        # with open(file='data_saved/cipher_cache.json') as file2:
        #     data2 = json.load(file2)
        #     data2.pop("Login")
        # with open(file='data_saved/cipher_cache.json', mode='w') as file2:
        #     json.dump(data2, file2, indent=4)

        # --- Add New Key Data
        
        if messagebox.showinfo("Succeed", "Update Complete!"):
            self.mainwindow.destroy()