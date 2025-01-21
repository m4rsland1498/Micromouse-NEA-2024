def updateTimes(minutes, seconds, best_path):
    change = False
    with open("current_mouse.txt", "r") as f:
        current = f.readline()
    if current.split(":")[0] != "default":
        with open("userMice.txt", "r") as f:
            lines = f.readlines()
        for i in lines:
            if i.split(":")[0] == current.split(":")[0]:
                _, values = i.split(":")
        try:
            speed, acceleration, cminutes, cseconds, length = map(str, values.split(",")) #current min/sec
            #current average speed
            cas = (int(length))/((int(cminutes)*60)+(int(cseconds)))
            #new average speed
            nas = (len(best_path))/((int(minutes)*60)+(int(seconds)))
            if nas > cas:
                change = True
            elif nas == cas:
                if int(minutes) < int(cminutes):
                    change = True
                elif int(minutes) == int(cminutes):
                    if int(seconds) < int(cseconds):
                        change = True

        except:
            speed, acceleration = map(str, values.split(","))
            print("hello")
            change = True

        if change:
            updatedLine = current.split(":")[0] + ":" + speed + "," + acceleration + "," + minutes + "," + seconds + "," + str(len(best_path))
            with open("userMice.txt", "r") as f:
                lines = f.readlines()

            for i in range(len(lines)):
                if lines[i].split(":")[0] == current.split(":")[0]:
                    lines[i] = updatedLine

            with open("userMice.txt", "w") as f:
                f.writelines(line if line.endswith("\n") else line + "\n" for line in lines)
