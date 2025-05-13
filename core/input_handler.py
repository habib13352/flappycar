import pygame
from core import utils

class InputHandler:
    def __init__(self, game):
        self.game = game

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if self.game.entering_name:
                if pygame.K_a <= event.key <= pygame.K_z:
                    self.game.initials[self.game.current_char_index] = chr(event.key).upper()
                    if self.game.current_char_index < 2:
                        self.game.current_char_index += 1

                elif event.key == pygame.K_LEFT and self.game.current_char_index > 0:
                    self.game.current_char_index -= 1

                elif event.key == pygame.K_RIGHT and self.game.current_char_index < 2:
                    self.game.current_char_index += 1

                elif event.key == pygame.K_BACKSPACE:
                    # Always clear the current character
                    if self.game.initials[self.game.current_char_index] != '-':
                        self.game.initials[self.game.current_char_index] = '-'
                    elif self.game.current_char_index > 0:
                        self.game.current_char_index -= 1
                        self.game.initials[self.game.current_char_index] = '-'

                elif event.key == pygame.K_RETURN:
                    name = ''.join([c for c in self.game.initials if c != '-'])
                    if name:
                        self.game.high_scores = utils.insert_highscore(self.game.high_scores, name, self.game.score)
                        utils.save_highscores(self.game.high_scores)
                    self.game.entering_name = False
                    self.game.name_entered = True

            elif event.key == pygame.K_SPACE:
                if self.game.waiting_to_start:
                    self.game.reset()
                elif self.game.game_active:
                    self.game.car.jump()
                elif not self.game.entering_name:
                    self.game.waiting_to_start = True

        return True
