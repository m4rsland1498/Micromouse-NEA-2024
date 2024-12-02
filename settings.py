import tkinter as tk
from tkinter import font as tkfont

def settings__():
    with open("is_settings_open.txt", "w") as f:
        f.write("yes")
        f.close()

    def save_function():
        mName = name.get("1.0", "end-1c") # mouse name
        if len(mName) <= 8:
            speedV = str(speed.get()) # speed value
            accV = str(acc.get()) # acceleration Value
            with open("userMice.txt", "a") as f:
                f.write(mName+":"+speedV+","+accV+"\n")
                f.close()
        else:
            pass # do not save and show message

    window = tk.Tk()
    window.title("Settings")
    window.geometry("300x300")
    #window.iconbitmap("logo.ico")

    speed_label = tk.Label(window, text="Top Speed:")
    speed_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    speed = tk.Scale(window, from_=0, to=200, orient="horizontal")
    speed.grid(row=0, column=10, padx=10, pady=10)

    acc_label = tk.Label(window, text="Acceleration:")
    acc_label.grid(row=10, column=0, padx=10, pady=10, sticky="w")
    acc = tk.Scale(window, from_=0, to=200, orient="horizontal")
    acc.grid(row=10, column=10, padx=10, pady=10)

    name = tk.Text(window, height=1, width=10)
    name.grid()

    save = tk.Button(window, text="SAVE", command=(save_function))
    save.grid()

    window.mainloop()

    f = open("is_settings_open.txt", "w")
    f.write("no")
    f.close()

settings__() # for testing purposes