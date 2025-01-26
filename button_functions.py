import tkinter as tk
from tkinter import font as tkfont
from settings import settings__

def settings_():
    settings__()

def draw_maze(maze, window, pygame):
    for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 'G' or maze[i][j] == -1:
                    pygame.draw.rect(window, (255,0,0), [155+(20*j), 155+(20*i), 20, 20])
                elif maze[i][j] != 0:
                    pygame.draw.rect(window, (255,255,255), [155+(20*j), 155+(20*i), 20, 20])
                else:
                    pygame.draw.rect(window, (0,0,0), [155+(20*j), 155+(20*i), 20, 20])
                    