import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    

    while True:
        
        # Close window on quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        # Frames
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
