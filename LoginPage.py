from tkinter import Frame, Label, Entry, Button, messagebox, EXCEPTION
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import psycopg2


class Login(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master

        try:
            self.conn = psycopg2.connect(
                database='MVCBANK',
                user='postgres',
                password='Redcross500')
        except EXCEPTION as es:
            messagebox.showerror("Error", f'Error due to {str(es)}', parent=self.root)

        self.root.title("Login Page")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ===BG Image=====
        self.bg = ImageTk.PhotoImage(file="Images2/background.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ======Login Frame==========
        frame2 = Frame(self.root, bg='white')
        frame2.place(x=480, y=100, width=700, height=500)

        # ===Left Image=====
        self.pic = Image.open("Images2/bgimage.png")
        self.pic = self.pic.resize((300, 400))
        self.left = ImageTk.PhotoImage(self.pic)
        Label(self.root, image=self.left).place(x=0, y=0, width=400, height=700)
        left_txt = Label(self.root, text="BANKING APPLICATION", font=LARGE_FONT)
        left_txt.place(x=75, y=500)
        left_txt_author = Label(self.root, text="Beta by Tim Mukhamedov", font=MEDIUM_FONT)
        left_txt_author.place(x=110, y=550)

        # ======Right Panel Image========
        self.img = Image.open("Images2/loginimage.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=375)

        # ========Title==========
        Label(frame2, text="LOGIN HERE", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # ------------------------Row 1
        Label(frame2, text="EMAIL ADDRESS", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=150)
        self.txt_email_entry = Entry(frame2, textvariable=self.master.data["email"], font=MEDIUM_FONT, bg='lightgray')
        self.txt_email_entry.place(x=50, y=180, width=200)

        # -------------------------Row 2
        Label(frame2, text="Password", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=250)
        self.txt_password_entry = Entry(frame2, textvariable=self.master.data["password"], font=MEDIUM_FONT,
                                        bg='lightgray', show='*')
        self.txt_password_entry.place(x=50, y=280, width=200)

        # ----------Login Success----------------
        Button(frame2, text="Sign In", bd=0, cursor='hand2',
               command=lambda: self.login()).place(x=250, y=430, width=180)
        Button(frame2, text="New Account?", bd=0, cursor='hand2',
               command=lambda: self.newAccount()).place(x=250, y=460, width=180)

    def login(self):
        email = self.master.data["email"].get()
        password = self.master.data["password"].get()
        fields = [email, password]
        for entries in fields:
            if entries == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
                return

        try:
            my_cursor = self.conn.cursor()
            check_script = 'SELECT * FROM accounts WHERE email=%s and pword=%s'
            check_vars = (email, password)
            my_cursor.execute(check_script, check_vars)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
                return
            messagebox.showinfo("Success", "Welcome!", parent=self.root)
            self.master.switch_frame("AccountPage")

        except EXCEPTION as es:
            messagebox.showerror("Error", f'Error due to {str(es)}', parent=self.root)

    def newAccount(self):
        self.refresh()
        self.master.switch_frame("RegisterPage")

    def refresh(self):
        self.txt_email_entry.delete(0, "end")
        self.txt_password_entry.delete(0, "end")
