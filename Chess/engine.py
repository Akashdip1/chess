"""
This class is responible for storing all the informaiton about the current state of a chess game. It will also
be responible for determining valid moves at the current state. It will also keep a move log.
"""

class GameState():
    def __init__(self):
        #board is and 8x8 ed list, each element of the list has 2 chars
        #The first character represents the color of the piece i.e. b or w.
        #"--" means empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        
        self.whiteToMove = True
        self.moveLog = []
        

