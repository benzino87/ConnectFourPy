###
#
# AUTHOR: Jason Bensel
# DESCRIPTION: Game piece object used for pygame placement
# DATE 3/29/2017
#
###
class gamepiece:

    ###
    # Constructor that sets the default state of a gamepiece
    # image: inital image (nuclear bomb)
    # chip: circle corresponding to player 1 or 2
    # explosion: image that flashes when bomb falls into place
    # xpos: inital x-coord position of chip cooresponding to column of gameboard
    # ypos: inital y-coord position of chip corresponding to row of gameboard
    # speed: rate at which the piece moves on screen
    # rowplaced: state of final placement of game piece after landing
    ###
    def __init__(self, image, chip, explosion, xpos, ypos, speed, rowplaced):
        self.image = image
        self.chip = chip
        self.explosion = explosion
        self.speed = speed
        self.xpos = xpos
        self.ypos = ypos
        self.isPlaced = False
        self.rowplaced = rowplaced
        #chips inheritly fall downwards
        self.pos = image.get_rect().move(xpos, ypos)

    ###
    # Method to handle movement of falling object and image altering
    # returns: final position of image
    ###
    def move(self):
        if self.pos != (self.xpos, 46*self.rowplaced, 64, 46):
            self.pos = self.pos.move(0, self.speed)

            if self.pos.bottom > 46*self.rowplaced:
                self.pos = (self.xpos, 46*self.rowplaced, 64, 46)
                self.image = self.explosion
                self.isPlaced = True


        return self.pos

    ###
    # Method to change the final state of the image to the corresponding player
    # chip
    ###
    def changeimg(self):
        self.image = self.chip
