import pygame, sys
import gamepiece
import gameEngine
from gamepiece import *
from gameEngine import *
from pygame.locals import *

#Initialize pygame
pygame.init()

#SCREEN SIZE
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#IMAGES
redimage = pygame.image.load('red_gamepiece.png')
redimage = pygame.transform.scale(redimage, (60,40))
blueimage = pygame.image.load('blue_gamepiece.png')
blueimage = pygame.transform.scale(blueimage, (64,46))

#COLORS   R   G   B
WHITE = (225,225,225)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)


gamepieces = []
gameboard = [[0]*10 for i in range(10)]
buttons = []

#Create button rectangles
for i in range(10):
    #create buttons rectangles
    button = pygame.Rect(64*i+2, 462, 60, 15)
    buttons.append(button)

#Initialize game engine
engine = gameEngine(10, 10)

def drawscreen():
    print(engine.winner)

    #redraw screen
    screen.fill(BLACK)
    for i in range(10):
        #draw vertical lines
        #            (x  ,  y)
        startpoint = 64*i, 0
        endpoint = 64*i, 460
        pygame.draw.line(screen, WHITE, startpoint, endpoint)

        #draw horizontal lines
        startpoint = 0, 46*i
        endpoint = 640, 46*i
        pygame.draw.line(screen, WHITE, startpoint, endpoint)


    #draw buttons
    for i in range(10):
        pygame.draw.rect(screen, WHITE, buttons[i])
    #redraw each gampiece
    for p in gamepieces:
        p.move()
        screen.blit(p.image, p.pos)

    if engine.winner != 0:
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "PLAYER " +str(engine.winner) + "WINS!!"
        textsurface = myfont.render(text, False, WHITE)
        screen.blit(textsurface,(width/2,height/2))


    pygame.display.update()
    pygame.time.delay(50)

while(1):
    #handle game events
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
        #check if clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(10):
                if buttons[i].collidepoint(x, y):
                    rowplaced = engine.playerMove(i)
                    if rowplaced == -1:
                        break
                    if engine.currentPlayer == 1:
                        piece = gamepiece(redimage, 64*i, 0, 10, rowplaced)
                    else:
                        piece = gamepiece(blueimage, 64*i, 0, 10, rowplaced)

                    gamepieces.append(piece)
                    engine.checkVerticalWin()
                    engine.checkHorizontalWin()
                    engine.checkDiagonalWin()


                    print("player %d clicked pos %d!" % (engine.currentPlayer, i))

                    engine.changePlayer()
    drawscreen()
