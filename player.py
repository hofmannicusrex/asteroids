import pygame
#import circleshape  # DOES NOT WORK for some reason... online docs say otherwise, so.
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Should I include a type hint of : int??? This might be a float.

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        # Retrieve the list of points.
        points_of_triangle: list[pygame.Vector2] = self.triangle()

        # Draw the triangle.
        pygame.draw.polygon(screen, "white", points_of_triangle, LINE_WIDTH)

    # Handles the calculation for the rotation of the player.
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # Actually updates the player's rotation base on keyboard input.
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # Forward and backward player movement.
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)  # For backward movement, reverse the delta time.

        # Left and right player movement.
        if keys[pygame.K_a]:
            self.rotate(-dt)  # For left rotation, reverse the delta time. Seems to work fine, but double-check this later!!!
        if keys[pygame.K_d]:
            self.rotate(dt)

    def move(self, dt: float) -> None:
        # Start with a unit vector pointing straight down from (0, 0) to (0, 1).
        unit_vector = pygame.Vector2(0, 1)
        # Rotate that vector by the player's rotation, so it's pointing in the same direction as the player.
        rotated_vector = unit_vector.rotate(self.rotation)
        # Import the PLAYER_SPEED constant and multiply the vector by PLAYER_SPEED * dt so that the vector is the length the player should move during this frame.
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        # Add the vector to the player's position to move them.
        self.position += rotated_with_speed_vector
