import pygame

# Screen dimensions and frame rate
WIDTH, HEIGHT = 480, 720
FPS = 60

# Colors
SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
PIPE_GREEN = (0, 128, 0) #unused?
LIGHT_GREEN = (144, 238, 144)
CAR_COLOR = (255, 0, 0) #RED
YELLOW = (255, 255, 0)
GREY = (50, 50, 50)

# Pipe configuration
PIPE_WIDTH = 70 # Set to 60 with pixel overlap of 6
BASE_PIPE_GAP = 190 # Set to 180
PIPE_SPAWN_INTERVAL = 1500
PIPE_SPACING_PIXELS = 420  # Used to calculate dynamic spawn timing (320)
PIPE_SPEED = 2  # Will be updated dynamically (? yup fixed it i think) 
GROUND_HEIGHT = 0   # ← height of the ground image at the bottom of the screen

# Highscore limit
MAX_SCORES = 10

# Fonts
pygame.font.init()
FONT = pygame.font.Font(None, 48)
SMALL_FONT = pygame.font.Font(None, 32)
LARGE_FONT = pygame.font.Font(None, 64)
