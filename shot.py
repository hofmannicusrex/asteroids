import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the circle for the shot.
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # This formula will ensure the shot moves in a straight line.
        # print(f"self.position equals: {self.position}")  # Debugging
        # print(f"self.velocity equals: {self.velocity}")  # Debugging
        self.position += (self.velocity * dt)
