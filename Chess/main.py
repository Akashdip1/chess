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
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if (r + c) % 2 == 1:
                p.draw.rect(
                    screen,
                    DARK,
                    p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )


# drawPieces() will draw the pieces on the board using the current GameState.board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if board[r][c] != "--":
                piece = IMAGES[board[r][c]]
                screen.blit(piece, (SQUARE_SIZE * c, SQUARE_SIZE * r))
            else:
                continue


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)
    
"""
This will be our main driver which will be responsible for user input and updating the graphics 
"""

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(LIGHT)

    gs = engine.GameState()
    loadImages()
    drawGameState(screen, gs)
    p.display.update()

    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False


if __name__ == "__main__":
    main()
