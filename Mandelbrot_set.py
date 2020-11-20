import pygame 
from pygame.locals import * 
import time , sys 

#GLOBAL VARIABLE 
WIDTH = 400
HEIGHT = 400
running = True
val =2
#Initialize the game 
pygame.init()

#Initialize the window 
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Set")

#Pixels array 
pxarry = pygame.PixelArray(win)


#Functions
def map(value , leftmin ,leftmax , rightmin , rightmax):
    leftSpan = leftmax - leftmin
    rightSpan = rightmax - rightmin

    valueScaled = float(value -leftmin)/float(leftSpan)

    return rightmin +( valueScaled * rightSpan)
def check_for_exit():
    global running 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running = False
    
def mandelbrot_set():
    global val
    off =0.01
    for x in range(WIDTH):
        for y in range(HEIGHT):
            a = map(x,100,WIDTH+off,-val,val)
            b = map(y,100,HEIGHT,-val,val)
            
            n = 0
            z = 0
            ca = a
            cb = b
            while(n < 100):
                aa = a*a - b*b
                bb =2*a*b
                a = aa + ca
                b = bb + cb
                if(a+b > 16):
                    break
                n+=1
            bright = 10
            if(n ==100):
                bright = 101

            pxarry[x,y] =(bright,bright,bright)
    val -=0.09+off
    off-=0.008
          
def main():
    while running:
        check_for_exit()
        mandelbrot_set()
        pygame.display.update()



if __name__ == "__main__":
    main()
