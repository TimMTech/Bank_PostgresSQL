from tkinter import Frame, Label, Button
from tkinter import messagebox, EXCEPTION
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import psycopg2


class AccountDash(tk.Frame):
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

        self.root.title("Home Page")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ===BG Image=====
        self.bg = ImageTk.PhotoImage(file="Images2/background.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ======Account Dash Frame=========
        frame3 = Frame(self.root, bg='white')
        frame3.place(x=480, y=100, width=700, height=500)

        # ===Left Image=====
        self.pic = Image.open("Images2/bgimage.png")
        self.pic = self.pic.resize((300, 400))
        self.left = ImageTk.PhotoImage(self.pic)
        Label(self.root, image=self.left).place(x=0, y=0, width=400, height=700)
        left_txt = Label(self.root, text="BANKING APPLICATION", font=LARGE_FONT)
        left_txt.place(x=75, y=500)
        left_txt_author = Label(self.root, text="Beta by Tim Mukhamedov", font=MEDIUM_FONT)
        left_txt_author.place(x=110, y=550)

        # ========Right Panel Image============
        self.img = Image.open("Images2/investment.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=350)

        # ========Title==============
        Label(frame3, text="ACCOUNT DASHBOARD", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # -----------------------Row 1
        Label(frame3, text="Choose What's Right For You", font=MEDIUM_FONT, bg='white', fg='green').place(x=80, y=80)

        # =========Options==============
        Button(frame3, text="Personal Details", bd=0, cursor='hand2',
               command=lambda: master.switch_frame("PersonalPage")).place(x=60, y=160, width=180)
        Button(frame3, text="Deposit", bd=0, cursor='hand2',
               command=lambda: master.switch_frame("DepositPage")).place(x=60, y=240, width=180)
        Button(frame3, text="Withdraw", bd=0, cursor='hand2',
               command=lambda: master.switch_frame("WithdrawPage")).place(x=60, y=320, width=180)
        Button(frame3, text="Sign Out", bd=0, cursor='hand2',
               command=lambda: self.successLogout()).place(x=60, y=400, width=180)

    def successLogout(self):
        messagebox.showinfo("Success", "Logged Out Successfully", parent=self.root)
        self.master.switch_frame("LoginPage")
