# debug_pipe_cap.py

import pygame
import os
from core import settings

# ← tweak this to match the PIPE_CAP_HEIGHT you’re trialing in pipe.py
CAP_HEIGHT = 32  

def main():
    pygame.init()
    # needed so convert_alpha() works
    pygame.display.set_mode((1, 1))

    sprite_path = os.path.join("assets", "pipe", "pipe3.png")
    raw = pygame.image.load(sprite_path).convert_alpha()
    print("Raw image size:         ", raw.get_size())

    # 1) Crop transparent border
    crop_rect = raw.get_bounding_rect()
    cropped = raw.subsurface(crop_rect).copy()
    print("Cropped sprite size:    ", cropped.get_size())

    # 2) Scale to your PIPE_WIDTH
    target_w = settings.PIPE_WIDTH
    scale_factor = target_w / crop_rect.width
    scaled_h = int(crop_rect.height * scale_factor)
    scaled = pygame.transform.scale(cropped, (target_w, scaled_h))
    print("🔍 SCALED PIPE SIZE:     ", scaled.get_size())

    # 3) Slice out the cap and report its height
    cap_slice = scaled.subsurface((0, 0, target_w, CAP_HEIGHT))
    print("🔍 CURRENT CAP_HEIGHT:   ", cap_slice.get_height())

    pygame.quit()

if __name__ == "__main__":
    main()
