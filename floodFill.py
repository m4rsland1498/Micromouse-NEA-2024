def flood_fill(maze, SOC):
    gx = SOC[0][0]
    gy = SOC[0][1]
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
                pass
            
    if not completed:
        return flood_fill(maze, new_SOC)
    else:
        return best_path(maze, [(gx,gy)])
    
def best_path(maze, path):
    directions = [
                  [1,0], # right
                  [0,1], # down
                  [-1,0], # left
                  [0,-1], # up
                  ]
    next_best = (0,0)
    print(type(next_best))
    current = path.pop()
    print(type(current))
    for i in directions:
        if maze[current[0]+i[0]][current[1]+i[1]] == -1:
            return path
        elif next_best == (0,0):
            next_best = (current[0]+i[0],current[1]+i[1])
        elif maze[current[0]+i[0]][current[1]+i[1]] < maze[next_best[0]][next_best[1]]:
            next_best = maze[next_best[0]][next_best[1]]
    path.append(next_best)
    return best_path(maze, path)


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

print(flood_fill(maze1, [(11,11)]))