import pygame
from core import settings  # Import global settings like fonts, colors, screen dimensions

class HUD:
    # Draws the current score on the screen
    def draw_score(self, screen, score, flash_timer):
        # If flash_timer > 0, flash the score in yellow (e.g., after scoring)
        color = settings.WHITE if flash_timer == 0 else settings.YELLOW
        text = settings.FONT.render(f"Score: {score}", True, color)
        screen.blit(text, (20, 20))  # Draw at top-left corner

    # Displays current level parameters (like speed and pipe gap)
    def draw_level_info(self, screen, speed, gap):
        text = settings.SMALL_FONT.render(f"Speed: {speed}, Gap: {gap}", True, settings.WHITE)
        screen.blit(text, (20, 70))  # Display under the score

    # Shows the current frames-per-second in the top-right corner
    def draw_fps(self, screen, clock):
        fps = int(clock.get_fps())
        fps_text = settings.SMALL_FONT.render(f"FPS: {fps}", True, settings.WHITE)
        screen.blit(fps_text, (settings.WIDTH - 100, 20))

    # Renders the initials input screen after the game ends
    def draw_initials(self, screen, initials, current_index):
        # Display prompt text
        prompt = settings.FONT.render("ENTER YOUR INITIALS", True, settings.WHITE)
        screen.blit(prompt, (settings.WIDTH // 2 - prompt.get_width() // 2, settings.HEIGHT // 2 - 120))

        # Draw three letters for initials, highlight the currently selected one
        for i in range(3):
            char = initials[i] if initials[i] != '-' else '-'  # Placeholder if empty
            color = settings.YELLOW if i == current_index else settings.WHITE  # Highlight selected
            rendered = settings.LARGE_FONT.render(char, True, color)
            # Position letters side-by-side horizontally
            x = settings.WIDTH // 2 - 80 + i * 60
            screen.blit(rendered, (x, settings.HEIGHT // 2 - rendered.get_height() // 2))

    # Displays the top high scores on a background box
    def draw_highscores(self, screen, scores):
        # Draw "HIGH SCORES" title
        title = settings.LARGE_FONT.render("HIGH SCORES", True, settings.WHITE)
        screen.blit(title, (settings.WIDTH // 2 - title.get_width() // 2, 100))

        # Draw background box behind the scores
        bg = pygame.Surface((settings.WIDTH - 80, settings.MAX_SCORES * 40 + 20))
        bg.fill(settings.GREY)
        screen.blit(bg, (40, 180))

        # Loop through each score and draw it
        for i, entry in enumerate(scores[:settings.MAX_SCORES]):
            label = settings.FONT.render(f"{i+1}. {entry['name']} - {entry['score']}", True, settings.WHITE)
            screen.blit(label, (settings.WIDTH // 2 - label.get_width() // 2, 200 + i * 40))
