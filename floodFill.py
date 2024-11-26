def flood_fill(maze, SOC):
    new_SOC = []
    directions = [
                  [1,0], # right
                  [0,1], # down
                  [-1,0], # left
                  [0,-1], # up
                  ]
    completed = True
    
    for i in SOC:
        if maze[i[0]][i[1]] == "G":
            maze[i[0]][i[1]] = -1 # distances indexed at -1,
            # decrease as further away so that maze arrays
            # can still use 1 and 0 for paths and walls for continuity
        for j in directions:

            try: # catches out of bounds errors and type errors between "S"/"G" and 0/1
                if (maze[i[0]+j[0]][i[1]+j[1]] != 0) and (maze[i[0]+j[0]][i[1]+j[1]] <= maze[i[0]][i[1]]
                    or maze[i[0]+j[0]][i[1]+j[1]] == 1 
                    or maze[i[0]+j[0]][i[1]+j[1]] == "S"):
                    completed = False
                    maze[i[0]+j[0]][i[1]+j[1]] = maze[i[0]][i[1]] - 1
                    new_SOC.append(([i[0]+j[0] , i[1]+j[1]]))
            except:
                maze[1][1] = maze[i[0]][i[1]] - 1
            
    if not completed:
        return flood_fill(maze, new_SOC)
    else:
        return maze#best_path(maze, [[1,1]], False) # start coordinates

def best_path(maze, path, completed):

    directions = [
                  [1,0], # right
                  [0,1], # down
                  [-1,0], # left
                  [0,-1], # up
                  ]
    
    current = path[-1]
    next_best = [current[0]+1, current[1]+0]

    for i in directions:

        #try: # catches type errors when S is a neighbour

        if current == [1,1]: # Start node
            pfm = [1+i[0], 1+i[1]] # possible first move
            if maze[pfm[0]][pfm[1]] > maze[next_best[0]][next_best[1]]:
                next_best = [pfm[0],pfm[1]]    


        elif maze[current[0]+i[0]][current[1]+i[1]] == -1:
            path.append([current[0]+i[0], current[1]+i[1]])
            completed = True
            print("completed") # debugging
            return path
            
        elif (maze[next_best[0]][next_best[1]] < maze[current[0]+i[0]][current[1]+i[1]] 
            and maze[current[0]+i[0]][current[1]+i[1]] != 0):
            next_best = [current[0]+i[0],current[1]+i[1]]        

        #except:
            #pass # we can pass as we do not need to return to the start

    path.append(next_best)
    if not completed:
        return best_path(maze, path, completed)


# testing below 
maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 'S', 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
 [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
 [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
 [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
 [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
 [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
 [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
 [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 'G', 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
 [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
 [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maze = flood_fill(maze1, [(11,11)])
print(maze)
print(best_path(maze, [[1,1]], False)) # start coordinates