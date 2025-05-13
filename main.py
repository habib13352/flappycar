import pygame
from core import settings
from core.game import Game

debug_mode = False  # ✅ Step 1: Global toggle

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            debug_mode = not debug_mode  # ✅ Step 2: Toggle D key

        if not game.handle_events(event):
            running = False

    game.update()
    game.draw(debug_mode)  # ✅ Step 3: Pass debug mode in
    game.clock.tick(settings.FPS)

pygame.quit()
