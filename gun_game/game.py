import pygame 
from pygame.locals import * 
from random import randint
import time
import math
from subprocess import Popen
#Globals 
WIDTH = 600
HEIGHT = 400
PX = WIDTH/2
PY = HEIGHT-40
BX = PX
BY = HEIGHT+10
shotting = False
#Initialize the game
enemies = [[WIDTH-50, 40]] 
speed = [-0.1]
bmbs_em = []
LIMIT = 0
pygame.init()



win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GUN GAME")

bg_img = pygame.image.load("bg.png")
en_im = pygame.image.load("enemy.png")
bomb_im = pygame.image.load("bomb.png")
bmb = False
hit_en = 0

# enemy = 
#Function 
def distance(x1, y1, x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def enemy():
    global LIMIT,em_im,hit_en
    if(randint(0,500) == 5 and LIMIT < 6):
        enemies.append([WIDTH-50,40])
        speed.append(-0.1 + randint(-1,0)/10)
        LIMIT +=1
    for i in range(len(enemies)):
        if(randint(0,3000) ==2):
            bmbs_em.append([enemies[i][0],enemies[i][1]])
        if(enemies[i][0] < 0 or enemies[i][0] > WIDTH):
            speed[i] *= -1
        enemies[i][0] += speed[i]
        win.blit(en_im , (enemies[i][0], enemies[i][1]))
        if(distance(enemies[i][0], enemies[i][1], BX,BY) < 16):
            # print("ENEMY DESTROYED", enemies[i])
            pygame.draw.circle(win, (255,0,0),(enemies[i][0], enemies[i][1]),20)
            win.blit(bomb_im,(enemies[i][0], enemies[i][1]))
            # enemies.remove(enemies[i])
            # speed.remove(speed[i])
            hit_en = i
            
            # time.sleep(0.1)
            # break
    if(hit_en):
        enemies.pop(hit_en)
        speed.pop(hit_en)
        hit_en =0
        LIMIT-=1
    for i in range(len(bmbs_em)):
        # print(len(bmbs_em))
        # pygame.draw.circle(win, (255,0,0),(bmbs_em[i][0], bmbs_em[i][1]),4)
        if(bmbs_em[i][1] > HEIGHT):
            bmbs_em.pop(i)
            break
        else:
            pygame.draw.circle(win, (255,0,0),(bmbs_em[i][0], bmbs_em[i][1]),4)
            bmbs_em[i][1] +=0.4

def player():
    image = pygame.image.load("player.png")
    win.blit(image,(PX,PY))

def shoot_bullets():
    global BX , BY
    pygame.draw.circle(win,(255,0,0),(BX,BY),200)
    BX = PX
    while(BY > 0):
        print(BX,BY)
        pygame.draw.circle(win, (255,0,0),(BX,BY),13)
        BY -=1
    BY = HEIGHT


while True:
    win.blit(bg_img,(0,0))
    enemy()
    pygame.draw.circle(win,(255,0,0),(BX,BY),3)
    if(shotting):
        
        BY -=0.7
        if(BY< 0):
            shotting = False
            BY = HEIGHT+10
    player()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        # print(event.type)
        if event.type == KEYDOWN or event.type == KEYUP:
            if event.key == K_LEFT:
                if(PX- 8 < 0):
                    PX = 0
                PX-=8
            if event.key == K_RIGHT:
                if(PX+8 > WIDTH-30):
                    PX = WIDTH-30
                PX+=8
            if event.key == K_UP:
                if(not shotting):
                    Popen(["play","gun_sound.ogg"])
                    BY = PY -10
                    BX = PX+15
                    shotting = True
    pygame.display.update()




