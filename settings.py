import tkinter as tk
from tkinter import font as tkfont
import threading

def settings__():
    #with open("is_settings_open.txt", "w") as f:
        #f.write("yes")

    def save_function():
        mName = name.get("1.0", "end-1c")  # mouse name

        number_of_saved = 0
        with open("userMice.txt", "r") as f:
            for line in f:
                number_of_saved+=1

        if (len(mName) <= 8 
        and not(" " in mName or "\t" in mName or "\n" in mName 
        or "," in mName or ":" in mName)
        and mName != ""
        and mName != "default"):
        # checks length, if contains whitespace, if empty,
        # and for disallowed characters/name
            errorMsg.config(text="")
            speedV = str(speed.get())  # speed value
            accV = str(acc.get())  # acceleration value

            # Read the existing file and store all lines
            with open("userMice.txt", "r") as f:
                lines = f.readlines()

            # Check if the name already exists and overwrite it if found
            name_found = False
            with open("userMice.txt", "w") as f:
                for line in lines:
                    # Split the line into name and values, and check if the name matches
                    name_in_line = line.split(":")[0]
                    if name_in_line == mName:
                        # If the name matches, overwrite this line with the new values
                        f.write(mName+":"+speedV+","+accV+"\n")
                        name_found = True
                    else:
                        # Otherwise, just write the line back
                        f.write(line)

                # If the name wasn't found, check if enough space, and append the new data at the end
                if not name_found:
                    if number_of_saved < 15:
                        f.write(mName+":"+speedV+","+accV+"\n")
                    else:
                        errorMsg.config(text="Maximum mice reached.")
                else:
                    with open("current_mouse.txt", "r") as f:
                            current = f.readlines()[0]
                    if current.split(":")[0] == mName:
                        with open("current_mouse.txt", "w") as f:
                            f.write(mName+":"+speedV+","+accV+"\n")

            update_names()
        else:
            if mName == "default":
                errorMsg.config(text="Name not allowed.")
            elif ":" in mName or "," in mName:
                errorMsg.config(text="Character not allowed.")
            elif len(mName) > 8:
                errorMsg.config(text="Maximum 8 characters.")
            elif mName == "":
                errorMsg.config(text="Name cannot be empty.")
            else:
                errorMsg.config(text="Cannot contain whitespace.")

    def delete_function():
        mName = name.get("1.0", "end-1c")
        with open("current_mouse.txt", "r") as f:
            line = f.readlines()[0]
        if mName == line.split(":")[0]:
            with open("current_mouse.txt", "w") as f:
                f.write("default:67,67\n")
        with open("userMice.txt", "r") as f:
            lines = f.readlines()
        with open("userMice.txt", "w") as f:
            name_in = False
            for line in lines:
                if mName == line.split(":")[0]:
                    name_in = True
                    lines.remove(line)
                    for i in lines:
                        f.write(i)
            if not(name_in):
                for i in lines:
                    f.write(i)
                errorMsg.config(text="Not a saved mouse.")
            else:
                errorMsg.config(text="")

        update_names()

    def mouse_list():
        mouse_win = tk.Toplevel()
        mouse_win.title("Your Mice")
        mouse_win.geometry("600x300")

        bold = tkfont.Font(size=10, weight="bold")
        titles = tk.Label(mouse_win, text="Name:TopSpeed,Acceleration,BestMinutes,BestSeconds, LengthOfPath", font="bold")
        titles.pack()
        global miceL # mice list
        miceL = tk.Label(mouse_win, text="")
        miceL.pack()

        update_names()

        #mouse_win.mainloop()
        while True:
            try:
                # Process pending events
                mouse_win.update_idletasks()
                mouse_win.update()
            except tk.TclError:
                # Break the loop if the window is closed
                break

    def select_function():
        mName = name.get("1.0", "end-1c")
        with open("userMice.txt", "r") as f:
            lines = f.readlines()
            name_in = False
            for line in lines:
                if mName == line.split(":")[0]:
                    name_in = True
                    selection = line
                    break

        if name_in:
            with open("current_mouse.txt", "w") as f:
                f.write(selection+"\n")
        else:
            errorMsg.config(text="Not a saved mouse.")
    #-----------------------------------------------------------------------------------------

    window = tk.Tk()
    window.title("Settings")
    window.geometry("420x320")
    #window.iconbitmap("logo.ico")

    global update_names
    def update_names():
        with open("userMice.txt", "r") as f:
            names=f.read()
        try: # removes error message if save/delete whilst mouse list window not open
            miceL.config(text=names)
        except:
            pass

    #-----------------------------------------------------------------------------------------

    mouse_button = tk.Button(window, text="MICE", command=(threading.Thread(target=mouse_list)))
    mouse_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    label = tk.Label(window, text="67=1m/s(m/s/s), 200 3m/s(m/s/s)")
    label.grid()

    speed_label = tk.Label(window, text="Top Speed:")
    speed_label.grid(row=10, column=0, padx=10, pady=10, sticky="w")
    speed = tk.Scale(window, from_=67, to=200, orient="horizontal",)
    speed.grid(row=10, column=10, padx=10, pady=10, sticky="w")

    acc_label = tk.Label(window, text="Acceleration:")
    acc_label.grid(row=20, column=0, padx=10, pady=10, sticky="w")
    acc = tk.Scale(window, from_=67, to=200, orient="horizontal")
    acc.grid(row=20, column=10, padx=10, pady=10, sticky="w")

    name = tk.Text(window, height=1, width=10)
    name.grid(row=30, column=0)

    save = tk.Button(window, text="SAVE", command=(save_function))
    save.grid()

    delete = tk.Button(window, text="DELETE", command=(delete_function))
    delete.grid()

    select = tk.Button(window, text="SELECT", command=(select_function))
    select.grid()

    global errorMsg
    errorMsg = tk.Label(window, text="")
    errorMsg.grid(row=30, column=10)
    
    #window.mainloop()
    while True:
        try:
            # Process pending events
            window.update_idletasks()
            window.update()
        except tk.TclError:
            # Break the loop if the window is closed
            break

    with open("is_settings_open.txt", "w") as f:
        f.write("no")

#settings__() # for testing purposes