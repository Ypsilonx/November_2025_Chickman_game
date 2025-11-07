"""
Maze/Map module.
Handles maze layout, walls, and tile management.
"""

import arcade
from typing import List, Tuple
from pacman.utils.constants import (
    TILE_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    COLOR_WALL
)


class Maze:
    """
    Represents the game maze/map.
    
    Attributes:
        width: Width in tiles
        height: Height in tiles
        grid: 2D array representing the maze (0=empty, 1=wall)
        walls: List of wall rectangles for collision detection
    """
    
    def __init__(self):
        """Initialize the maze."""
        # Calculate grid dimensions
        self.width = SCREEN_WIDTH // TILE_SIZE
        self.height = SCREEN_HEIGHT // TILE_SIZE
        
        # Create empty grid
        self.grid: List[List[int]] = []
        
        # Wall rectangles for collision
        self.walls: List[Tuple[float, float, float, float]] = []
        
        # Create default maze
        self._create_default_maze()
        
    def _create_default_maze(self):
        """Create a simple hardcoded maze layout."""
        # Initialize empty grid
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        # Simple maze: walls around the border
        for y in range(self.height):
            for x in range(self.width):
                # Border walls
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.grid[y][x] = 1
                    
                # Add some internal walls for fun
                # Vertical walls
                elif x == 5 and (y < 8 or y > 10):
                    self.grid[y][x] = 1
                elif x == self.width - 6 and (y < 8 or y > 10):
                    self.grid[y][x] = 1
                    
                # Horizontal walls
                elif y == 5 and (x < 8 or x > self.width - 9):
                    self.grid[y][x] = 1
                elif y == self.height - 6 and (x < 8 or x > self.width - 9):
                    self.grid[y][x] = 1
        
        # Build wall collision rectangles
        self._build_wall_rectangles()
        
    def _build_wall_rectangles(self):
        """Build collision rectangles for all walls."""
        self.walls.clear()
        
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:  # Wall tile
                    # Calculate pixel position
                    wall_x = x * TILE_SIZE
                    wall_y = y * TILE_SIZE
                    
                    # Store as (left, bottom, width, height)
                    self.walls.append((
                        wall_x,
                        wall_y,
                        TILE_SIZE,
                        TILE_SIZE
                    ))
    
    def draw(self):
        """Draw the maze."""
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:  # Wall
                    # Calculate pixel position (bottom-left corner)
                    pixel_x = x * TILE_SIZE
                    pixel_y = y * TILE_SIZE
                    
                    # Draw wall as filled rectangle
                    # arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, color)
                    arcade.draw_lrbt_rectangle_filled(
                        pixel_x,
                        pixel_x + TILE_SIZE,
                        pixel_y,
                        pixel_y + TILE_SIZE,
                        COLOR_WALL
                    )
    
    def is_wall(self, tile_x: int, tile_y: int) -> bool:
        """
        Check if a tile position is a wall.
        
        Args:
            tile_x: X position in tiles
            tile_y: Y position in tiles
            
        Returns:
            True if the tile is a wall, False otherwise
        """
        # Check bounds
        if tile_x < 0 or tile_x >= self.width or tile_y < 0 or tile_y >= self.height:
            return True  # Out of bounds = wall
        
        return self.grid[tile_y][tile_x] == 1
    
    def is_wall_at_pixel(self, pixel_x: float, pixel_y: float) -> bool:
        """
        Check if a pixel position is inside a wall.
        
        Args:
            pixel_x: X position in pixels
            pixel_y: Y position in pixels
            
        Returns:
            True if position is in a wall, False otherwise
        """
        tile_x = int(pixel_x // TILE_SIZE)
        tile_y = int(pixel_y // TILE_SIZE)
        return self.is_wall(tile_x, tile_y)
    
    def get_tile_center(self, tile_x: int, tile_y: int) -> Tuple[float, float]:
        """
        Get the pixel center of a tile.
        
        Args:
            tile_x: X position in tiles
            tile_y: Y position in tiles
            
        Returns:
            Tuple of (pixel_x, pixel_y)
        """
        pixel_x = tile_x * TILE_SIZE + TILE_SIZE // 2
        pixel_y = tile_y * TILE_SIZE + TILE_SIZE // 2
        return pixel_x, pixel_y
