###
#
# AUTHOR: Jason Bensel
# DESCRIPTION: Initializes game engine and contains most functionality for
#              placement of images, including displaying the gameboard
#
# DATE 3/29/2017
#
###

#!/usr/bin/env python3
import pygame, sys, getopt, pickle
from gamepiece import *
from gameEngine import *
from pygame.locals import *
from random import randint

                    #GLOBALS    www.goo
gwidth = 10         #Width of gameboard
gheight = 10        #Height of gameboard
gsquare = None      #Square gameboard
gconnect = 4        #Required connections
gload = None        #Loaded filename

#Argument handler
try:
    opts, args = getopt.getopt(sys.argv[1:], "whc:wh:sc:w:h:s:c:l", ["width=","height=","connect=","square=","load="])
    for opt, arg in opts:
        try:
            if opt in ("-w", "--width"):
                gwidth = int(arg)
            if opt in ("-h", "--height"):
                gheight = int(arg)
            if opt in ("-s", "--square"):
                gsquare = int(arg)
            if opt in ("-c", "--connect"):
                gconnect = int(arg)
            if opt in ("-l", "--load"):
                gload = arg
        except:
            print("Not a valid number")
            sys.exit(2)
except getopt.GetoptError:
    print("-w <width> -h <height> -c <connect> -s <square> -l <load>")
    sys.exit(2)

#If square parameter is given assign to height and width for game engine object
if gsquare != None:
    gheight = gsquare
    gwidth = gsquare

#Initialize game engine
if gload != None:
    loadengine = pickle.load(open(gload, "rb"))
    gwidth = loadengine.width
    gheight = loadengine.height
    gconnect = loadengine.connect
    engine = gameEngine(loadengine.width, loadengine.height, loadengine.connect)
else:
    engine = gameEngine(gwidth, gheight, gconnect)



#Initialize pygame
pygame.init()

#SCREEN SIZE
width = 64*gwidth
height = 48*gheight
size = width, height
print(size)
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
bubblegum.play()


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


gamepieces = []     #List of all added game pieces (for drawing)
buttons = []        #List of all buttons (for drawing)

#create savebutton
save = pygame.Rect(0, 0, 64, 20)
font = pygame.font.SysFont('Comic Sans MS', 12)
text = "SAVE"
savetext = font.render(text, False, BLACK)


#Create button rectangles and add to buttons
for i in range(gwidth):
    button = pygame.Rect(64*i+2, 46*gheight+2, 60, 15)
    buttons.append(button)


###
# Saves game state
###
def savegame():
    print(engine)
    pickle.dump(engine, open("gamesave.p", "wb"))

###
# Function for redrawing screen for every game loop
###
def drawscreen():

    #redraw screen
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, WHITE, save)
    screen.blit(savetext,(0,0))

    #Draw grid for gameboard
    for i in range(gwidth):
        #draw vertical lines
        startpoint = 64*i, 0
        endpoint = 64*i, 46*gheight
        pygame.draw.line(screen, WHITE, startpoint, endpoint)

    for i in range(gheight):
        #draw horizontal lines
        startpoint = 0, 46*i
        endpoint = 64*gwidth, 46*i
        pygame.draw.line(screen, WHITE, startpoint, endpoint)


    #draw buttons
    for i in range(gwidth):
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
            if save.collidepoint(x, y):
                savegame()
            for i in range(gwidth):
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
