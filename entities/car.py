import pygame
import os
from core import settings

class Car:
    def __init__(self):
        # Store vertical position as a float for sub-pixel movement smoothness
        self.y = settings.HEIGHT / 2
        self.movement = 0.0

        # Physics constants
        self.gravity = 0.35
        self.jump_strength = -7.5
        self.max_fall_speed = 9

        # Sprite dimensions (looks right at 108x75)
        self.width, self.height = 108, 75

        # Load and scale pixel art sprite
        sprite_path = os.path.join("assets", "car", "red_rx7.png")
        self.base_image = pygame.image.load(sprite_path).convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image, (self.width, self.height))

        # Base rect (use smaller hitbox if needed)
        center_x, center_y = 100, int(self.y)

        # Adjust hitbox here if needed
        hitbox_width = int(self.width * 0.95)   # 95% of full width
        hitbox_height = int(self.height * 0.65)  # 65% of full height

        self.rect = pygame.Rect(0, 0, hitbox_width, hitbox_height)
        self.rect.center = (center_x, center_y)

    def update(self):
        # Apply gravity with a max fall speed (terminal velocity)
        self.movement = min(self.movement + self.gravity, self.max_fall_speed)
        self.y += self.movement
        self.rect.centery = round(self.y)

    def jump(self):
        self.movement = self.jump_strength

    def draw(self, screen, debug_mode=False):
        # Tilt the car based on movement: flap = tilt up, fall = tilt down
        angle = -self.movement * 3
        angle = max(-25, min(90, angle))

        # Rotate sprite and re-center it
        rotated = pygame.transform.rotate(self.base_image, angle)
        rotated_rect = rotated.get_rect(center=self.rect.center)

        # Draw sprite
        screen.blit(rotated, rotated_rect)

        # Optional: draw hitbox for dev mode
        if debug_mode:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
