import pygame
#import player  # DOES NOT WORK for some reason... online docs say otherwise, so.
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Initialize pygame.
    pygame.init()

    # Set the height and width of the "display".
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize a new "clock" object.
    game_clock = pygame.time.Clock()

    # Delta time. The amount of time that has passed since the previous frame.
    dt = 0.0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create two separate groups to store...
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #
    asteroids = pygame.sprite.Group()

    # Ensure the player is in both group prior to the game loop!
    Player.containers = (updatable, drawable)
    #
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Instantiate our player character.
    player: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate our asteroid field.
    asteroid_field: AsteroidField = AsteroidField()

    # Game Loop
    while True:
        # Log the state for debugging.
        log_state()

        # Process the pygame event queue.
        for event in pygame.event.get():
            # Exit the game if the user chooses to quit.
            if event.type == pygame.QUIT:
                return

        # Black background.
        screen.fill("black")

        # Update the player's rotation.
        #player.update(dt)

        # Update the rotation of the objects in the updatable group.
        updatable.update(dt)

        # Re-render the player on the screen.
        #player.draw(screen)

        # Iterate over all objects in drawable and draw them individually.
        for object in drawable:
            object.draw(screen)

        # Refresh the screen.
        pygame.display.flip()

        # Update the game clock (60 FPS).
        # Calculate the delta time.
        dt = game_clock.tick(60) / 1000

        #print(dt)  # Debugging.

if __name__ == "__main__":
    main()
