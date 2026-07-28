import pygame
from typing import Self


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    # Consider changing the type hint for other if another shape besides "circles"
    # are implemented in the future! Note that the collision logic would likely
    # also need altered in that scenario.
    def collides_with(self, other: Self) -> bool:
        # Calculate the distance between the "center" positions of both circle objects.
        distance_between_position_vectors: float = self.position.distance_to(other.position)
        # Retrieve the radius of both circle objects.
        self_radius: float = self.radius
        other_radius: float = other.radius

        # If the distance between each object's positions is less than the sum
        # of their radii, then we know the circles are colliding!
        if distance_between_position_vectors <= (self_radius + other_radius):
            return True
        return False
