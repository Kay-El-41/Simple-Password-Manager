from tkinter import *

import json
from settings import SettingWindow
from addedit import AddEditUI
from view import ViewData
from caesar_encrypt import Cipher


#-- CODE COMPLETED

class MainWindow:
    ''' Display The Main Window Of The Program '''
    def __init__(self) -> None:
        self.cipher = Cipher()
        # --- Setting Main Window
        self.mainwindow = Tk()
        self.mainwindow.geometry("500x830")
        self.mainwindow.title("Welcome Back")
        self.mainwindow.config(bg='white', padx=40, pady=20)
        self.mainwindow.resizable(False, False)
        self.initial_loading()
        self.mainwindow.mainloop()
        
    def initial_loading(self):
        # --- Heading
        mainheading = Label(self.mainwindow, text="Your Websites",bg='white', fg='#00abf7', font=('calibri', 40))
        mainheading.grid(column=0, row=0, sticky=NS, columnspan=3)

        self.line = horizontal =Frame(self.mainwindow, bg='#00abf7', height=2, width=400)
        self.line = horizontal.grid(column=0, row=1, columnspan=3, pady=10)

        # --- Adding List
        self.scroll_bar = Scrollbar(self.mainwindow, activebackground='#00abf7')
        self.scroll_bar.grid(column=0, row=2, columnspan=3)

        self.mylist = Listbox(self.mainwindow,
            border=0, highlightcolor='white',
            highlightthickness=0, font=('calibri', 18),
            activestyle="none",
            yscrollcommand = self.scroll_bar.set, width=35, height=20, bg='white')
        
        self.mylist.grid(pady=20, column=0, columnspan=3, row=2, sticky=W)

        self.scroll_bar.config(command = self.mylist.yview)

        # --- Making Buttons
        self.settings_icon = PhotoImage(master=self.mainwindow, file='resources/settings_icon.png')
        settings_button = Button(self.mainwindow,image=self.settings_icon, activeforeground='white', border=0, bg='#00abf7', activebackground='#00a3f6', width=33, height=33, command=self.setting_start)
        settings_button.grid(column=0, row=3)

        view_button = Button(self.mainwindow,text="View", font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.view_data)
        view_button.grid(column=1, row=3)

        add_new_button = Button(self.mainwindow,text="Add New+", font=('calibri',15,'normal'), bg='#00abf7',fg='white', activeforeground='white', border=0, activebackground='#00a3f6', width=15, command=self.add_new_data)
        add_new_button.grid(column=2, row=3)

        self.refresh_list()


    def refresh_list(self):
        ''' Refresh The List '''
        self.mylist.delete(0, END)
        with open(file="data_saved/main.json") as file:
            data_list = json.load(file)
        for data in data_list:
            if data != "Login":
                self.mylist.insert(END, data)
        self.mainwindow.after(3000, self.refresh_list)

    def setting_start(self):
        '''Open Setting Windows'''
        SettingWindow()

    def add_new_data(self):
        ''' Open Add New Data Window '''
        self.addData = AddEditUI(mode='S')

    def view_data(self):
        ''' Open View Data Window '''
        # Getting Item From A List
        for i in self.mylist.curselection():
            selected_data = self.mylist.get(i)

            # Getting Data From The Data File
            with open(file="data_saved/main.json")as file:
                new_data_list = json.load(file)[selected_data]
                # -- Variables to Transfer To View Window
                name = selected_data
                website = new_data_list['website']
                username = new_data_list['user']
                password = new_data_list['password']
                
            password_decrypted = self.cipher.caesar_cipher(forwhat=name, text=password, action='D')
            self.newView = ViewData(name, website, username, password_decrypted)
