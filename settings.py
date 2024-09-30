import tkinter as tk
from tkinter import font as tkfont

def settings__():
    with open("is_settings_open.txt", "w") as f:
        f.write("yes")
        f.close()

    window = tk.Tk()
    window.title("Settings")
    window.geometry("300x300")
    #window.iconbitmap("logo.ico")

    window.mainloop()

    f = open("is_settings_open.txt", "w")
    f.write("no")
    f.close()