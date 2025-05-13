import pygame
from core import settings
from core.game import Game

# Initialize pygame and create the game window
pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("FlappyCarCoolVer")

# Create game instance
game = Game(screen)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if not game.handle_events(event):
            running = False

    game.update()
    game.draw()
    game.clock.tick(settings.FPS)

pygame.quit()
  