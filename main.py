import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

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

        # Refresh the screen.
        pygame.display.flip()

if __name__ == "__main__":
    main()
