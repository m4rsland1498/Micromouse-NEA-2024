def statsWindow():
    import matplotlib
    matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt

    with open("userMice.txt", "r") as f:
        lines = f.readlines()

    miceWRD = [] # mice With Run Data
    for line in lines:
        name, values = line.split(":")
        try:
            speed, acceleration, minutes, seconds, length = map(str, values.split(","))
            miceWRD.append([name, speed, acceleration, minutes, seconds, length])
        except:
            pass

    plt.style.use("_mpl-gallery")

    # make data and plot ---------------------------------------------
    fig, ax = plt.subplots(figsize=(10,3))
    colours = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "turquoise"]

    # function to plot the initial line chart
    def plot_line_chart():
        ax.clear()
        for i in range(len(miceWRD)):
            time = int(miceWRD[i][3])*60+int(miceWRD[i][4]) # time in seconds
            length = int(miceWRD[i][5])

            ax.plot([0, time], [length,length], label=miceWRD[i][0], linewidth=2.0, color=colours[i % len(colours)])

        plt.title("Length/Time (Next[n]/Previous[p])")
        plt.xlabel("Time (s)", fontsize=12, labelpad=10)
        plt.ylabel("Length (x20cm)", fontsize=12, labelpad=10)
        ax.legend()

    # function to plot bar chart
    def plot_bar_chart():
        ax.clear()
        names = [mouse[0] for mouse in miceWRD]
        efficiencies = [int(mouse[5])/(int(mouse[3])*60+int(mouse[4])) for mouse in miceWRD]
        ax.bar(names, efficiencies, color=[colours[i] for i in range(len(miceWRD))])
        plt.title("Efficiencies (Next[n]/Previous[p])")
        plt.xlabel("Mice", fontsize=12, labelpad=10)
        plt.ylabel("Efficiency", fontsize=12, labelpad=10)

    # start with line chart
    plot_line_chart()

    # function to switch between graphs
    def switch_graph(event):
        if event.key == "n": # press 'n' for the bar chart
            plot_bar_chart()
        elif event.key == "p": # press 'p' for the line chart
            plot_line_chart()
        fig.canvas.draw() # redraw the figure

    fig.canvas.manager.set_window_title("Your Mice")

    # connect the key press event to the function
    fig.canvas.mpl_connect("key_press_event", switch_graph)

    plt.tight_layout()
    plt.show()

#statsWindow() # for testing purposes only