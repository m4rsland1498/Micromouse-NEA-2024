# when dfs is first called, visited = [] and discovered_maze = []

def dfs(maze, x, y, visited, discovered_maze):

    visited.append([x,y])

    directions = [
                  [1,0] # right
                  [0,1] # down
                  [-1,0] # left
                  [0,-1] # up
                  ]
    
    if maze[x][y] == "G":
        return discovered_maze
    else:
        if x != 20 and maze[x+1][y] != 0 and [x+1, y] not in visited:
            pass

        elif y != 20 and maze[x][y+1] != 0 and [x, y+1] not in visited:
            pass

        elif x != 1 and maze[x-1][y] != 0 and [x-1, y] not in visited:
            pass

        elif y!= 1 and maze[x][y-1] != 0 and [x, y-1 not in visited]:
            pass

        
