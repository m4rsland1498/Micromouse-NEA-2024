import tkinter as tk
from tkinter import font as tkfont

def settings__():
    with open("is_settings_open.txt", "w") as f:
        f.write("yes")
        f.close()

    def save_function():
        mName = name.get("1.0", "end-1c")  # mouse name
        if len(mName) <= 8: # add "and not white space"
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

                # If the name wasn't found, append the new data at the end
                if not name_found:
                    f.write(mName+":"+speedV+","+accV+"\n")

            update_names()
        else:
            pass # do not save and show message

    def delete_function():
        pass

    def mouse_list():
        mouse_win = tk.Tk()
        mouse_win.title("Your Mice")
        mouse_win.geometry("300x300")

        titles = tk.Label(mouse_win, text="Name:Top Speed:Acceleration")
        titles.pack()
        global mice
        mice = tk.Label(mouse_win, text="")
        mice.pack()

        update_names()

        mouse_win.mainloop
    #-----------------------------------------------------------------------------------------

    window = tk.Tk()
    window.title("Settings")
    window.geometry("300x300")
    #window.iconbitmap("logo.ico")

    global update_names
    def update_names():
        with open("userMice.txt", "r") as f:
            names=f.read()
        mice.config(text=names)

    #-----------------------------------------------------------------------------------------

    mouse_button = tk.Button(window, text="MICE", command=(mouse_list))
    mouse_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    speed_label = tk.Label(window, text="Top Speed:")
    speed_label.grid(row=10, column=0, padx=10, pady=10, sticky="w")
    speed = tk.Scale(window, from_=0, to=200, orient="horizontal",)
    speed.grid(row=10, column=10, padx=10, pady=10, sticky="w")

    acc_label = tk.Label(window, text="Acceleration:")
    acc_label.grid(row=20, column=0, padx=10, pady=10, sticky="w")
    acc = tk.Scale(window, from_=0, to=200, orient="horizontal")
    acc.grid(row=20, column=10, padx=10, pady=10, sticky="w")

    name = tk.Text(window, height=1, width=10)
    name.grid()

    save = tk.Button(window, text="SAVE", command=(save_function))
    save.grid()

    delete = tk.Button(window, text="DELETE", command=(delete_function))
    delete.grid()

    window.mainloop()

    f = open("is_settings_open.txt", "w")
    f.write("no")
    f.close()

settings__() # for testing purposes