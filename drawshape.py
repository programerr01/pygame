#importing  all the modules
import pygame, sys, random
from pygame.locals import *
from pygame import *


#initialisng the window
pygame.init()
win = pygame.display.set_mode((1200,700))
pygame.display.set_caption("DRAWING SHAPES")

#all the colors we are going to use in the drawing
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
yellow = (126,0,0)
cyan = (124,45,64)
gray = (64,64,64)
pink = (123,12,45)


#main function
def main():
	global x,y,color,w,x2 ,y2 #global variable we are going to use outside the function
	while True: #infinite loop
		allcolors = [red, blue, gray,green, cyan,yellow,pink] dictionary of all the objects
		w = random.randint(0,4) #getting a random numbers for drawing
		c = random.randint(0,6) 
		color = allcolors[c] #getting random colors from all the colors
		x = random.randint(0,1200) #getting the x coordinate out of all the windowsize
		y = random.randint(0,700) #y coordinate
		x2= random.randint(0,509) # x2 for line
		y2 = random.randint(0,400) # y2 for line
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
		        raise SystemExit
		    elif event.type == pygame.KEYDOWN: #if keys are pressed 
		    	if event.key == pygame.K_SPACE: if space is pressed
		    		draw0() #drawing any random shape
		
		     
		pygame.display.update() #updating the screen


def draw0(): #draw method
	if w == 0:
	 	pygame.draw.rect(win,color, pygame.Rect(x,y,x+10,200))
	elif w ==1:
	 	pygame.draw.circle(win, color, (x,y), 25)
	elif w ==2:
	    pygame.draw.rect(win, color, pygame.Rect(x,y,100,100))
	elif w ==3:
		pygame.draw.line(win, color, (x, y), (x2, y2),5)		





if __name__ == "__main__":
	main()
