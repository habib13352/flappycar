import pygame
import random
import os
from core import settings

class PipePair:
    PIPE_WIDTH     = settings.PIPE_WIDTH
    PIPE_CAP_IMG   = None     # bottom cap
    PIPE_TOP_CAP   = None     # flipped top cap
    PIPE_BODY_IMG  = None     # body tile
    CAP_HEIGHT     = 32       # your measured cap slice
    OVERLAP        = 8        # body‐tile overlap (3)

    def __init__(self, x, gap):
        # 1) Load, crop & scale once
        if PipePair.PIPE_BODY_IMG is None:
            raw = pygame.image.load(
                os.path.join("assets", "pipe", "pipe3.png")
            ).convert_alpha()

            # Crop transparent border
            mask = pygame.mask.from_surface(raw)
            rect = mask.get_rect()
            raw = raw.subsurface(rect).copy()

            # Scale to target width
            w = PipePair.PIPE_WIDTH
            h = int(raw.get_height() * (w / raw.get_width()))
            full = pygame.transform.scale(raw, (w, h))

            # Slice cap vs body
            ch = PipePair.CAP_HEIGHT
            PipePair.PIPE_CAP_IMG   = full.subsurface((0, 0, w, ch)).copy()
            PipePair.PIPE_TOP_CAP   = pygame.transform.flip(PipePair.PIPE_CAP_IMG, False, True)
            PipePair.PIPE_BODY_IMG  = full.subsurface((0, ch, w, h - ch)).copy()

        # 2) Gap & position
        if settings.PIPE_SPEED < 4:
            min_gap, pct = 170, 0.06
        elif settings.PIPE_SPEED < 5:
            min_gap, pct = 160, 0.06
        elif settings.PIPE_SPEED < 6:
            min_gap, pct = 150, 0.08
        elif settings.PIPE_SPEED < 8:
            min_gap, pct = 150, 0.09    
        else:
            min_gap, pct = 150, 0.09

        self.base_gap    = max(min_gap, gap)
        variation        = int(self.base_gap * pct)
        self.gap         = self.base_gap + random.randint(-variation, variation)
        self.top_height  = random.randint(50, settings.HEIGHT - self.gap - 150)
        self.bottom_y    = self.top_height + self.gap
        self.x           = x

        # 3) Hitboxes
        w = PipePair.PIPE_WIDTH
        self.top_rect    = pygame.Rect(self.x, 0,    w, self.top_height)
        self.bottom_rect = pygame.Rect(self.x, self.bottom_y, w, settings.HEIGHT - self.bottom_y)
        self.passed      = False

    def update(self):
        self.x -= settings.PIPE_SPEED
        self.top_rect.x    = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen, debug_mode=False):
        ch      = PipePair.CAP_HEIGHT
        body    = PipePair.PIPE_BODY_IMG
        bh      = body.get_height()
        step    = bh - PipePair.OVERLAP

        # --- TOP PIPE ---
        target = self.top_height - ch
        y = 0
        while True:
            if y + bh > target:
                # Clamp final tile to stop exactly at the cap start
                y = target - (bh - PipePair.OVERLAP)
                screen.blit(body, (self.x, y))
                break
            screen.blit(body, (self.x, y))
            y += step

        cap_y = target - PipePair.OVERLAP
        screen.blit(PipePair.PIPE_TOP_CAP, (self.x, cap_y))

        # --- BOTTOM PIPE ---
        screen.blit(PipePair.PIPE_CAP_IMG, (self.x, self.bottom_y))
        yb = self.bottom_y + ch
        while yb < settings.HEIGHT:
            screen.blit(body, (self.x, yb))
            yb += step

        # --- DEBUG HITBOXES ---
        if debug_mode:
            pygame.draw.rect(screen, (255, 0, 0), self.top_rect, 2)
            pygame.draw.rect(screen, (255, 0, 0), self.bottom_rect, 2)

    def is_off_screen(self):
        return self.x + PipePair.PIPE_WIDTH < 0

    def has_passed(self, car_rect):
        if not self.passed and (self.x + PipePair.PIPE_WIDTH) < car_rect.left:
            self.passed = True
            return True
        return False
