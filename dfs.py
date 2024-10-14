undicovered_maze = [['X' for _ in range(22)] for _ in range(22)]

def dfs(maze, x, y, visited, discovered_maze):

    visited.append([x,y])

    directions = [
                  [1,0], # right
                  [0,1], # down
                  [-1,0], # left
                  [0,-1], # up
                  ]
    
    neighbours = []
    for i in directions:
        neighbours.append([x+i[0], y+i[1]])

    for i in neighbours:
        if maze[i[0]][i[1]] == 0:
            discovered_maze[i[0]][i[1]] = 0
        
        elif i not in visited and i[0] != 0 and i[0] != 21 and i[1] != 0 and i[1] != 21:
            discovered_maze[i[0]][i[1]] = 1
            dfs(maze, i[0], i[1], visited, discovered_maze)

    return visited, discovered_maze

from mazes import maze1

search = dfs(maze1, 1, 1, [], undicovered_maze)
print(search[1])

        
