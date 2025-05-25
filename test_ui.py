import tkinter as tk
from app.views.login import LoginWindow

def run_login_ui():
    root = LoginWindow()
    root.mainloop()

if __name__ == "__main__":
    run_login_ui()
