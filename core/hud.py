import pygame
from core import settings

class HUD:
    def draw_score(self, screen, score, flash_timer):
        color = settings.WHITE if flash_timer == 0 else settings.YELLOW
        text = settings.FONT.render(f"Score: {score}", True, color)
        screen.blit(text, (20, 20))

    def draw_level_info(self, screen, speed, gap):
        text = settings.SMALL_FONT.render(f"Speed: {speed}, Gap: {gap}", True, settings.WHITE)
        screen.blit(text, (20, 70))

    def draw_fps(self, screen, clock):
        fps = int(clock.get_fps())
        fps_text = settings.SMALL_FONT.render(f"FPS: {fps}", True, settings.WHITE)
        screen.blit(fps_text, (settings.WIDTH - 100, 20))

    def draw_initials(self, screen, initials, current_index):
        prompt = settings.FONT.render("ENTER YOUR INITIALS", True, settings.WHITE)
        screen.blit(prompt, (settings.WIDTH // 2 - prompt.get_width() // 2, settings.HEIGHT // 2 - 120))

        for i in range(3):
            char = initials[i] if initials[i] != '-' else '-'
            color = settings.YELLOW if i == current_index else settings.WHITE
            rendered = settings.LARGE_FONT.render(char, True, color)
            x = settings.WIDTH // 2 - 80 + i * 60
            screen.blit(rendered, (x, settings.HEIGHT // 2 - rendered.get_height() // 2))

    def draw_highscores(self, screen, scores):
        title = settings.LARGE_FONT.render("HIGH SCORES", True, settings.WHITE)
        screen.blit(title, (settings.WIDTH // 2 - title.get_width() // 2, 100))
        bg = pygame.Surface((settings.WIDTH - 80, settings.MAX_SCORES * 40 + 20))
        bg.fill(settings.GREY)
        screen.blit(bg, (40, 180))

        for i, entry in enumerate(scores[:settings.MAX_SCORES]):
            label = settings.FONT.render(f"{i+1}. {entry['name']} - {entry['score']}", True, settings.WHITE)
            screen.blit(label, (settings.WIDTH // 2 - label.get_width() // 2, 200 + i * 40))
