import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # Draw the circle for the asteroid.
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # This formula will ensure the asteroid moves in a straight line.
        self.position += (self.velocity * dt)

    def split(self) -> None:
        # Immediately destroy the current asteroid.
        self.kill()

        # If this was the smallest type of asteroid, exit the method.
        # The asteroid was already "killed", so nothing else needs done.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None

        # Otherwise, we need to spawn two smaller asteroids.
        log_event("asteroid_split")

        # Generate a random floating-point number between 20 and 50. This will represent
        # the angles (positive and negative) of travel for the new asteroids.
        new_asteroids_travel_angle = random.uniform(20, 50)

        # Calculate the rotation of the vector that will be used by the two new asteroids.
        first_new_asteroid_travel_vector = self.velocity.rotate(new_asteroids_travel_angle)
        second_new_asteroid_travel_vector = self.velocity.rotate(-new_asteroids_travel_angle)

        # Compute the radius of the smaller asteroids.
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids at the position of the current asteroid.
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)

        # Set the velocity for both new asteroids and accelerate their speed by 20%.
        first_new_asteroid.velocity = first_new_asteroid_travel_vector.rotate(new_asteroids_travel_angle) * 1.2
        second_new_asteroid.velocity = second_new_asteroid_travel_vector.rotate(new_asteroids_travel_angle) * 1.2
