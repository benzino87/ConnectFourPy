class gamepiece:
    def __init__(self, image, xpos, ypos, speed, rowplaced):
        self.image = image
        self.speed = speed
        self.xpos = xpos
        self.ypos = ypos
        self.rowplaced = rowplaced
        #chips inheritly fall downwards
        self.pos = image.get_rect().move(xpos, ypos)
    def move(self):
        if self.pos != (self.xpos, 46*self.rowplaced, 64, 46):
            self.pos = self.pos.move(0, self.speed)
            if self.pos.bottom > 46*self.rowplaced:
                self.pos = (self.xpos, 46*self.rowplaced, 64, 46)
        # if self.pos.bottom == 500:
        #     self.pos.bottom = 0
        return self.pos
    #def stopMove(self, ypos):
