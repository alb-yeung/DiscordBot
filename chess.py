import moves

class Piece:
    #chess piece class
    
    def __init__(self, c, p, pos, b):
        self.color = c
        self.name = p
        self.position = pos
        self.board = b
        b.setPiece(self)
        #self.getMoves = moves.commands[p]
    def getMoves(self):
        return moves.commands[self.name](self)
    def getBoard(self):
        return self.board
    def getColor(self):
        return self.color
    def getPosition(self):
        return self.position
    def getName(self):
        return self.name
    def move(self,pos):
        if pos in self.getMoves():
            return True
        return False

class Board:
    #board class
    def __init__(self):
        self.board = []
        for x in range(0,8):
            a = []
            for y in range(0,8):
                a.append(0)
            self.board.append(a)

    LETTERS = 'ABCDEFGH'
    def addPiece(self, color, piece, position):
        p = Piece(color, piece, position, self)
    def setPiece(self,piece, *oldPos):
        if (piece == 0):
            self.board[8-(int)(oldPos[1])][Board.LETTERS.find(oldPos[0])]=piece
            return
        position = piece.getPosition()
        self.board[8-(int)(position[1])][Board.LETTERS.find(position[0])]=piece
    def getPiece(self,position):
        return self.board[8-(int)(position[1])][Board.LETTERS.find(position[0])]
    def getBoard(self):
        finalString = ""
        for x in self.board:
            for y in x:
                if (y == 0):
                    finalString+= (str)(y) + "\t"
                else:
                    finalString+= y.getName() + "\t"
            finalString+= "\n"
        print(finalString)
        #return finalString
    
