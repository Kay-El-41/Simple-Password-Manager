from tkinter import *
# --- CODE COMPLETED --- #

BODY_TEXT_FONT =('calibri', 15, 'normal')
CONTACT_TEXT_FONT = ('calibri', 13, 'normal')


class AboutMe:
    def __init__(self) -> None:
        # --- Setting Main Window
        self.mainwindow = Tk()
        self.mainwindow.geometry("450x500")
        self.mainwindow.title("About Me")
        self.mainwindow.config(bg='white',padx=40, pady=35)
        self.mainwindow.resizable(False, False)

        # --- Setting Main Heading
        label = Label(self.mainwindow, text="About Me", font=('calibri', 30, 'normal'), bg='white')
        label.grid(column=0, row=0, sticky=NS)

        quicktext = Label(self.mainwindow, text="Developed with love by Kayel", bg='white', font=('calibri', 18, 'normal'))
        quicktext.grid(column=0, row=1, sticky=NS)

        # --- Setting Body Texts
        body_1 = Label(self.mainwindow, text='The data and passwords are stored locally \non your computer.', bg='white', font=BODY_TEXT_FONT, justify='left')
        body_1.grid(column=0, row=2, sticky=W, pady=20)

        body_2 = Label(self.mainwindow, text='Do not worry. All data stored are encrypted \nfor your security.', bg='white', font=BODY_TEXT_FONT, justify='left')
        body_2.grid(column=0, row=3, sticky=W)

        body_3 = Label(self.mainwindow, text='Please keep in mind that once the app is \nuninstalled, all data stored will be deleted', bg='white', font=BODY_TEXT_FONT, justify='left')
        body_3.grid(column=0, row=4, sticky=W, pady=20)

        # --- Contact Me
        contact_label = Label(self.mainwindow, text='Contact Me Via', bg='white', font=BODY_TEXT_FONT, justify='left')
        contact_label.grid(column=0, row=5, sticky=SE)

        contact_mail = Label(self.mainwindow, text='Mail: khantlin.work@gmail.com', bg='white', font=CONTACT_TEXT_FONT, justify='left')
        contact_mail.grid(column=0, row=6, sticky=SE)

        contact_twitter = Label(self.mainwindow, text='Twitter: twitter.com/KayEL41', bg='white', font=CONTACT_TEXT_FONT, justify='left')
        contact_twitter.grid(column=0, row=7, sticky=SE)
        self.mainwindow.mainloop()
