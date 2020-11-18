# Game of life 

import pygame 
from pygame.locals import * 
import random
import time
"""
Rules of game of life :- 
1. Cell with 1 or 0 neighbours will die of loneliness 
2. Cell with 2 or 3 neighbours survive 
3. Cell with more than 4 or 4 neighbours will die of overcrowding 
4. Cell with exactly 3 neighbours will come back to life.
"""
#Global Variables 
WIDTH = 1200
HEIGHT = 1200 
RUNNING = True 
#COLOR 
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
WHITE = (255,255,255)
#GRID 
grid = [[0 for i in range(int(WIDTH/20))]for j in range(int(HEIGHT/20))]
#Initialize the game 

pygame.init()

#Intialize the window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game of Life")

#Check for the  grid for rules 
def check_rules(i,j):
    def check(i,j):
        if(i -1 >=0 and i+1 <= int(WIDTH/20)):
            if(j-1 >= 0 and j+1 <= int(HEIGHT/20)):
                return True
        return False
    life_cells = 0
    for a in range(-1,2,1):
        for b in range(-1,2,1):
            if(check(i+a,j+b)):
                if(a and b):
                    if(grid[i+a][j+b] ==1):
                        # print("yes")
                        life_cells+=1
    if(grid[i][j] == 1):
        #Rule 1
        if(life_cells < 2):
            print("change")
            grid[i][j] =0
        # Rule 2
        elif(life_cells  == 2 or life_cells == 3):
            pass
        # Rule 3
        elif(life_cells  <= 4):
            # print("change")
            grid[i][j] = 0
    if(grid[i][j] == 0):
        # Rule 4
        if(life_cells ==3):
            grid[i][j] =1 

#COLORING RULES
def color_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] ==1):
                # i = i * 20
                # j = j * 20
                # print("in Grid")
                pygame.draw.rect(win,WHITE,pygame.Rect(i*20,j*20,20,20))
    
#DRAWING THE GRID LINES
def grid_draw():
    for i in range(0 , WIDTH,20):
        for j in range(0, HEIGHT ,20):
            pygame.draw.line(win,WHITE,(i,j),(i,HEIGHT))

    for i in range(0 , WIDTH,20):
        for j in range(0, HEIGHT ,20):
            pygame.draw.line(win,WHITE,(i,j),(WIDTH,j))

# GAME OF LIFE RULES
def game_of_life():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            check_rules(i,j)
    
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(random.randrange(0,2) == 1):
                grid[i][j] = 1
def main():
    while RUNNING:
        win.fill((0,0,0))
        # check_rules()
        color_grid()
        grid_draw()
        game_of_life()
        time.sleep(0.2)
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
        pygame.display.update()
        # break

if __name__ == "__main__":
    main()