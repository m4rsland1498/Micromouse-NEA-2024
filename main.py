from introduction import introduce
import pygame
from settings import settings_
from mazes import mazes
from mazes import blank
import random
from button_functions import draw_maze
import buttons
import button_functions

global maze
maze = blank
introduce()

pygame.init()

window = pygame.display.set_mode([750,750])
pygame.display.set_caption('Micromouse Simulator')
mm_logo = pygame.image.load("logo.png")
pygame.display.set_icon(mm_logo)

width = window.get_width()
height = window.get_height()

#--- Initialising Buttons ---
gen_maze = buttons.Buttons("Generate Maze", 0, 0)
run = buttons.Buttons("Run", 145, 0)
settings = buttons.Buttons("Settings", 290, 0)


#--- Main Loop ---
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    window.fill((255,255,255))

    pygame.draw.rect(window, (0,0,0), [155, 155, 440, 440]) # Maze Block
    
    #--- Buttons ---
    
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]
    button_font = pygame.font.SysFont('Corbel',21)
    
        # "Generate Maze" Button
    gen_maze.draw(mouse, pygame, window, button_font, clicked)
            # Draws maze    
    if (gen_maze.get_x_pos() <= mouse[0] <= gen_maze.get_x_pos()+140 and
    gen_maze.get_y_pos() <= mouse[1] <= gen_maze.get_y_pos()+40 and
    clicked == True):
        maze = random.choice(mazes)

        # "Run" Button
    run.draw(mouse, pygame, window, button_font, clicked)
            # Run function
    if (run.get_x_pos() <= mouse[0] <= run.get_x_pos()+140 and
    run.get_y_pos() <= mouse[1] <= run.get_y_pos()+40 and
    clicked == True):
        print("run button pressed")

        # "Settings" Button
    settings.draw(mouse, pygame, window, button_font, clicked)
            # Opens Settings
    if (settings.get_x_pos() <= mouse[0] <= settings.get_x_pos()+140 and
    settings.get_y_pos() <= mouse[1] <= settings.get_y_pos()+40 and
    clicked == True):
        settings_()

    #-------------------------------------------------------------------------------------    
    
    pygame.draw.rect(window, (0, 0, 0), [0, 40, 750, 5]) # Underline for the buttons
    draw_maze(maze, window, pygame)
    pygame.display.update()
    
    # Rest of Code
    
pygame.quit()
