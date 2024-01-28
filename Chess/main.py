""" 
This is the main driver file. It will be responsible for handeling user input and displaying current GameState
object
"""

import pygame as p
import engine

p.init()
WIDTH = HEIGHT = 800
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
DARK, LIGHT = (110, 61, 42), (252, 202, 182)
FPS = 30
IMAGES = {}

"""
IMAGES will initialize a global dictionary of images. This will be called exactly once in main
"""


def loadImages():
    pieces = ["wP", "wK", "wQ", "wR", "wB", "wN", "bP", "bK", "bQ", "bR", "bB", "bN"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load("Assets/" + piece + ".svg"), (SQUARE_SIZE, SQUARE_SIZE)
        )


# drawBoard() will draw the squares on the board
def drawBoard(screen):
    screen.fill(LIGHT)
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if (r+c) % 2 == 0:
               p.draw.rect(screen, DARK, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# drawPieces() will draw the pieces on the board using the current GameState.board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if board[r][c] != "--":
                piece = board[r][c]
                screen.blit(IMAGES[piece], (SQUARE_SIZE * c, SQUARE_SIZE * r))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


"""
This will be our main driver which will be responsible for user input and updating the graphics 
"""


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()

    gs = engine.GameState()
    loadImages()
    drawGameState(screen, gs)
    p.display.update()

    sqSelected = ()  # To keep track of the squares selected by the user, (tuple, (row, col))
    playerClicks = []  # To keep track of the first and last clicked squares,[(6, 4), (4, 4)]

    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # location of the mouse in tuple (x, y)
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE  # row and column of the square clicked
                if sqSelected == (row, col):
                    sqSelected, playerClicks = (), []
                      # deselect if player clicks same square twice
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)  # append for both 1st and 2nd click
                if len(playerClicks) == 2:  # move the chess piece after 2 clicks
                    move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = [] # reset

        drawGameState(screen, gs)
        clock.tick(FPS)
        p.display.flip()

if __name__ == "__main__":
    main()
