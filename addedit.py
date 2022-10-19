from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from caesar_encrypt import Cipher

import json
import randompass as RP
import pyperclip

HEADING_FONT = ('calibri', 18, 'normal')
FONT = ('calibri', 15, 'normal')


class AddEditUI:
    ''' Require mode, (S)ave New Data, (U)pdate New Data
    Required name to edit'''
    def __init__(self, mode='none', to_edit_name='none') -> None:

        self.mode = mode
        self.website_to_edit = to_edit_name
        self.cipher = Cipher()
    
        # -- Main Window
        self.mainwindow = Tk()
        self.mainwindow.title("Info")
        self.mainwindow.config(bg='white', padx=40)
        self.mainwindow.geometry("550x620")
        self.initial_loading()
        self.mainwindow.resizable(False, False)
        self.mainwindow.mainloop()

    def initial_loading(self):
        mainheading = Label(self.mainwindow, text="You're Saving As..", bg='white', fg='#00abf7', font=('calibri', 35))
        mainheading.grid(column=0, row=0, columnspan=2, sticky=W, pady=20)

        # --- Line
        horizontal = Frame(self.mainwindow, bg='#00abf7', height=2, width=480)
        horizontal.grid(column=0, row=1, columnspan=5, sticky=W)

        # --- Main Labels
        name_label = Label(self.mainwindow, text="Name", bg='white', font=HEADING_FONT)
        name_label.grid(column=0, row=2, sticky=W, columnspan=2, pady=4)

        website_name_label = Label(self.mainwindow, text="Website", bg='white', font=HEADING_FONT)
        website_name_label.grid(column=0, row=4, sticky=W, columnspan=2, pady=4)

        login_with_label = Label(self.mainwindow, text="Login With", bg='white', font=HEADING_FONT)
        login_with_label.grid(column=0, row=6, sticky=W, columnspan=2, pady=4)

        password_label = Label(self.mainwindow, text="Password", bg='white', font=HEADING_FONT)
        password_label.grid(column=0, row=8, sticky=W, columnspan=2, pady=4)

        # --- Data Labels
        self.name_data_entry = ttk.Entry(self.mainwindow, font=FONT, width=40)
        self.name_data_entry.grid(column=0, row=3, sticky=W, columnspan=2, ipady=6)
        self.name_data_entry.focus_force()

        self.website_link_data_entry = ttk.Entry(self.mainwindow, font=FONT, width=40)
        self.website_link_data_entry.grid(column=0, row=5, sticky=W, columnspan=2, ipady=6)

        self.login_with_data_entry = ttk.Entry(self.mainwindow, font=FONT, width=40)
        self.login_with_data_entry.grid(column=0, row=7, sticky=W, columnspan=2, ipady=6)

        self.password_data_entry = ttk.Entry(self.mainwindow, show='*', font=FONT, width=40)
        self.password_data_entry.grid(column=0, row=9, sticky=W, columnspan=2, ipady=6, padx=5)

        # --- Passoword Show Hide Button
        self.hide_password_icon = PhotoImage(master=self.mainwindow, file='resources/hide_password_eye_icon.png')
        self.show_password_icon = PhotoImage(master=self.mainwindow, file='resources/show_password_eye_icon.png')

        self.show_password_button = Button(self.mainwindow, image=self.show_password_icon, bg='white', border=0, activebackground='white', command=self.show_or_hide_password)
        self.show_password_button.grid(column=3, row=9, sticky=E, padx=5)

        self.random_password_icon = PhotoImage(master=self.mainwindow, file='resources/got_idea_icon.png')
        self.random_password_button = Button(self.mainwindow, image=self.random_password_icon, bg='white', border=0, activebackground='white', command=self.generate_password)
        self.random_password_button.grid(column=2, row=9, sticky=E, pady=10)
        
        self.copy_icon = PhotoImage(master=self.mainwindow, file='resources/copy_clip_iocn.png')
        self.copy_website_button = Button(self.mainwindow, image=self.copy_icon, bg='white', border=0, activebackground='white', command=self.copy_website_to_clipboard)
        self.copy_website_button.grid(column=3, row=5, sticky=E, padx=5)

        self.copy_username_button = Button(self.mainwindow, image=self.copy_icon, bg='white', border=0, activebackground='white', command=self.copy_username_to_clipboard)
        self.copy_username_button.grid(column=3, row=7, sticky=E, padx=5)

        self.copy_password_button = Button(self.mainwindow, image=self.copy_icon, bg='white', border=0, activebackground='white', command=self.copy_password_to_clipboard)
        self.copy_password_button.grid(column=4, row=9, sticky=E)

        # --- Function Button

        function_button = Button(self.mainwindow, text='Save', font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.function_clicked)
        function_button.grid(column=0, row=10, pady=100)

        cancel_button = Button(self.mainwindow, text='Cancel', font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.cancel_clicked)
        cancel_button.grid(column=1, row=10, pady=100, sticky=NS)

        # --- Preparing For Save Mode
        if self.mode == 'S':
            function_button.config(text="Save")

        # --- Preparing For Edit Mode
        if self.mode == 'U':
            function_button.config(text="Update")
            with open(file="data_saved/main.json")as file:
                new_data_list = json.load(file)[self.website_to_edit]
                # -- Variables to Transfer To View Window
                name = self.website_to_edit
                website = new_data_list['website']
                username = new_data_list['user']
                password = new_data_list['password']
                password_decryped = self.cipher.caesar_cipher(forwhat=self.website_to_edit, text=password, action='D')

            self.name_data_entry.insert(0, name)
            self.website_link_data_entry.insert(0, website)
            self.login_with_data_entry.insert(0, username)
            self.password_data_entry.insert(0, password_decryped)

    def show_or_hide_password(self):
        ''' Show ot Hide Password Entry As *'''
        if self.password_data_entry.cget('show') == '':
            self.password_data_entry.config(show='*')
            self.show_password_button.config(image=self.show_password_icon)
        else:
            self.password_data_entry.config(show='')
            self.show_password_button.config(image=self.hide_password_icon)

    def copy_website_to_clipboard(self):
        pyperclip.copy(self.website_link_data_entry.get())

    def copy_username_to_clipboard(self):
        pyperclip.copy(self.login_with_data_entry.get())

    def copy_password_to_clipboard(self):
        pyperclip.copy(self.password_data_entry.get())

    def generate_password(self) -> str:
        '''Generate A String Of Random Password'''
        self.password_generator = RP.RandomPassword()
        self.password_data_entry.delete(0, END)
        self.password_data_entry.insert(0, self.password_generator.generate_random_password())

    def cancel_clicked(self):
        if messagebox.askokcancel("Notice", "The data entered will be lost. Are you sure?"):
            self.mainwindow.destroy()

    def function_clicked(self):
        name = self.name_data_entry.get()
        website = self.website_link_data_entry.get()
        user = self.login_with_data_entry.get()
        password = self.password_data_entry.get()
        password = self.cipher.caesar_cipher(text=password, forwhat='Login', action='E')

        self.new_data = {
            name: {
                "website": website,
                "user": user,
                "password": password
            }
        }
        # -- Saving A New Data Set
        if self.mode == 'S':
            self.cipher.cipher_add_key(name)
            with open(file='data_saved/main.json') as file:
                data = json.load(file) # Load Data
                data.update(self.new_data) # Update Data
            with open(file='data_saved/main.json', mode='w') as file2:
                json.dump(data, file2, indent=4)

        # -- Update Exiting Data Set
        if self.mode == 'U':

            self.cipher.cipher_add_key(name)
            with open(file='data_saved/main.json') as file:
                data = json.load(file) # Load Data
                data.pop(self.website_to_edit)
                data.update(self.new_data) # Update Data
            with open(file='data_saved/main.json', mode='w') as file:
                json.dump(data, file, indent=4) # Save Updated Data
            
            # with open(file='data_saved/cipher_cache.json') as file2:
            #     data2 = json.load(file2)
            #     data2.pop(self.website_to_edit)
            #     data2.update(self.new_data)
            # with open(file='data_saved/cipher_cache.json', mode='w') as file2:
            #     json.dump(data2, file2, indent=4)
        
        if messagebox.showinfo("Success!", "Saving data complete."):
            self.mainwindow.destroy()

