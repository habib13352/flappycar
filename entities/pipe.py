import pygame
import random
from core import settings

class PipePair:
    def __init__(self, x, gap):
        # Dynamically adjust minimum gap based on current speed
        if settings.PIPE_SPEED < 6:
            min_gap = 120
            variation_pct = 0.06
        elif settings.PIPE_SPEED < 8:
            min_gap = 110
            variation_pct = 0.09
        else:
            min_gap = 100
            variation_pct = 0.12

        self.base_gap = max(min_gap, gap)

        # Add randomness to make pipe openings feel varied
        variation = int(self.base_gap * variation_pct)
        gap_variation = random.randint(-variation, variation)
        self.gap = self.base_gap + gap_variation

        # Calculate height of top and bottom pipes
        top_height = random.randint(50, settings.HEIGHT - self.gap - 150)
        bottom_height = settings.HEIGHT - (top_height + self.gap)

        # Create top and bottom pipes as pygame rectangles
        self.top = pygame.Rect(x, 0, settings.PIPE_WIDTH, top_height)
        self.bottom = pygame.Rect(x, top_height + self.gap, settings.PIPE_WIDTH, bottom_height)

        self.passed = False  # Marks if player has passed this pipe (for scoring)

    def update(self):
        # Move the pipes left by the current global pipe speed
        self.top.centerx -= settings.PIPE_SPEED
        self.bottom.centerx -= settings.PIPE_SPEED

    def draw(self, screen):
        # Draw both top and bottom pipes
        pygame.draw.rect(screen, settings.PIPE_GREEN, self.top)
        pygame.draw.rect(screen, settings.PIPE_GREEN, self.bottom)

    def is_off_screen(self):
        # True if the pipe has moved off the left side of the screen
        return self.top.right < 0

    def has_passed(self, car_rect):
        # True if the car has passed the pipe (used to count score once per pipe)
        return not self.passed and self.top.right < car_rect.left
