class gameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gameboard = [[0]*width for i in range(height)]
        print(self.gameboard)
        self.currentPlayer = 1
        self.winner = 0
    def changePlayer(self):
        if(self.currentPlayer == 1):
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1
    def playerMove(self, col):
        for row in range(self.height-1, -1, -1):
            if self.gameboard[row][col] == 0:
                self.gameboard[row][col] = self.currentPlayer
                #return row for image placement
                return row
        return -1

    def checkVerticalWin(self):
        count = 1
        for col in range(self.width):
            for row in range(self.height-1, -1, -1):
                if self.gameboard[row][col] == self.currentPlayer:
                    count += 1
                    if count == 4:
                        self.winner = self.currentPlayer
                else:
                    count = 0

    def checkHorizontalWin(self):
        count = 1
        for row in range(self.height-1, -1, -1):
            for col in range(self.width):
                if self.gameboard[row][col] == self.currentPlayer:
                    count += 1
                    if count == 4:
                        self.winner = self.currentPlayer
                else:
                    count = 0

    def checkDiagonalWin(self):
        count = 1
        for row in range(self.height-1, -1, -1):
            for col in range(self.width):
                for i in range(4):
                    if row + i < self.height -1 and col + i < self.width -1:
                        if self.gameboard[row+i][col+i] == self.currentPlayer:
                            count += 1
                            if count == 4:
                                self.winner = self.currentPlayer
                        else:
                            count = 0
                for i in range(4):
                    if row + i < self.height and col - i > 0:
                        if self.gameboard[row+i][col-i] == self.currentPlayer:
                            count += 1
                            if count == 4:
                                self.winner = self.currentPlayer
                        else:
                            count = 0
