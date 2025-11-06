"""
Game constants and configuration values.
All magic numbers and configuration should be defined here.
"""

# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pacman Game - Junior.guru Challenge"
FPS = 60

# Game grid settings
TILE_SIZE = 32  # Size of each grid tile in pixels
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# Player settings
PLAYER_SPEED = 3
PLAYER_SIZE = 28

# Ghost settings
GHOST_SPEED = 2.5
GHOST_SCARED_SPEED = 1.5
GHOST_SCARED_TIME = 10.0  # seconds

# Game mechanics
STARTING_LIVES = 3
DOT_POINTS = 10
POWER_PELLET_POINTS = 50
GHOST_POINTS = 200
BONUS_FRUIT_POINTS = 500

# Colors (RGB)
COLOR_WALL = (33, 33, 222)  # Blue walls
COLOR_DOT = (255, 255, 255)  # White dots
COLOR_POWER_PELLET = (255, 184, 255)  # Pink power pellets
COLOR_PLAYER = (255, 255, 0)  # Yellow Pacman
COLOR_GHOST_BLINKY = (255, 0, 0)  # Red ghost
COLOR_GHOST_PINKY = (255, 184, 255)  # Pink ghost
COLOR_GHOST_INKY = (0, 255, 255)  # Cyan ghost
COLOR_GHOST_CLYDE = (255, 184, 82)  # Orange ghost
COLOR_GHOST_SCARED = (33, 33, 255)  # Blue when scared

# Asset paths
ASSETS_DIR = "src/pacman/assets"
SPRITES_DIR = f"{ASSETS_DIR}/sprites"
SOUNDS_DIR = f"{ASSETS_DIR}/sounds"
MAPS_DIR = f"{ASSETS_DIR}/maps"
