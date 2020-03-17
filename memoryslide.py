import pygame,sys ,random #import modules we need
from pygame.locals import *

#These are some of the constant we are going to be using
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE  = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert(BOARDHEIGHT * BOARDWIDTH) % 2 ==0, 'Boards need to have an even number of boxes for pairs of matches'
#x and y margin
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT *(BOXSIZE + GAPSIZE)))/2)

#all the colors we are going to use
#   	r  g  b
gray =(100,100,100)
navyblue = (60,60,100)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,128,0)
purple = (255,0,0)
cyan = (0,255,255)

BGCOLOR = navyblue
LIGHTBGCOLOR = gray
BOXCOLOR = white
HIGHLIGHTCOLOR = blue
#all the shapes we are going to be using 
donut = "donut"
square = "square"
diamond = "diamond"
lines = "lines"
oval = "oval"

ALLCOLORS = (red , blue , green, yellow, orange , purple , cyan)
ALLSHAPES = (donut , square , diamond , lines , oval)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT , "Board is too big for the number of shapes/colors is defined"

#main function
def main():
	global FPSCLOCK , win
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	win = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

	mousex = 0
	mousey = 0
	pygame.display.set_caption("Memory game")

	mainBoard = generateRandomizedBoard()
	revealedBoxes = generateRevealBoxesData(False)

	firstSelection = None

	win.fill(BGCOLOR)
	startGameAnimation(mainBoard)

	while True:
		mouseClicked = False
		win.fill(BGCOLOR)
		drawBoard(mainBoard , revealedBoxes)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex , mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex ,  mousey = event.pos
				mouseClicked = True
		boxx , boxy = getBoxatPixel(mousex ,mousey)
		if boxx != None and boxy != None:
			if not revealedBoxes[boxx][boxy]:
				drawHighlighBox(boxx , boxy)
			if not revealedBoxes[boxx][boxy] and mouseClicked:
				revealBoxesAnimation(mainBoard , [(boxx , boxy)])
				revealedBoxes[boxx][boxy] = True

				if firstSelection == None:
					firstSelection = (boxx , boxy)
				else:
					icon1shape , icon1color = getShapeAndColor(mainBoard, firstSelection[0] , firstSelection[1])
					icon2shape , icon2color = getShapeAndColor(mainBoard ,boxx , boxy)

					if icon1shape != icon2shape or icon1color != icon2color:
						pygame.time.wait(1000)
						coverBoxesAnimation(mainBoard ,[(firstSelection[0], firstSelection[1]), (boxx , boxy)])
						revealedBoxes[firstSelection[0]][firstSelection[1]] = False

						revealedBoxes[boxx][boxy] = False
					elif hasWon(revealedBoxes):
						gameWonAnimation(mainBoard)
						pygame.time.wait(2000)

						mainBoard = generateRandomizedBoard()
						revealedBoxes = generateRevealBoxesData(False)

						drawBoard(mainBoard , revealedBoxes)
						pygame.display.update()
						pygame.time.wait(1000)

						startGameAnimation(mainBoard)
						firstSelection = None

		pygame.display.update()
		FPSCLOCK.tick(FPS)


def generateRevealBoxesData(val):
	revealedBoxes = []
	for i in range(BOARDWIDTH):
		revealedBoxes.append([val] * BOARDHEIGHT)
	return revealedBoxes

def generateRandomizedBoard():
	icons = []
	for color in ALLCOLORS:
		for shapes in ALLSHAPES:
			icons.append((shapes , color))
	random.shuffle(icons)
	numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT /2)

	icons = icons[:numIconsUsed] * 2
	random.shuffle(icons)

	Board = []
	for x in range(BOARDWIDTH):
		column = []
		for y in range(BOARDHEIGHT):
			column.append(icons[0])
			del icons[0]
		Board.append(column)
	return Board


def splitIntoGroupsOf(groupSize , theList): 
	result = []
	for i in range(0, len(theList) , groupSize):
		result.append(theList[i:i + groupSize])
	return result

def leftTopCoordOfBox(boxx , boxy):
	left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
	top = boxy * (BOXSIZE + GAPSIZE)  + YMARGIN
	return (left , top)

