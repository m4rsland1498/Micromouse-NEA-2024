import matplotlib.pyplot as plt
import numpy as np

def statsWindow():
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

    # make data and plot
    fig, ax = plt.subplots()
    for i in miceWRD:
        time = int(i[3])*60+int(i[4]) # time in seconds
        length = int(i[5])

        ax.plot([0, time], [length,length], label=i[0],linewidth=2.0)

    plt.show()


statsWindow() # for testing purposes only
