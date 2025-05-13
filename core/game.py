import pygame
from core import settings, utils
from core.input_handler import InputHandler
from entities.car import Car
from entities.pipe import PipePair

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.car = Car()
        self.pipes = []
        self.pipe_gap = settings.BASE_PIPE_GAP
        self.score = 0
        self.high_scores = utils.load_highscores()

        self.waiting_to_start = True
        self.game_active = False
        self.entering_name = False
        self.name_entered = False

        self.initials = ['-', '-', '-']
        self.current_char_index = 0
        self.score_flash_timer = 0
        self.scored_pipes = []

        self.input_handler = InputHandler(self)

        # Distance‐based spawn tracking
        self.distance_since_last_spawn = 0

    def reset(self):
        self.car = Car()
        self.pipes.clear()
        self.scored_pipes.clear()
        self.pipe_gap = settings.BASE_PIPE_GAP
        self.score = 0
        self.score_flash_timer = 0
        self.initials = ['-', '-', '-']
        self.current_char_index = 0

        self.waiting_to_start = False
        self.game_active = True
        self.entering_name = False
        self.name_entered = False

        # Reset to base speed and spawn distance
        settings.PIPE_SPEED = 3
        self.distance_since_last_spawn = 0

        # Spawn first pipe immediately
        self.pipes.append(PipePair(settings.WIDTH, self.pipe_gap))

    def handle_events(self, event):
        return self.input_handler.handle_event(event)

    def update(self):
        if not self.game_active:
            return

        # Move car
        self.car.update()

        # Move pipes
        for pipe in self.pipes:
            pipe.update()

        # Remove off‐screen pipes
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]

        # Scoring
        for pipe in self.pipes:
            if pipe.has_passed(self.car.rect):
                self.score += 1
                pipe.passed = True
                if self.score % 5 == 0:
                    self.score_flash_timer = 15

        # Speed scaling and gap adjustment
        settings.PIPE_SPEED = 3 + 0.5 * (self.score // 5)
        self.pipe_gap = max(120, settings.BASE_PIPE_GAP - self.score * 2)

        # Pipe spawning based on distance
        self.distance_since_last_spawn += settings.PIPE_SPEED
        if self.distance_since_last_spawn >= settings.PIPE_SPACING_PIXELS:
            self.pipes.append(PipePair(settings.WIDTH, self.pipe_gap))
            self.distance_since_last_spawn -= settings.PIPE_SPACING_PIXELS

        # Flash timer
        if self.score_flash_timer > 0:
            self.score_flash_timer -= 1

        # Collision detection
        for pipe in self.pipes:
            if self.car.rect.colliderect(pipe.top) or self.car.rect.colliderect(pipe.bottom):
                self.game_active = False
                if utils.is_highscore(self.high_scores, self.score):
                    self.entering_name = True
                return

        if self.car.rect.top <= 0 or self.car.rect.bottom >= settings.HEIGHT:
            self.game_active = False
            if utils.is_highscore(self.high_scores, self.score):
                self.entering_name = True

    def draw(self, debug_mode=False):
        self.screen.fill(settings.SKY_BLUE)

        if self.waiting_to_start:
            msg = settings.FONT.render("Press SPACE to Start", True, settings.WHITE)
            x = settings.WIDTH//2 - msg.get_width()//2
            y = settings.HEIGHT//2 - msg.get_height()//2
            self.screen.blit(msg, (x, y))

        elif self.game_active:
            self.car.draw(self.screen, debug_mode)
            for pipe in self.pipes:
                pipe.draw(self.screen)

            # Score display
            color = settings.WHITE if self.score_flash_timer == 0 else settings.YELLOW
            score_text = settings.FONT.render(f"Score: {self.score}", True, color)
            speed_text = settings.SMALL_FONT.render(
                f"Speed: {settings.PIPE_SPEED}, Gap: {self.pipe_gap}", True, settings.WHITE
            )
            self.screen.blit(score_text, (20, 20))
            self.screen.blit(speed_text, (20, 70))

            # FPS
            fps = int(self.clock.get_fps())
            fps_text = settings.SMALL_FONT.render(f"FPS: {fps}", True, settings.WHITE)
            fx = settings.WIDTH - fps_text.get_width() - 20
            self.screen.blit(fps_text, (fx, 20))

            # Debug label
            if debug_mode:
                dbg_text = settings.SMALL_FONT.render("DEBUG MODE ON", True, (255, 0, 0))
                self.screen.blit(dbg_text, (20, settings.HEIGHT - 40))

        elif self.entering_name:
            prompt = settings.FONT.render("ENTER YOUR INITIALS", True, settings.WHITE)
            px = settings.WIDTH//2 - prompt.get_width()//2
            self.screen.blit(prompt, (px, settings.HEIGHT//2 - 120))
            for i in range(3):
                char = self.initials[i] if self.initials[i] != '-' else '-'
                color = settings.YELLOW if i == self.current_char_index else settings.WHITE
                rendered = settings.LARGE_FONT.render(char, True, color)
                x = settings.WIDTH//2 - 80 + i*60
                y = settings.HEIGHT//2 - rendered.get_height()//2
                self.screen.blit(rendered, (x, y))

        else:
            game_over = settings.FONT.render("Game Over", True, settings.WHITE)
            restart = settings.SMALL_FONT.render("Press SPACE to Restart", True, settings.WHITE)
            self.screen.blit(game_over, (settings.WIDTH//2 - game_over.get_width()//2, 50))
            self.screen.blit(restart, (settings.WIDTH//2 - restart.get_width()//2, settings.HEIGHT - 80))

            title = settings.LARGE_FONT.render("🏆 HIGH SCORES", True, settings.WHITE)
            tx = settings.WIDTH//2 - title.get_width()//2
            self.screen.blit(title, (tx, 100))

            bg = pygame.Surface((settings.WIDTH-80, settings.MAX_SCORES*40+20))
            bg.fill(settings.GREY)
            self.screen.blit(bg, (40, 180))
            for idx, entry in enumerate(self.high_scores[:settings.MAX_SCORES]):
                lbl = settings.FONT.render(f"{idx+1}. {entry['name']} - {entry['score']}", True, settings.WHITE)
                lx = settings.WIDTH//2 - lbl.get_width()//2
                ly = 200 + idx*40
                self.screen.blit(lbl, (lx, ly))

        pygame.display.update()
