class gamepiece:
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
    def move(self):
        if self.pos != (self.xpos, 46*self.rowplaced, 64, 46):
            self.pos = self.pos.move(0, self.speed)

            if self.pos.bottom > 46*self.rowplaced:
                self.pos = (self.xpos, 46*self.rowplaced, 64, 46)
                self.image = self.explosion
                self.isPlaced = True


        return self.pos

    def changeimg(self):
        self.image = self.chip
