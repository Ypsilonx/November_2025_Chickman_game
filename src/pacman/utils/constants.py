"""
Game constants and configuration values.
All magic numbers and configuration should be defined here.
"""

# Window settings
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Chickman - Junior.guru Challenge"
FPS = 60

# Game grid settings
TILE_SIZE = 32  # Size of each grid tile in pixels
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# Chicken (player) settings
CHICKEN_SPEED = 3
CHICKEN_SIZE = 28

# Fox (enemy) settings
FOX_SPEED = 2.5
FOX_SCARED_SPEED = 1.5
FOX_SCARED_TIME = 10.0  # seconds

# Game mechanics
STARTING_LIVES = 3
SEED_POINTS = 10  # Regular seeds
SUPER_SEED_POINTS = 50  # Power seeds
FOX_POINTS = 200  # Points for catching frightened fox
BONUS_FRUIT_POINTS = 500

# Colors (RGB)
COLOR_WALL = (33, 33, 222)  # Blue walls
COLOR_SEED = (255, 255, 255)  # White seeds
COLOR_SUPER_SEED = (255, 184, 82)  # Orange super seeds
COLOR_CHICKEN = (255, 255, 0)  # Yellow chicken
COLOR_FOX_RUSTY = (255, 69, 0)  # Orange-red fox (Rusty)
COLOR_FOX_GINGER = (255, 140, 0)  # Orange fox (Ginger)
COLOR_FOX_COPPER = (184, 115, 51)  # Brown fox (Copper)
COLOR_FOX_AMBER = (255, 191, 0)  # Yellow-orange fox (Amber)
COLOR_FOX_SCARED = (33, 33, 255)  # Blue when scared

# Asset paths
ASSETS_DIR = "src/pacman/assets"
SPRITES_DIR = f"{ASSETS_DIR}/sprites"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"
MAPS_DIR = f"{ASSETS_DIR}/maps"
