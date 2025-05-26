import pygame
import random
import os
from core import settings

class PipePair:
    PIPE_WIDTH     = settings.PIPE_WIDTH
    PIPE_CAP_IMG   = None     # Bottom cap sprite (used for bottom pipe)
    PIPE_TOP_CAP   = None     # Flipped top cap (used for top pipe)
    PIPE_BODY_IMG  = None     # Repeating body tile
    CAP_HEIGHT     = 32       # Height of the pipe cap in pixels
    OVERLAP        = 3        # Overlap between body tiles to avoid visual gaps

    def __init__(self, x, gap):
        # === LOAD AND SLICE SPRITE ONLY ONCE ===
        if PipePair.PIPE_BODY_IMG is None:
            raw = pygame.image.load(
                os.path.join("assets", "sprites", "pipe", "pipe3.png")
            ).convert_alpha()

            # Crop out transparent borders using mask
            mask = pygame.mask.from_surface(raw)
            rect = mask.get_rect()
            raw = raw.subsurface(rect).copy()

            # Scale the pipe sprite to the target width
            w = PipePair.PIPE_WIDTH
            h = int(raw.get_height() * (w / raw.get_width()))
            full = pygame.transform.scale(raw, (w, h))

            # Slice out the cap and body parts
            ch = PipePair.CAP_HEIGHT
            PipePair.PIPE_CAP_IMG   = full.subsurface((0, 0, w, ch)).copy()
            PipePair.PIPE_TOP_CAP   = pygame.transform.flip(PipePair.PIPE_CAP_IMG, False, True)
            PipePair.PIPE_BODY_IMG  = full.subsurface((0, ch, w, h - ch)).copy()

        # === DETERMINE PIPE GAP BASED ON DIFFICULTY ===
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

        # === POSITION AND HITBOX SETUP ===
        self.top_height  = random.randint(50, settings.HEIGHT - self.gap - 150)
        self.bottom_y    = self.top_height + self.gap
        self.x           = x

        w = PipePair.PIPE_WIDTH
        self.top_rect    = pygame.Rect(self.x, 0, w, self.top_height)
        self.bottom_rect = pygame.Rect(self.x, self.bottom_y, w, settings.HEIGHT - self.bottom_y)

        self.passed = False  # Used for scoring when car passes pipe

    def update(self):
        # === MOVE PIPE TO THE LEFT ===
        self.x -= settings.PIPE_SPEED
        self.top_rect.x    = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen, debug_mode=False):
        ch      = PipePair.CAP_HEIGHT
        body    = PipePair.PIPE_BODY_IMG
        bh      = body.get_height()
        step    = bh - PipePair.OVERLAP

        # ========================
        # === DRAW TOP PIPE ====
        # ========================
        target = self.top_height  # Bottom of top pipe hitbox
        y = 0

        # Stack body tiles up to just before the cap
        while True:
            if y + bh >= target - ch:
                y = target - ch - (bh - PipePair.OVERLAP)
                screen.blit(body, (self.x, y))
                break
            screen.blit(body, (self.x, y))
            y += step

        # Draw top cap to align exactly with hitbox bottom
        cap_y = target - ch
        screen.blit(PipePair.PIPE_TOP_CAP, (self.x, cap_y))

        # ==========================
        # === DRAW BOTTOM PIPE ====
        # ==========================
        screen.blit(PipePair.PIPE_CAP_IMG, (self.x, self.bottom_y))
        yb = self.bottom_y + ch
        while yb < settings.HEIGHT:
            screen.blit(body, (self.x, yb))
            yb += step

        # ================================
        # === DEBUG HITBOX VISUALIZER ===
        # ================================
        if debug_mode:
            pygame.draw.rect(screen, (255, 0, 0), self.top_rect, 2)
            pygame.draw.rect(screen, (255, 0, 0), self.bottom_rect, 2)
            pygame.draw.line(screen, (0, 255, 0), (self.x, self.top_height), (self.x + PipePair.PIPE_WIDTH, self.top_height), 2)  # bottom of top hitbox

    def is_off_screen(self):
        # Pipe has moved off the left side of the screen
        return self.x + PipePair.PIPE_WIDTH < 0

    def has_passed(self, car_rect):
        # Used to detect if car has passed pipe (for scoring)
        if not self.passed and (self.x + PipePair.PIPE_WIDTH) < car_rect.left:
            self.passed = True
            return True
        return False
