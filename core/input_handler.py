import pygame
from core import utils

class InputHandler:
    def __init__(self, game):
        # Store reference to the Game object to access game state
        self.game = game

    def handle_event(self, event):
        # === QUIT EVENT ===
        if event.type == pygame.QUIT:
            return False  # Signal the main loop to exit

        # === KEYDOWN EVENT HANDLING ===
        if event.type == pygame.KEYDOWN:

            # === NAME ENTRY MODE (Highscore) ===
            if self.game.entering_name:
                # If a letter key A–Z is pressed
                if pygame.K_a <= event.key <= pygame.K_z:
                    self.game.initials[self.game.current_char_index] = chr(event.key).upper()
                    if self.game.current_char_index < 2:
                        self.game.current_char_index += 1  # Move to next initial

                # Navigate left in initial selection
                elif event.key == pygame.K_LEFT and self.game.current_char_index > 0:
                    self.game.current_char_index -= 1

                # Navigate right in initial selection
                elif event.key == pygame.K_RIGHT and self.game.current_char_index < 2:
                    self.game.current_char_index += 1

                # Backspace behavior: clear current or go back and clear previous
                elif event.key == pygame.K_BACKSPACE:
                    if self.game.initials[self.game.current_char_index] != '-':
                        self.game.initials[self.game.current_char_index] = '-'
                    elif self.game.current_char_index > 0:
                        self.game.current_char_index -= 1
                        self.game.initials[self.game.current_char_index] = '-'

                # Enter confirms name entry and saves the high score
                elif event.key == pygame.K_RETURN:
                    # Build name by skipping empty slots
                    name = ''.join([c for c in self.game.initials if c != '-'])
                    if name:
                        # Insert and save new high score
                        self.game.high_scores = utils.insert_highscore(self.game.high_scores, name, self.game.score)
                        utils.save_highscores(self.game.high_scores)

                    self.game.entering_name = False
                    self.game.name_entered = True

            # === GENERAL GAME KEY HANDLING ===
            elif event.key == pygame.K_SPACE:
                if self.game.waiting_to_start:
                    self.game.reset()  # Start game from waiting screen
                elif self.game.game_active:
                    self.game.car.jump()  # Trigger car flap
                elif not self.game.entering_name:
                    # From game over screen, SPACE returns to waiting state
                    self.game.waiting_to_start = True

        return True  # Continue running game loop
