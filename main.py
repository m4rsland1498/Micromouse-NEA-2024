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
import time


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
start_ticks = 0
clock = pygame.time.Clock()


#--- Main Loop ---
running = True
while running:
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT  and is_open == "no"):
            running = False
            
    window.fill((255,255,255))

    # --- clock ---
    if not speed_running:
        minutes = "0"
        seconds = "0"
        start_ticks = 0
        try:
            if i_in_visited == len(best_path) and dfs_running == False:
                with open("current_mouse.txt", "r") as f:
                    current = f.readlines()[0]
                with open("userMice.txt", "r") as f:
                    lines = f.readlines()
                change = False
                try:
                    with open("current_mouse.txt", "r") as file:
                        line = file.readline().strip()
                    _, values = line.split(":")  # Split by colon
                    speed, acceleration, oldminutes, oldseconds = map(float, values.split(","))
                    if oldminutes < minutes:
                        change = True
                    if oldminutes == minutes:
                        if oldseconds < seconds:
                            change = True
                except:
                    change = True
                
                if change:
                    for i in range(len(lines)):
                        if current == lines[i].split(":")[0]:
                            lines[i] = lines[i]+","+minutes+seconds
        except:
            pass
    else:
        elapsed_time = pygame.time.get_ticks() - start_ticks
        minutes = str(elapsed_time // 60000)
        seconds = str((elapsed_time // 1000) % 60)
    
    font = pygame.font.SysFont(None, 100)

    minutes_surface = font.render(minutes, True, (0, 0, 0))
    colon_surface = font.render(":", True, (0, 0, 0))
    seconds_surface = font.render(seconds, True, (0, 0, 0))

    # Calculate positions
    center_x = window.get_width() // 2
    center_y = 100

    # Align text around the colon
    colon_rect = colon_surface.get_rect(center=(center_x, center_y))
    minutes_rect = minutes_surface.get_rect(right=colon_rect.left, centery=center_y)
    seconds_rect = seconds_surface.get_rect(left=colon_rect.right, centery=center_y)

    # Blit to the screen
    window.blit(minutes_surface, minutes_rect)
    window.blit(colon_surface, colon_rect)
    window.blit(seconds_surface, seconds_rect)

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

        # get speed and acceleration values for current mouse
        with open("current_mouse.txt", "r") as file:
            line = file.readline().strip()
        _, values = line.split(":")  # Split by colon
        try:
            speed, acceleration, temp, temp2 = map(float, values.split(","))
        except:
            speed, acceleration = map(float, values.split(","))

        vCoefficients = delay_coefficient_calculator(best_path, speed, acceleration)

        start_ticks = pygame.time.get_ticks()
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
        try:
            mouse_sprite.x = 155 + (best_path[i_in_best_path][1]*20)
            mouse_sprite.y = 155 + (best_path[i_in_best_path][0]* 20)
            i_in_best_path += 1
        except:
            speed_running = False
            i_in_visited = -1
            i_in_best_path = 0
            
            maze = random.choice(mazes) # sends back to start and creates new maze so no errors when click run again
            mouse_sprite.x = 175
            mouse_sprite.y = 175

        print("i_in_best_path:", i_in_best_path)
        print("vCoefficients:", vCoefficients)
        coefficient = vCoefficients[i_in_best_path - 1]
        hop_delay = 13400/speed # hop_delay is in millisecondseach cell here is 20cmx20cm,
        #micrmouse speeds roughly 1-3m/s, max speed value is 200, lowest is 67, 67*1000/5
        pygame.time.delay(int(hop_delay*coefficient))

    #-------------------------------------------------------------------------------------

    pygame.display.update()
    clock.tick(60)
    
    # Rest of Code
    
pygame.quit()
    # Rest of Code
    
pygame.quit()
