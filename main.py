import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import threading

from introduction import introduce
import pygame
from mazes import mazes
from mazes import blank
import random
from button_functions import draw_maze
from button_functions import settings_
from dfs import dfs
import mouse
import buttons
from floodFill import flood_fill
from floodFill import delay_coefficient_calculator


global maze
maze = blank
introduce()

f = open("is_settings_open.txt", "w")
f.write("no")
f.close()
is_open = "no"

pygame.init()

window = pygame.display.set_mode([750,750])
pygame.display.set_caption('Micromouse Simulator')
mm_logo = pygame.image.load("logo.png")
pygame.display.set_icon(mm_logo)

width = window.get_width()
height = window.get_height()

#--- Initialising Buttons (and mouse) --- 
gen_maze = buttons.Buttons("Generate Maze", 0, 0)
run = buttons.Buttons("Run", 145, 0)
settings = buttons.Buttons("Settings", 290, 0)

mouse_sprite = mouse.mouse_sprite()

# --- Initial variables for "Run" ---
i_in_visited = -1
i_in_best_path = 0
dfs_running = False
speed_running = False


#--- Main Loop ---
running = True
while running:
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT  and is_open == "no"):
            running = False
            
    window.fill((255,255,255))

    pygame.draw.rect(window, (0,0,0), [155, 155, 440, 440]) # Maze Block

    #--- Checks if settings is open ---
    f = open("is_settings_open.txt", "r")
    is_open = str((f.read()))
    f.close()
    
    #--- Buttons ---

    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]
    button_font = pygame.font.SysFont('Corbel',21)

    for i in buttons.Buttons.instances:
        i.draw(mouse, pygame, window, button_font, clicked)
    
        # "Generate Maze" Button
            # Draws maze    
    if (gen_maze.get_x_pos() <= mouse[0] <= gen_maze.get_x_pos()+140 and
    gen_maze.get_y_pos() <= mouse[1] <= gen_maze.get_y_pos()+40 and
    clicked == True and is_open == "no" and dfs_running == False
    and speed_running == False):
        maze = random.choice(mazes)

        mouse_sprite.x = 175
        mouse_sprite.y = 175

        # "Run" Button
            # Run function
    if (run.get_x_pos() <= mouse[0] <= run.get_x_pos()+140 and 
    run.get_y_pos() <= mouse[1] <= run.get_y_pos()+40 and
    clicked == True and is_open == "no" and maze != blank and dfs_running == False
    and speed_running == False):
    # --- dfs ----------------------------------------------------------------------------
        dfs_running = True
        speed_running = True
        i_in_visited = 0

        undiscovered_maze = [['X' for i in range(22)] for i in range(22)]
        visited = []

        df_search = dfs(maze, 1, 1, visited, undiscovered_maze)

        maze = df_search[1]
        
        print(df_search[0])
    #-------------------------------------------------------------------------------------
    #--- flood fill ----------------------------------------------------------------------
        x =- 1
        y = -1
        final_x = 0
        final_y = 0
        for i in maze:
            y += 1
            x = -1
            for j in i:
                x+=1
                if maze[x][y] == "X":
                    maze[x][y] = 0
                elif maze[x][y] == "G":
                    final_x = x
                    final_y = y
                else:
                    pass
        best_path = flood_fill(maze, [(final_x,final_y)])
        print("maze:", maze)
        print("best_path:", best_path)
        speed = 50 # temporary value, will be gotten from user settings
        acceleration = 50 # temporary value, will be gotten from user settings
        vCoefficients = delay_coefficient_calculator(best_path, speed, acceleration)
    #-------------------------------------------------------------------------------------

        # "Settings" Button
            # Opens Settings
    if (settings.get_x_pos() <= mouse[0] <= settings.get_x_pos()+140 and
    settings.get_y_pos() <= mouse[1] <= settings.get_y_pos()+40 and
    clicked == True and is_open == "no" and dfs_running == False
    and speed_running == False): 

        threading.Thread(target=settings_).start()

    #-------------------------------------------------------------------------------------    
    
    pygame.draw.rect(window, (0, 0, 0), [0, 40, 750, 5]) # Underline for the buttons
    draw_maze(maze, window, pygame)

    if maze != blank:
        mouse_sprite.draw(window, pygame) #draws mouse if a maze has been generated
    
    # --- Visuals when mouse is running dfs-----------------------------------------------
    try:
        if i_in_visited == len(df_search[0]) or i_in_visited == -1:
            dfs_running = False
            i_in_visited = -1
        else:
            mouse_sprite.x = 155 + (df_search[0][i_in_visited][1]*20)
            mouse_sprite.y = 155 + (df_search[0][i_in_visited][0]*20)
            i_in_visited += 1

        if dfs_running == True:
            #pygame.time.delay(150) # disable for speed while testing
            pass
    except:
        pass
    #-------------------------------------------------------------------------------------
    # --- Visuals when mouse is running flood_fill----------------------------------------
    if i_in_visited == -1 and speed_running == True:
        if i_in_best_path == len(best_path):
            speed_running = False
            i_in_visited = -1
            i_in_best_path = 0
        else:
            mouse_sprite.x = 155 + (best_path[i_in_best_path][1]*20)
            mouse_sprite.y = 155 + (best_path[i_in_best_path][0]* 20)
            i_in_best_path += 1

        print("i_in_best_path:", i_in_best_path)
        print("vCoefficients:", vCoefficients)
        coefficient = vCoefficients[i_in_best_path - 1]
        pygame.time.delay(int(1000*coefficient))

    #-------------------------------------------------------------------------------------

    pygame.display.update()
    
    # Rest of Code
    
pygame.quit()
    # Rest of Code
    
pygame.quit()
