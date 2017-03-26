import pygame, sys
import gamepiece
import gameEngine
from gamepiece import *
from gameEngine import *
from pygame.locals import *
from random import randint

#Initialize pygame
pygame.init()

#SCREEN SIZE
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

#SET CAPION
pygame.display.set_caption('Connect Nukem 4')

#IMAGES
bg = pygame.image.load('img/dukenukem.jpg')
target = pygame.image.load('img/target.png')
redimage = pygame.image.load('img/red_gamepiece.png')
blueimage = pygame.image.load('img/blue_gamepiece.png')
explosion = pygame.image.load('img/explosion.png')
nuke = pygame.image.load('img/nuke.png')

#WAV FILES
sounds = ["bitchin.wav", "cry.wav", "cya_n_hell.wav", "getsome.wav", "gotta_hurt.wav", "hail.wav", "imgood.wav", "medieval.wav", "you_suck.wav", "you_will_die.wav"]
bubblegum = pygame.mixer.Sound("sounds/gum.wav")
#shotgun = pygame.mixer.Sound("mossberg.wav")
bubblegum.play()
#shotgun.play()


#RESIZE IMAGES
bg = pygame.transform.scale(bg, size)
target = pygame.transform.scale(target, (15, 15))
redimage = pygame.transform.scale(redimage, (60,40))
blueimage = pygame.transform.scale(blueimage, (64,46))
explosion = pygame.transform.scale(explosion, (60, 46))
nuke = pygame.transform.scale(nuke, (60, 46))
nuke = pygame.transform.rotate(nuke, 270)

#COLORS   R   G   B
WHITE = (225,225,225)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)

#List of all added game pieces (for drawing)
gamepieces = []
#List of all buttons (for drawing)
buttons = []

#Create button rectangles and add to buttons
for i in range(10):
    button = pygame.Rect(64*i+2, 462, 60, 15)
    buttons.append(button)

#Initialize game engine
engine = gameEngine(10, 10)

###
# Function for redrawing screen for every game loop
###
def drawscreen():

    #redraw screen
    screen.blit(bg, (0,0))

    #Draw grid for gameboard
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
        x = buttons[i].x
        y = buttons[i].y
        screen.blit(target, (x+23, y))

    #redraw each gampiece
    for p in gamepieces:
        if p.isPlaced == True:
            p.changeimg()
        p.move()
        screen.blit(p.image, p.pos)

    #Check for valid winner and print to screen
    if engine.winner != 0:
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "PLAYER " +str(engine.winner) + "WINS!!"
        textsurface = myfont.render(text, False, WHITE)
        screen.blit(textsurface,(width/2,height/2))

    pygame.display.update()
    pygame.time.delay(50)



###
# Main game loop, handles game events (user input) and alters game engine
###
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
                        piece = gamepiece(nuke, redimage, explosion, 64*i, 0, 10, rowplaced)
                    else:
                        piece = gamepiece(nuke, blueimage, explosion, 64*i, 0, 10, rowplaced)

                    sound = pygame.mixer.Sound("sounds/"+sounds[randint(0, len(sounds)-1)])
                    sound.play()
                    gamepieces.append(piece)
                    engine.checkVerticalWin()
                    engine.checkHorizontalWin()
                    engine.checkDiagonalWin()

                    print("player %d clicked pos %d!" % (engine.currentPlayer, i))

                    engine.changePlayer()
    drawscreen()
