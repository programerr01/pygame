from pygame.locals import *  #importing special key from pygame
import pygame , sys, random #importing pygame and sys module

pygame.init()  #initialising the pygame
#setting the display size
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("New pygame color") # setting up the caption
#all the colors we are going to be using in this 
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
yellow = (128,0,0)
green = (0,0,255)
blue = (0,255,0)
a = (12,23,200)
b = (120,243,12)
c =(123,0,102)
cyan = (128,128,0)


allcolors = [a,b,c, red, black,white, yellow, blue,cyan,green] #creating the dictionary object for the colors




#mainloop 
def main():
  while True:
  #Listening for the event
    for event in pygame.event.get():
      s = random.randrange(0,9,1) #getting a random intger from 
      if event.type  == QUIT: #checking if the user wants to quit or not
        pygame.quit() #quiting
        sys.exit()
      elif event.type == MOUSEBUTTONUP: #on mouse press
          win.fill(allcolors[s]) #filling the window with the random color
    pygame.display.update() #updating the display after each iteration


 main()
