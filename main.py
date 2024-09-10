from introduction import introduce
import pygame


introduce()

pygame.init()

window = pygame.display.set_mode([750,750])
pygame.display.set_caption('Micromouse Simulator')
mm_logo = pygame.image.load("logo.png")
pygame.display.set_icon(mm_logo)

width = window.get_width()
height = window.get_height()


#--- Main Loop ---
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    window.fill((255,255,255))
    
    #--- Buttons ---
    
    mouse = pygame.mouse.get_pos()
    button_font = pygame.font.SysFont('Corbel',21)
    
        # "Generate Maze" Button
    
    gen_maze_text = button_font.render('Generate Maze', True, (255,255,255))

    if 0 <= mouse[0] <= 140 and 0 <= mouse[1] <= 40:
        pygame.draw.rect(window, (150,150,150), [0, 0, 140, 40])
    else:
        pygame.draw.rect(window, (0,0,0), [0, 0, 140, 40])

        # "Run" Button

    run_text = button_font.render("Run", True, (255,255,255))

    if 145 <= mouse[0] <= 285 and 0 <= mouse[1] <= 40:
        pygame.draw.rect(window, (150,150,150), [145, 0, 140, 40])
    else:
        pygame.draw.rect(window, (0,0,0), [145, 0, 140, 40])

        # "Settings" Button

    settings_text = button_font.render("Settings", True, (255,255,255))

    if 290 <= mouse[0] <= 430 and 0 <= mouse[1] <= 40:
        pygame.draw.rect(window, (150,150,150), [290, 0, 140, 40])
    else:
        pygame.draw.rect(window, (0,0,0), [290, 0, 140, 40])
        
    window.blit(gen_maze_text, (5, 10))
    window.blit(run_text, (150, 10))
    window.blit(settings_text, (295, 10))
    
    pygame.draw.rect(window, (0, 0, 0), [0, 40, 750, 5]) # Underline for the buttons
    pygame.draw.rect(window, (0,0,0), [200, 200, 350, 350]) # Maze Block
    pygame.display.update()
    
    # Rest of Code
    
    pygame.display.flip()
    
pygame.quit()
