import pygame
import time

def displayGridWorld(grid, title):
    black = (0,0,0) # blocked
    white = (255, 255, 255) # unblocked
    green = (0, 255, 0) # shortest path
    red = (255, 0, 0) # end
    blue =(123,104,238) # explored cells
    orange = (255, 153, 0)  #  agent

    size = [850, 850]
    screen = pygame.display.set_mode(size)
    width = 7
    height = 7
    margin = 1


    pygame.init()
    pygame.display.set_caption(title)

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(black)
        
        # draw the grid
        for i in range(len(grid)):
            for j in range(len(grid)):
                # color = white
                if grid[i][j].type == 0:
                    color = white
                elif grid[i][j].type == 1:
                    color = black
                elif grid[i][j].type == 2:
                    color = orange
                elif grid[i][j].type == 3:
                    color = red
                elif grid[i][j].type == 4:
                    color = blue  # explored cells
                else:
                    color = green  # shortest path

                pygame.draw.rect(screen, color, [(margin + width) * j + margin,(margin + height) * i + margin,width, height])
        clock.tick(20)
        pygame.display.flip()
    pygame.quit()
