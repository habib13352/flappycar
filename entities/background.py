import pygame
from core import settings

class Background:
    def __init__(self):
        # full-screen sky
        self.sky = pygame.image.load("assets/bkg/sky.png")\
                              .convert()
        self.sky = pygame.transform.scale(self.sky,
                                          (settings.WIDTH, settings.HEIGHT))
        
        # clouds layer (scaled 1% wider, 8% taller)
        raw_clouds = pygame.image.load("assets/bkg/clouds.png").convert_alpha()
        cw, ch = raw_clouds.get_size()
        new_w = int(cw * 1.16)  # 16% wider
        new_h = int(ch * 1.08)  # 8% taller
        self.clouds = pygame.transform.scale(raw_clouds, (new_w, new_h))

        # skyline silhouette (scaled 10% wider & taller)
        raw_skyline = pygame.image.load("assets/bkg/skyline.png").convert_alpha()
        sw, sh = raw_skyline.get_size()
        new_sw = int(sw * 1.10)  # 10% wider
        new_sh = int(sh * 1.10)  # 10% taller
        self.skyline = pygame.transform.scale(raw_skyline, (new_sw, new_sh))

       

    def draw(self, screen):
        # 1) sky
        screen.blit(self.sky, (0, 0))

        # 2) skyline
        ground_h   = settings.GROUND_HEIGHT
        skyline_h  = self.skyline.get_height()
        skyline_y  = settings.HEIGHT - ground_h - skyline_h
        screen.blit(self.skyline, (0, skyline_y))

        # 3) clouds
        clouds_h = self.clouds.get_height()
        clouds_y = (skyline_y - clouds_h // 2)
        screen.blit(self.clouds, (-37, clouds_y))