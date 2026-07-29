import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the circle for the asteroid.
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # This formula will ensure the asteroid moves in a straight line.
        self.position += (self.velocity * dt)
