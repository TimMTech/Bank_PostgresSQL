from tkinter import Label, Frame, Entry, Button, messagebox
from tkinter import IntVar, Checkbutton, CENTER, EXCEPTION
from tkinter import ttk
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT, COMBOBOX_FONT
import tkinter as tk
import psycopg2


class Register(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.available = 'false'
        try:
            self.conn = psycopg2.connect(
                database='MVCBANK',
                user='postgres',
                password='Redcross500')
        except EXCEPTION as es:
            messagebox.showerror("Error", f'Error due to {str(es)}', parent=self.root)

        self.root.title("Register Page")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ===BG Image=====
        self.bg = ImageTk.PhotoImage(file="Images2/background.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===Left Image=====
        self.pic = Image.open("Images2/bgimage.png")
        self.pic = self.pic.resize((300, 400))
        self.left = ImageTk.PhotoImage(self.pic)
        Label(self.root, image=self.left).place(x=0, y=0, width=400, height=700)
        left_txt = Label(self.root, text="BANKING APPLICATION", font=LARGE_FONT)
        left_txt.place(x=75, y=500)
        left_txt_author = Label(self.root, text="Beta by Tim Mukhamedov", font=MEDIUM_FONT)
        left_txt_author.place(x=110, y=550)

        # ===Register Frame=====
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=500)

        Label(frame1, text="REGISTER HERE", font=LARGE_FONT, bg='white', fg='green').place(x=50, y=0)

        # ----------------------Row 1
        Label(frame1, text="First Name", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=50)
        self.txt_firstname_entry = Entry(frame1, textvariable=self.master.data["firstname"], font=MEDIUM_FONT,
                                         bg='lightgray')
        self.txt_firstname_entry.place(x=50, y=80, width=200)

        Label(frame1, text="Last Name", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=50)
        self.txt_lastname_entry = Entry(frame1, textvariable=self.master.data["lastname"], font=MEDIUM_FONT,
                                        bg='lightgray')
        self.txt_lastname_entry.place(x=400, y=80, width=200)

        # ----------------------Row 2

        Label(frame1, text="Contact No", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=120)
        self.txt_contact_entry = Entry(frame1, textvariable=self.master.data["contact"], font=MEDIUM_FONT,
                                       bg='lightgray')
        self.txt_contact_entry.place(x=50, y=150, width=200)

        Label(frame1, text="Email", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=120)
        self.txt_email_entry = Entry(frame1, textvariable=self.master.data["email"], font=MEDIUM_FONT, bg='lightgray')
        self.txt_email_entry.place(x=400, y=150, width=200)

        # ----------------------Row 3

        Label(frame1, text="Security Question", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=190)

        self.cmb_quest = ttk.Combobox(frame1, textvariable=self.master.data["question"], font=COMBOBOX_FONT,
                                      state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name",
                                    "Your Birth Place",
                                    "Your Best Friend's Name")
        self.cmb_quest.place(x=50, y=220, width=200)
        self.cmb_quest.current(0)

        Label(frame1, text="Answer", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=190)
        self.txt_answer_entry = Entry(frame1, textvariable=self.master.data["answer"], font=MEDIUM_FONT, bg='lightgray')
        self.txt_answer_entry.place(x=400, y=220, width=200)

        # ---------------------Row 4

        Label(frame1, text="Password", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=260)
        self.txt_password_entry = Entry(frame1, textvariable=self.master.data["password"], font=MEDIUM_FONT,
                                        bg='lightgray',
                                        show='*')
        self.txt_password_entry.place(x=50, y=290, width=200)

        Label(frame1, text="Confirm Password", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=260)
        self.txt_confirm_password_entry = Entry(frame1, textvariable=self.master.data["confirmpassword"],
                                                font=MEDIUM_FONT,
                                                bg='lightgray', show='*')
        self.txt_confirm_password_entry.place(x=400, y=290, width=200)

        # ----------Terms----------
        self.var_check = IntVar()
        Checkbutton(frame1, text="I Agree to Terms & Conditions", variable=self.var_check, onvalue=1, offvalue=0,
                    font=MEDIUM_FONT,
                    bg='white').place(x=50, y=360)

        Button(frame1, text="Register", bd=0, cursor='hand2',
               command=lambda: self.register()).place(x=50, y=430, width=180)
        Button(frame1, text="Sign In", bd=0, cursor='hand2',
               command=lambda: master.switch_frame("LoginPage")).place(x=400, y=430, width=180)

    def register(self):
        firstname = self.master.data["firstname"].get()
        lastname = self.master.data["lastname"].get()
        contact = self.master.data["contact"].get()
        email = self.master.data["email"].get()
        question = self.master.data["question"].get()
        answer = self.master.data["answer"].get()
        password = self.master.data["password"].get()
        confirm_pass = self.master.data["confirmpassword"].get()
        balance = '0'
        fields = [firstname, lastname, contact,
                  email, question, answer,
                  password, confirm_pass]
        for entries in fields:
            if entries == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
                return
            if question == "Select":
                messagebox.showerror("Error", "Must Select a Question", parent=self.root)
                return
            if password != confirm_pass:
                messagebox.showerror("Error", "Password Does Not Match", parent=self.root)
                return
            if self.var_check.get() == 0:
                messagebox.showerror("Error", "Please Agree to Terms & Conditions", parent=self.root)
                return
        try:
            my_cursor = self.conn.cursor()
            check_script = 'SELECT * FROM accounts WHERE email=%s'
            check_var = email
            my_cursor.execute(check_script, (check_var,))
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "Account Exists", parent=self.root)
                return
            insert_script = 'INSERT INTO accounts (firstname, lastname, phone, email, question, answer, pword, ' \
                            'balance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) '
            insert_values = (firstname, lastname, contact, email, question, answer, password, balance)
            my_cursor.execute(insert_script, insert_values)
            self.conn.commit()
            self.conn.close()
            self.refresh()
            messagebox.showinfo("Success", "Account Created!", parent=self.root)

        except EXCEPTION as es:
            messagebox.showerror("Error", f'Error due to {str(es)}', parent=self.root)

    def refresh(self):
        self.txt_firstname_entry.delete(0, "end")
        self.txt_lastname_entry.delete(0, "end")
        self.txt_contact_entry.delete(0, "end")
        self.txt_email_entry.delete(0, "end")
        self.cmb_quest.current(0)
        self.txt_answer_entry.delete(0, "end")
        self.txt_password_entry.delete(0, "end")
        self.txt_confirm_password_entry.delete(0, "end")
        self.var_check.set(0)
