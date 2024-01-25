import pygame
import chess

pygame.init()

WIDTH, HEIGHT = 1600, 1600

DARK, LIGHT=  (110, 61, 42), (252, 202, 182) 

ROWS, COLS = 8, 8

SQUARE_WIDTH, SQUARE_HEIGHT = WIDTH//8, HEIGHT//8 

PIECE_WIDTH, PIECE_HEIGHT = 200,200 

FPS = 60

#Pieces

WHITE_KING_IMAGE = pygame.image.load("Assets/wK.svg")
WHITE_KING = pygame.transform.scale(WHITE_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

WHITE_QUEEN_IMAGE = pygame.image.load("Assets/wQ.svg")
WHITE_QUEEN= pygame.transform.scale(WHITE_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

WHITE_ROOK_IMAGE = pygame.image.load("Assets/wR.svg")
WHITE_ROOK= pygame.transform.scale(WHITE_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

WHITE_KNIGHT_IMAGE = pygame.image.load("Assets/wN.svg")
WHITE_KNIGHT= pygame.transform.scale(WHITE_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

WHITE_BISHOP_IMAGE = pygame.image.load("Assets/wB.svg")
WHITE_BISHOP = pygame.transform.scale(WHITE_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

WHITE_PAWN_IMAGE = pygame.image.load("Assets/wP.svg")
WHITE_PAWN = pygame.transform.scale(WHITE_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))


BLACK_KING_IMAGE = pygame.image.load("Assets/bK.svg")
BLACK_KING = pygame.transform.scale(BLACK_KING_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

BLACK_QUEEN_IMAGE = pygame.image.load("Assets/bQ.svg")
BLACK_QUEEN = pygame.transform.scale(BLACK_QUEEN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

BLACK_ROOK_IMAGE = pygame.image.load("Assets/bR.svg")
BLACK_ROOK= pygame.transform.scale(BLACK_ROOK_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

BLACK_KNIGHT_IMAGE = pygame.image.load("Assets/bN.svg")
BLACK_KNIGHT= pygame.transform.scale(BLACK_KNIGHT_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

BLACK_BISHOP_IMAGE = pygame.image.load("Assets/bB.svg")
BLACK_BISHOP = pygame.transform.scale(BLACK_BISHOP_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))

BLACK_PAWN_IMAGE = pygame.image.load("Assets/bP.svg") 
BLACK_PAWN= pygame.transform.scale(BLACK_PAWN_IMAGE, (PIECE_WIDTH, PIECE_HEIGHT))


DICT = {
    "p" : BLACK_PAWN,
    "k" : BLACK_KING,
    "q" : BLACK_QUEEN,
    "r" : BLACK_ROOK,
    "b" : BLACK_BISHOP,
    "n" : BLACK_KNIGHT,
    "P" : WHITE_PAWN,
    "K" : WHITE_KING,
    "Q" : WHITE_QUEEN,
    "R" : WHITE_ROOK,
    "B" : WHITE_BISHOP,
    "N" : WHITE_KNIGHT
}


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def drawBoard():
    pygame.display.set_caption("Chessboard")
    for row in range(ROWS):
        for col in range(COLS):
            if (row+col) % 2 == 0:
                pygame.draw.rect(WIN, DARK, (SQUARE_WIDTH * col, SQUARE_HEIGHT * row, SQUARE_WIDTH, SQUARE_HEIGHT))
            else:
                continue

#Test - Fen to pieces on the board
fen = chess.STARTING_FEN 
def fen_to_board(fen):
    board = []
    for row in fen.split("/"):
        board_row = []
        for c in row:
            if c == " ":
                break
            elif c in "12345678":
                board_row.extend(["-"] * int(c))
            elif c.isalpha():
                board_row.append(c)
        board.append(board_row)
    return board
def drawPieces(board = fen_to_board(fen)):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "-":
                continue
            else:
                WIN.blit(DICT[board[i][j]],(PIECE_WIDTH*j, PIECE_HEIGHT*i))
# End Test

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(LIGHT)

        drawBoard()
        drawPieces()
        pygame.display.update()
        
        clock.tick(FPS)
    pygame.quit()
       
if __name__ == "__main__":
    main()
