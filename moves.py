import chess

letters = 'ABCDEFGH'

def pawn(piece):
    board = piece.getBoard()
    possibleMoves = []
    letter = piece.getPosition()[0]
    number = (int)(piece.getPosition()[1])
    if (piece.color == "white"):
        if (number<7):
            #check in front
            if (board.getPiece(letter + (str)(number+1)) == 0):
                possibleMoves.append(letter+(str)(number+1))
            #check diagonal left
            if (letter!='A'):
                if (board.getPiece(letters[letters.find(letter) - 1] + (str)(number+1))!=0):
                    if (board.getPiece(letters[letters.find(letter) - 1] + (str)(number+1)).color=='black'):
                        possibleMoves.append(letters[letters.find(letter) - 1] + (str)(number+1))
            #check diagonal right
            if (letter!='H'):
                if (board.getPiece(letters[letters.find(letter) + 1] + (str)(number+1))!=0):
                    if (board.getPiece(letters[letters.find(letter) + 1] + (str)(number+1)).color=='black'):
                        possibleMoves.append(letters[letters.find(letter) + 1] + (str)(number+1)) 
    else:
        if (number>1):
            #check in front
            if (board.getPiece(letter + (str)(number - 1)) == 0):
                possibleMoves.append(letter+(str)(number-1))
            #check diagonal left
            if (letter!='A'):
                if (board.getPiece(letters[letters.find(letter) - 1] + (str)(number-1))!=0):
                    if (board.getPiece(letters[letters.find(letter) - 1] + (str)(number-1)).color=='white'):
                        possibleMoves.append(letters[letters.find(letter) - 1] + (str)(number-1))
            #check diagonal right
            if (letter!='H'):
                if (board.getPiece(letters[letters.find(letter) + 1] + (str)(number-1))!=0):
                    if (board.getPiece(letters[letters.find(letter) + 1] + (str)(number-1)).color=='white'):
                        possibleMoves.append(letters[letters.find(letter) + 1] + (str)(number-1))
    return possibleMoves

def rook(piece):
    board = piece.getBoard()
    possibleMoves = []
    letter = piece.getPosition()[0]
    number = (int)(piece.getPosition()[1])

def knight(piece):
    board = piece.getBoard()
    possibleMoves = []
    letter = piece.getPosition()[0]
    number = (int)(piece.getPosition()[1])

def bishop(piece):
    board = piece.getBoard()
    possibleMoves = []
    letter = piece.getPosition()[0]
    number = (int)(piece.getPosition()[1])

def queen(piece):
    board = piece.getBoard()
    possibleMoves = []
    letter = piece.getPosition()[0]
    number = (int)(piece.getPosition()[1])

def king(piece):
    board = piece.getBoard()
    possibleMoves = []
    letter = piece.getPosition()[0]
    number = (int)(piece.getPosition()[1])

    
#here for lambda'ing in Piece
commands = {
    'pawn':pawn
    }
