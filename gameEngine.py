###
#
# AUTHOR: Jason Bensel
# DESCRIPTION: Game engine object which holds the game state
# DATE 3/29/2017
#
###
import pickle

class gameEngine:

    ###
    # Constructor initializes empty gameboard with given size and sets
    # current player
    # width: number of columns gameboard will contain
    # height: number of rows the gameboard will contain
    # connect: required number of connections for a winner
    ###
    def __init__(self, width, height, connect):
        self.width = width
        self.height = height
        self.connect = connect
        self.gameboard = [[0]*width for i in range(height)]
        print(self.gameboard)
        self.currentPlayer = 1
        self.winner = 0

    ###
    # Simply alternates player after every move
    ###
    def changePlayer(self):
        if(self.currentPlayer == 1):
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1

    ###
    # Finds position of game piece given column and inserts game piece in
    # desired column and row
    # col: column chosen by player
    ###
    def playerMove(self, col):
        for row in range(self.height-1, -1, -1):
            if self.gameboard[row][col] == 0:
                self.gameboard[row][col] = self.currentPlayer
                #return row for image placement
                return row
        return -1

    ###
    # Checks all game pieces for vertical win by iterating through each
    # position in the gameboard and checking current position and rows above
    # current position. If count is met then set a win status
    ###
    def checkVerticalWin(self):
        count = 1
        for col in range(self.width):
            for row in range(self.height-1, -1, -1):
                if self.gameboard[row][col] == self.currentPlayer:
                    count += 1
                    if count == self.connect:
                        self.winner = self.currentPlayer
                else:
                    count = 0

    ###
    # Checks all game pieces for a horizontal win by iterating through each
    # position in the gameboard and checking current position and columns to
    # the right of current position. If count is met then set a win status
    ###
    def checkHorizontalWin(self):
        count = 1
        for row in range(self.height-1, -1, -1):
            for col in range(self.width):
                if self.gameboard[row][col] == self.currentPlayer:
                    count += 1
                    if count == self.connect:
                        self.winner = self.currentPlayer
                else:
                    count = 0

    ###
    # Checks all game pieces for a diagonal win by iterating through each
    # position in the gameboard and checking current position and column / row
    # combination to the left and right of current position. If count is met
    # then set a win status
    ###
    def checkDiagonalWin(self):
        count = 0
        for row in range(self.height-1, -1, -1):
            for col in range(self.width):
                for i in range(self.connect):
                    if row - i > 0 and col + i < self.width -1:
                        if self.gameboard[row-i][col+i] == self.currentPlayer:
                            count += 1
                            if count == self.connect:
                                self.winner = self.currentPlayer
                        else:
                            count = 0

                count = 0
                for i in range(self.connect):
                    if row - i > 0 and col - i > 0:
                        if self.gameboard[row-i][col-i] == self.currentPlayer:
                            count += 1
                            if count == self.connect:
                                self.winner = self.currentPlayer
                        else:
                            count = 0
