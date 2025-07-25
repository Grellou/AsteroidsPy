import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # Small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Medium - Large asteroid
        else:
            random_angle = random.uniform(20.0, 50.0)

            asteroid_one_vector = (
                pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            )
            asteroid_two_vector = (
                pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
            )

            asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(
                self.position.x, self.position.y, asteroid_radius  # type: ignore
            )
            asteroid_two = Asteroid(
                self.position.x, self.position.y, asteroid_radius  # type: ignore
            )

            asteroid_one.velocity = asteroid_one_vector
            asteroid_two.velocity = asteroid_two_vector
