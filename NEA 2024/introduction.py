import tkinter as tk
from tkinter import font as tkfont


def introduce():

    window = tk.Tk()
    window.title("Introduction")
    window.geometry("750x750")
    window.iconbitmap("logo.ico")

    xlarge_font = tkfont.Font(size=24, weight="bold")
    large_font = tkfont.Font(size=15, weight="bold")
    bold = tkfont.Font(size=10, weight="bold")

    space = tk.Label(window, text="""

    """)
    space.pack()
    h1 = tk.Label(window, text="Introduction", font=xlarge_font)
    h1.pack()
    h2 = tk.Label(window, text="What is Micromouse?", font=large_font)
    h2.pack()
    p = tk.Label(window, text="""
    Micromouse is a robotics competition where small robots
    autonomously navigate a maze to reach a designated endpoint, typically the centre.
    These robots, called micromice, use sensors, motors, and control algorithms to find
    the optimal path through a square maze, usually 16 by 16 cells.

    Key rules for micromouse include:

    - Micromice must navigate without remote control or external guidance.
                
    - Competitors have a limited number of runs, with only the fastest time counting.
                
    - Micromice can use different strategies to map the maze, but cannot have pre-programmed knowledge of the layout.
                
    - The maze layout is unknown before the competition, promoting real-time problem-solving.

    Micromouse fosters innovation in robotics and encourages creative
    solutions in control systems and algorithm design.""")
    p.pack()
    space = tk.Label(window, text="")
    space.pack()
    h3 = tk.Label(window, text="This Project:", font=large_font)
    h3.pack()
    p1 = tk.Label(window, text="""
    In this NEA project, there contains:

    - A random maze generator that replicates the style of mazes found within micromice competitions.
                
    - A simulated micromouse that determines the best route by compromising between length and the speed
    at which it is able to travel (for example, corners slow down micromice).
                
    - Statistics!

    NOTE: Yes, you can see the full maze. However, the micromouse can only see what is ahead of it.""")
    p1.pack()
    space = tk.Label(window, text="")
    space.pack()

    close = tk.Button(window, text="CLOSE THIS WINDOW TO CONTINUE...", font=bold, command=window.destroy)
    close.pack()

    window.mainloop()