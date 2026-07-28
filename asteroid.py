import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the circle for the asteroid.
        # pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, LINE_WIDTH)
        # pygame.draw.circle(screen, "white", super().position, self.radius, LINE_WIDTH)
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # self.x += (super().velocity * dt)
        # self.y += (super().velocity * dt)
        self.position += (self.velocity * dt)
