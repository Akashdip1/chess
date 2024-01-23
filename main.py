import pygame

pygame.init()

WIDTH, HEIGHT = 1600, 1600

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill("white")
        pygame.display.update()
        
        clock.tick(FPS)
    pygame.quit()
       
if __name__ == "__main__":
    main()
