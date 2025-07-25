import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # type: ignore

    # Asteroid containers
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore

    # Asteroid field containers
    AsteroidField.containers = updatable  # type: ignore
    asteroid_field = AsteroidField()

    # Shot containers
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)  # type: ignore

    # Player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        # Close window on quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        updatable.update(dt)

        # Check for collision with player
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit()

        # Check for collision with bullets
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()

        # Draw
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        # Frames
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
