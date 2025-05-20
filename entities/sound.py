import pygame
import os

# Initialize the mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Load sound effects
flap_snd  = pygame.mixer.Sound("assets/snd/flap.mp3")
death_snd = pygame.mixer.Sound("assets/snd/death.mp3")

# Play background music (looped if loop=True)
def play_music(loop=True):
    pygame.mixer.music.load("assets/snd/music.mp3")
    pygame.mixer.music.set_volume(0.5)  # optional
    pygame.mixer.music.play(-1 if loop else 0)

# Stop music
def stop_music():
    pygame.mixer.music.stop()

# Play the flap/jump sound
def play_flap():
    flap_snd.play()

# Play the death/collision sound
def play_death():
    death_snd.play()
