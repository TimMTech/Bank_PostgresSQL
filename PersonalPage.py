from tkinter import Frame, Label, Button, messagebox, EXCEPTION
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import psycopg2


class PersonalDetails(tk.Frame):

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

        self.root.title("Personal Details")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ======Personal Frame==========
        frame4 = Frame(self.root, bg='white')
        frame4.place(x=480, y=100, width=700, height=500)

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

        # DATA HANDLER
        email = self.master.data["email"].get()
        my_cursor = self.conn.cursor()
        active_script = 'SELECT firstname, lastname, phone, email FROM accounts WHERE email=%s'
        retrieve_var = email
        my_cursor.execute(active_script, (retrieve_var,))
        data = my_cursor.fetchone()
        firstname = data[0]
        lastname = data[1]
        phone = data[2]
        email = data[3]

        # =============Title===============
        Label(frame4, text="PERSONAL INFORMATION", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # -------------------------------Row 1
        Label(frame4, text="First Name", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=30)
        Label(frame4, text=firstname, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=50)

        # -------------------------------Row 2
        Label(frame4, text="Last Name", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=130)
        Label(frame4, text=lastname, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=150)

        # -------------------------------Row 3
        Label(frame4, text="Contact Number", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=230)
        Label(frame4, text=phone, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=250)

        # -------------------------------Row 4
        Label(frame4, text="Email", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=330)
        Label(frame4, text=email, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=350)

        # ===========Options===============
        Button(frame4, text="Previous", bd=0, cursor='hand2',
               command=lambda: self.master.switch_frame("AccountPage")).place(x=400, y=430, width=180)
