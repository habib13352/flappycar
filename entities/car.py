import pygame
from core import settings

class Car:
    def __init__(self):
        # Store vertical position as a float for sub-pixel smoothness
        self.y = settings.HEIGHT / 2
        self.movement = 0.0

        # Physics constants
        self.gravity       = 0.35 # stronger pull down
        self.jump_strength = -7.5 # harder, quicker lift
        self.max_fall_speed = 9    # limits your dive speed

        # Dimensions and base image
        self.width, self.height = 50, 30
        self.base_image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.base_image, settings.CAR_COLOR, (0, 0, self.width, self.height))

        # Actual rect for collisions & positioning
        self.rect = self.base_image.get_rect(center=(100, int(self.y)))

    def update(self):
        # Apply gravity but cap to terminal velocity
        self.movement = min(self.movement + self.gravity, self.max_fall_speed)
        # Update float-based y and sync to the rect
        self.y += self.movement
        self.rect.centery = round(self.y)

    def jump(self):
        # Instant upward thrust
        self.movement = self.jump_strength

    def draw(self, screen):
        # Compute tilt angle: up to +25° on a flap, up to -90° when diving
        # We invert sign so upward movement (negative y-velocity) tilts up
        angle = -self.movement * 3
        angle = max(-25, min(90, angle))

        # Rotate the base image and re-center it
        rotated = pygame.transform.rotate(self.base_image, angle)
        rotated_rect = rotated.get_rect(center=self.rect.center)

        # Blit the rotated sprite
        screen.blit(rotated, rotated_rect)
