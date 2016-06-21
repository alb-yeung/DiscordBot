import moves

class Piece:
    #chess piece class
    
    def __init__(self, c, p, pos, b):
        self.color = c
        self.position = pos
        self.board = b
        b.setPiece(self,pos)
        self.getMoves = moves.commands[p]

    def getBoard(self):
        return self.board
    def getColor(self):
        return self.color
    def getPosition(self):
        return self.position

class Board:
    #board class
    def __init__(self):
        self.board = []
        for x in range(0,8):
            a = []
            for y in range(0,8):
                a.append(0)
            self.board.append(a)

    letterToNumber={
        'A':0,
        'B':1,
        'C':2,
        'D':3,
        'E':4,
        'F':5,
        'G':6,
        'H':7
        }
    def setPiece(self,piece,position):
        self.board[8-(int)(position[1])][Board.letterToNumber[position[0]]]=piece
    def getPiece(self,l,n):
        return self.board[8-n][Board.letterToNumber[l]]
    def getBoard(self):
        finalString = ""
        for x in self.board:
            for y in x:
                finalString+= (str)(y) + "\t"
            finalString+= "\n"
        print(finalString)
        #return finalString
    
