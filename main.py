import pygame
import sys
#import player  # DOES NOT WORK for some reason... online docs say otherwise, so.
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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

    # Create two separate groups to store "updatable" and "drawable" objects.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Create a group for the asteroid objects.
    asteroids = pygame.sprite.Group()
    # Create a group for the shot objects.
    shots = pygame.sprite.Group()

    # Ensure the player is in these groups prior to the game loop!
    Player.containers = (updatable, drawable)
    # Ensure the asteroid and asteroidfield objects are in the correct groups prior to the game loop!
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    # Ensure the shot objects are in the correct groups prior to the game loop!
    Shot.containers = (shots, updatable, drawable)

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

        # Update the rotation of the objects in the updatable group.
        updatable.update(dt)

        # Decrease the player's cooldown timer.
        player.shot_cd_timer -= dt

        # Iterate over all the objects in the asteroids group.
        for asteroid in asteroids:
            # If any of the asteroids collide with the player...
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Iterate over all objects in the drawable group and draw them individually.
        for object in drawable:
            object.draw(screen)

        # Refresh the screen.
        pygame.display.flip()

        # Update the game clock (60 FPS).
        # Calculate the delta time. The .tick() function returns millesconds, so must convert to seconds.
        dt = game_clock.tick(60) / 1000

        #print(dt)  # Debugging.

if __name__ == "__main__":
    main()