def getBoxatPixel(x,y):
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left , top = leftTopCoordOfBox(boxx , boxy)
			boxRect = pygame.Rect(left , top ,BOXSIZE , BOXSIZE)
			if boxRect.collidepoint(x,y):
				return (boxx , boxy)
	return (None , None)

def drawIcon(shape, color , boxx ,boxy):
	quarter = int(BOXSIZE * 0.25)
	half = int(BOXSIZE * 0.5)

	left , top = leftTopCoordOfBox(boxx , boxy)

	if shape == donut:
		pygame.draw.circle(win , color , (left + half , top+ half) , half -5)
		pygame.draw.circle(win , BGCOLOR , (left + half , top + half) , quarter -5)

	elif  shape == square:
		pygame.draw.rect(win , color , (left + quarter , top + quarter , BOXSIZE- half , BOXSIZE - half))
	elif shape == diamond:
		pygame.draw.polygon(win, color, ((left + half, top), (left+ BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top +half)))	
	elif shape == lines:
		 for i in range(0, BOXSIZE , 4):
		 	pygame.draw.line(win , color , (left , top +1) , (left + i, top))
		 	pygame.draw.line(win ,color , (left + i , top + BOXSIZE -1), (left + BOXSIZE-1 , top + i ))
	elif shape == oval:
		pygame.draw.ellipse(win , color , (left , top + quarter, BOXSIZE , half))


def getShapeAndColor(board , boxx , boxy):
	return board[boxx ][boxy][0] , board[boxx][boxy][1]

def drawBoxCovers(board , boxes , coverage):
	for box in boxes:
		left , top = leftTopCoordOfBox(box[0]   , box[1])
		pygame.draw.rect(win , BGCOLOR , (left , top , BOXSIZE , BOXSIZE))

		shape , color = getShapeAndColor(board , box[0], box[1])
		drawIcon(shape , color , box[0] , box[1])
		if coverage > 0:
			pygame.draw.rect(win , BGCOLOR , (left , top , coverage , BOXSIZE))
	pygame.display.update()
	FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board , boxesToReveal):
	for coverage in range(BOXSIZE , (-REVEALSPEED)-1 , -REVEALSPEED):
		drawBoxCovers(board , boxesToReveal , coverage)
def coverBoxesAnimation(board , boxesToCover):
	for coverage in range(0 , BOXSIZE + REVEALSPEED , REVEALSPEED):
		drawBoxCovers(board , boxesToCover , coverage)

def drawBoard(board , revealed):
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left , top = leftTopCoordOfBox(boxx , boxy)
			if not revealed[boxx][boxy]:
				pygame.draw.rect(win , BOXCOLOR , (left , top , BOXSIZE , BOXSIZE))
			else:
				shape ,color = getShapeAndColor(board , boxx , boxy)
				drawIcon(shape , color , boxx ,boxy)

def drawHighlighBox(boxx , boxy):
	left , top = leftTopCoordOfBox(boxx , boxy)
	pygame.draw.rect(win , HIGHLIGHTCOLOR , (left -5 , top -5 , BOXSIZE + 10 , BOXSIZE  +10) ,4)

def startGameAnimation(board):
	coverBoxes = generateRevealBoxesData(False)
	boxes = []
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			boxes.append((x,y))
	random.shuffle(boxes)
	boxGroups = splitIntoGroupsOf(8, boxes)

	drawBoard(board , coverBoxes)
	for boxGroups in boxGroups:
		revealBoxesAnimation(board , boxGroups)
		revealBoxesAnimation(board , boxGroups)

def gameWonAnimation(board):
	coverBoxes = generateRevealBoxesData(True)
	color1 = LIGHTBGCOLOR
	color2 = BGCOLOR

	for i in range(13):
		color1 , color2 = color2 , color1
		win.fill(color1)
		drawBoard(board , coverBoxes)
		pygame.display.update()
		pygame.time.wait(300)

def hasWon(revealedBoxes):
	for i in revealedBoxes:
		if False in i:
			return False
	return True

if __name__ == "__main__":
	main()
