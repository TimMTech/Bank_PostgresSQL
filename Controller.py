import tkinter as tk
from RegisterPage import Register
from LoginPage import Login
from AccountPage import AccountDash
from PersonalPage import PersonalDetails

pages = {
    "RegisterPage": Register,
    "LoginPage": Login,
    "AccountPage": AccountDash,
    "PersonalPage": PersonalDetails,
    "DepositPage": Deposit,
    "WithdrawPage": Withdraw
}


class Controller(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.data = {"firstname": tk.StringVar(),
                     "lastname": tk.StringVar(),
                     "contact": tk.StringVar(),
                     "email": tk.StringVar(),
                     "question": tk.StringVar(),
                     "answer": tk.StringVar(),
                     "password": tk.StringVar(),
                     "confirmpassword": tk.StringVar(),
                     "balance": '0',
                     "deposit": tk.StringVar(),
                     "withdraw": tk.StringVar()
                     }
        self._frame = None
        self.switch_frame("RegisterPage")

    def switch_frame(self, page_name):
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place()


if __name__ == '__main__':
    app = Controller()
    app.mainloop()
