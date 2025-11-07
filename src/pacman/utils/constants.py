"""
Game constants and configuration values.
All magic numbers and configuration should be defined here.
"""

# Window settings
SCREEN_WIDTH = 1200  # Reduced from 1600 to fit screen better
SCREEN_HEIGHT = 900  # Reduced from 1200 to fit screen better
SCREEN_TITLE = "Chickman - Junior.guru Challenge"
FPS = 60

# Game grid settings
TILE_SIZE = 50  # Increased from 32 to 50 for better sprite visibility
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE  # 24 tiles wide
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE  # 18 tiles tall

# Chicken (player) settings
CHICKEN_SPEED = 5  # Adjusted for larger tiles
CHICKEN_SIZE = 48  # Increased from 28 to 48 for better visibility

# Fox (enemy) settings
FOX_SPEED = 4  # Adjusted for larger tiles
FOX_SCARED_SPEED = 2.5  # Adjusted for larger tiles
FOX_SCARED_TIME = 10.0  # seconds
FOX_SIZE = 48  # Size for fox sprites

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
