from tkinter import Frame, Label, Button, Entry, messagebox, EXCEPTION
from decimal import Decimal
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import os


class Withdraw(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.root.title("Withdraw")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ===BG Image=====
        self.bg = ImageTk.PhotoImage(file="Images/background.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ======Login Frame==========
        frame6 = Frame(self.root, bg='white')
        frame6.place(x=480, y=100, width=700, height=500)

        # ===Left Image=====
        self.pic = Image.open("Images/bgimage.png")
        self.pic = self.pic.resize((300, 400))
        self.left = ImageTk.PhotoImage(self.pic)
        Label(self.root, image=self.left).place(x=0, y=0, width=400, height=700)
        left_txt = Label(self.root, text="BANKING APPLICATION", font=LARGE_FONT)
        left_txt.place(x=75, y=500)
        left_txt_author = Label(self.root, text="Beta by Tim Mukhamedov", font=MEDIUM_FONT)
        left_txt_author.place(x=110, y=550)

        # ========Right Panel Image============
        self.img = Image.open("Images/depositimage.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=350)


        # ========Title==============
        Label(frame6, text="Withdraw", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # -----------------------Row 1
        Label(frame6, text="CURRENT BALANCE BELOW", font=MEDIUM_FONT, bg='white', fg='green').place(x=40, y=80)

        # -----------------------Row 2
        Label(frame6, text="Amount", font=MEDIUM_FONT, bg='white', fg='black').place(x=10, y=110)
        self.update_label = Label(frame6, text="$" + self.balance, font=MEDIUM_FONT, bg='white',
                                  fg='black')
        self.update_label.place(x=80, y=110)

        # -----------------------Row 3
        Label(frame6, text="ENTER AMOUNT BELOW", font=MEDIUM_FONT, bg='white', fg='green').place(x=40, y=210)
        Label(frame6, text="Amount $", font=MEDIUM_FONT, bg='white', fg='black').place(x=10, y=240)
        self.amount_entry = Entry(frame6, textvariable=self.master.data["withdraw"], font=MEDIUM_FONT, bg='lightgray')
        self.amount_entry.place(x=80, y=240, width=100)

        # ============Options==============
        Button(frame6, text="Withdraw", bd=0, cursor='hand2',
               command=lambda: self.finishWithdraw()).place(x=80, y=430, width=180)

        Button(frame6, text="Previous", bd=0, cursor='hand2',
               command=lambda: self.master.switch_frame("AccountPage")).place(x=400, y=430, width=180)