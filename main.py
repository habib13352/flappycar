import pygame
from core import settings
from core.game import Game

# Global toggle for enabling/disabling debug mode
debug_mode = False

# Initialize Pygame and create the main game window
pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("FlappyCarCoolVer")

# Create an instance of the Game class
game = Game(screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        # Toggle debug mode when the "D" key is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            debug_mode = not debug_mode

        # Handle other game events; if False is returned, exit the loop
        if not game.handle_events(event):
            running = False

    # Update game logic
    game.update()

    # Draw the game frame; pass debug mode flag for conditional rendering
    game.draw(debug_mode)

    # Limit the frame rate
    game.clock.tick(settings.FPS)

# Clean up and close the game window
pygame.quit()
