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
        return best_path(maze, [[1,1]], False) # start coordinates

def best_path(maze, path, completed):

    directions = [
                  [1,0], # right
                  [0,1], # down
                  [-1,0], # left
                  [0,-1], # up
                  ]
    
    current = path[-1]
    next_best = [0,0]
    for k in directions:
                next_best = [current[0]+k[0], current[1]+k[1]]
                if maze[next_best[0]][next_best[1]] != 0:
                    break

    for i in directions:

        if current == [1,1]: # Start node
            pfm = [0,0]
            for j in directions:
                pfm = [1+j[0], 1+j[1]] # possible first move
                if maze[pfm[0]][pfm[1]] != 0:
                    break
            if maze[pfm[0]][pfm[1]] > maze[next_best[0]][next_best[1]]:
                next_best = [pfm[0],pfm[1]]    

        elif maze[current[0]+i[0]][current[1]+i[1]] == -1:
            path.append([current[0]+i[0], current[1]+i[1]])
            completed = True
            print("completed") # debugging
            return path # base case
            
        elif (maze[next_best[0]][next_best[1]] < maze[current[0]+i[0]][current[1]+i[1]] 
            and maze[current[0]+i[0]][current[1]+i[1]] != 0):
            next_best = [current[0]+i[0],current[1]+i[1]]        

    path.append(next_best)
    if not completed:
        print(best_path)
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
#print(best_path(maze, [[1,1]], False)) # start coordinates