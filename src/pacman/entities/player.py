"""
Player entity (Chickman - the chicken).
Handles player movement, animation, and state.
"""

import arcade
from typing import Tuple
from pacman.utils.constants import (
    CHICKEN_SIZE,
    CHICKEN_SPEED,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TILE_SIZE
)


class Player:
    """
    Represents the player character (Chickman - the brave chicken).
    
    Attributes:
        center_x: X position in pixels
        center_y: Y position in pixels
        speed: Movement speed in pixels per frame
        direction: Current movement direction (0-3: right, up, left, down)
    """
    
    def __init__(self, x: float, y: float):
        """
        Initialize the player.
        
        Args:
            x: Starting x position in pixels
            y: Starting y position in pixels
        """
        # Position
        self.center_x = x
        self.center_y = y
        
        # Movement
        self.speed = CHICKEN_SPEED
        self.change_x = 0
        self.change_y = 0
        
        # Direction tracking (for animations later)
        # 0=right, 1=up, 2=left, 3=down
        self.direction = 0
        
        # Buffered direction for responsive controls
        # Allows player to queue next direction change
        self.next_direction = None  # Will store next desired direction
        
        # Size
        self.radius = CHICKEN_SIZE // 2
        
    def draw(self):
        """Draw the chicken as a yellow circle (placeholder for sprite)."""
        arcade.draw_circle_filled(
            self.center_x,
            self.center_y,
            self.radius,
            arcade.color.YELLOW
        )
        
    def update(self, maze=None):
        """
        Update player position based on movement.
        Called every frame.
        
        Args:
            maze: Optional Maze object for collision detection
        """
        # Try to apply buffered direction change if one exists
        if self.next_direction is not None and maze:
            next_change_x, next_change_y = self._direction_to_change(self.next_direction)
            
            # Test if we can move in the buffered direction
            test_x = self.center_x + next_change_x
            test_y = self.center_y + next_change_y
            
            if self._can_move_to(test_x, test_y, maze):
                # Apply the buffered direction
                self.change_x = next_change_x
                self.change_y = next_change_y
                self.direction = self.next_direction
                self.next_direction = None  # Clear buffer
        
        # Calculate new position
        new_x = self.center_x + self.change_x
        new_y = self.center_y + self.change_y
        
        # Check collision with walls if maze provided
        if maze:
            if self._can_move_to(new_x, new_y, maze):
                self.center_x = new_x
                self.center_y = new_y
        else:
            # No maze, just move freely
            self.center_x = new_x
            self.center_y = new_y
        
        # Keep player on screen (temporary boundary check)
        if self.center_x < self.radius:
            self.center_x = self.radius
        elif self.center_x > SCREEN_WIDTH - self.radius:
            self.center_x = SCREEN_WIDTH - self.radius
            
        if self.center_y < self.radius:
            self.center_y = self.radius
        elif self.center_y > SCREEN_HEIGHT - self.radius:
            self.center_y = SCREEN_HEIGHT - self.radius
    
    def _direction_to_change(self, direction: int) -> Tuple[float, float]:
        """
        Convert direction number to change_x, change_y.
        
        Args:
            direction: 0=right, 1=up, 2=left, 3=down
            
        Returns:
            Tuple of (change_x, change_y)
        """
        if direction == 0:  # Right
            return self.speed, 0
        elif direction == 1:  # Up
            return 0, self.speed
        elif direction == 2:  # Left
            return -self.speed, 0
        elif direction == 3:  # Down
            return 0, -self.speed
        return 0, 0
    
    def _can_move_to(self, x: float, y: float, maze) -> bool:
        """
        Check if player can move to position without hitting walls.
        
        Args:
            x: Target x position
            y: Target y position
            maze: Maze object
            
        Returns:
            True if movement is possible
        """
        import math
        
        # Check 8 points around the circle for faster collision detection
        num_points = 8
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            point_x = x + self.radius * math.cos(angle)
            point_y = y + self.radius * math.sin(angle)
            
            if maze.is_wall_at_pixel(point_x, point_y):
                return False
        
        return True
    
    def move_right(self):
        """Request moving right (buffered if can't immediately)."""
        # Try to move immediately if stopped
        if self.change_x == 0 and self.change_y == 0:
            self.change_x = self.speed
            self.change_y = 0
            self.direction = 0
        else:
            # Buffer the direction for next frame
            self.next_direction = 0
        
    def move_left(self):
        """Request moving left (buffered if can't immediately)."""
        if self.change_x == 0 and self.change_y == 0:
            self.change_x = -self.speed
            self.change_y = 0
            self.direction = 2
        else:
            self.next_direction = 2
        
    def move_up(self):
        """Request moving up (buffered if can't immediately)."""
        if self.change_x == 0 and self.change_y == 0:
            self.change_x = 0
            self.change_y = self.speed
            self.direction = 1
        else:
            self.next_direction = 1
        
    def move_down(self):
        """Request moving down (buffered if can't immediately)."""
        if self.change_x == 0 and self.change_y == 0:
            self.change_x = 0
            self.change_y = -self.speed
            self.direction = 3
        else:
            self.next_direction = 3
        
    def stop(self):
        """Stop all movement."""
        self.change_x = 0
        self.change_y = 0
    
    def get_tile_position(self) -> Tuple[int, int]:
        """
        Get player position in tile coordinates.
        
        Returns:
            Tuple of (tile_x, tile_y)
        """
        tile_x = int(self.center_x // TILE_SIZE)
        tile_y = int(self.center_y // TILE_SIZE)
        return tile_x, tile_y

