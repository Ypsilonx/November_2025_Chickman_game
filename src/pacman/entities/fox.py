"""
Fox entities and AI.
Handles fox behavior, pathfinding, and states.
"""

import arcade
import random
from enum import Enum
from typing import Tuple, List
from pacman.utils.constants import (
    TILE_SIZE,
    FOX_SPEED,
    FOX_SCARED_SPEED,
    FOX_SIZE,
    COLOR_FOX_SCARED,
    COLOR_FOX_RUSTY,
    COLOR_FOX_GINGER,
    COLOR_FOX_COPPER,
    COLOR_FOX_AMBER
)


class FoxState(Enum):
    """Fox AI states."""
    CHASE = "chase"       # Actively hunting chicken
    SCATTER = "scatter"   # Moving to home corner
    FRIGHTENED = "frightened"  # Running away (blue)
    EATEN = "eaten"       # Returning to spawn after being eaten


class Fox:
    """
    Base fox class with AI and pathfinding.
    
    Attributes:
        center_x: X position in pixels
        center_y: Y position in pixels
        name: Fox name (Rusty, Ginger, Copper, Amber)
        color: Fox color
        state: Current AI state
    """
    
    def __init__(self, x: float, y: float, name: str, color: Tuple[int, int, int]):
        """
        Initialize a fox.
        
        Args:
            x: Starting x position in pixels
            y: Starting y position in pixels
            name: Fox name
            color: RGB color tuple
        """
        # Position
        self.center_x = x
        self.center_y = y
        
        # Identity
        self.name = name
        self.base_color = color
        self.color = color
        
        # Movement
        self.speed = FOX_SPEED
        self.change_x = 0
        self.change_y = 0
        self.direction = 0  # 0=right, 1=up, 2=left, 3=down
        
        # AI State
        self.state = FoxState.SCATTER
        
        # Size
        self.radius = FOX_SIZE // 2
        
        # Spawn point (for returning after eaten)
        self.spawn_x = x
        self.spawn_y = y
        
        # Target tile for pathfinding
        self.target_tile_x = 0
        self.target_tile_y = 0
        
    def draw(self):
        """Draw the fox."""
        # Use scared color if frightened, otherwise base color
        if self.state == FoxState.FRIGHTENED:
            draw_color = COLOR_FOX_SCARED
        elif self.state == FoxState.EATEN:
            # Draw as eyes only (white circles)
            arcade.draw_circle_filled(
                self.center_x - 5,
                self.center_y + 3,
                3,
                arcade.color.WHITE
            )
            arcade.draw_circle_filled(
                self.center_x + 5,
                self.center_y + 3,
                3,
                arcade.color.WHITE
            )
            return
        else:
            draw_color = self.base_color
        
        # Draw fox body (circle for now)
        arcade.draw_circle_filled(
            self.center_x,
            self.center_y,
            self.radius,
            draw_color
        )
        
        # Draw eyes
        arcade.draw_circle_filled(
            self.center_x - 5,
            self.center_y + 3,
            3,
            arcade.color.WHITE
        )
        arcade.draw_circle_filled(
            self.center_x + 5,
            self.center_y + 3,
            3,
            arcade.color.WHITE
        )
        
        # Draw pupils based on direction
        pupil_offset = 2
        if self.direction == 0:  # Right
            pupil_x_offset = pupil_offset
            pupil_y_offset = 0
        elif self.direction == 1:  # Up
            pupil_x_offset = 0
            pupil_y_offset = pupil_offset
        elif self.direction == 2:  # Left
            pupil_x_offset = -pupil_offset
            pupil_y_offset = 0
        else:  # Down
            pupil_x_offset = 0
            pupil_y_offset = -pupil_offset
        
        arcade.draw_circle_filled(
            self.center_x - 5 + pupil_x_offset,
            self.center_y + 3 + pupil_y_offset,
            2,
            arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            self.center_x + 5 + pupil_x_offset,
            self.center_y + 3 + pupil_y_offset,
            2,
            arcade.color.BLACK
        )
    
    def update(self, maze, chicken_x: float, chicken_y: float):
        """
        Update fox AI and position.
        
        Args:
            maze: The Maze object
            chicken_x: Chicken X position
            chicken_y: Chicken Y position
        """
        # Adjust speed based on state
        if self.state == FoxState.FRIGHTENED:
            current_speed = FOX_SCARED_SPEED
        else:
            current_speed = self.speed
        
        # Simple AI for now - just move randomly at intersections
        # TODO: Implement proper pathfinding
        self._simple_movement(maze, current_speed)
        
    def _simple_movement(self, maze, speed: float):
        """
        Simple movement AI - changes direction randomly at intersections.
        
        Args:
            maze: The Maze object
            speed: Current movement speed
        """
        # Calculate new position
        new_x = self.center_x + self.change_x
        new_y = self.center_y + self.change_y
        
        # Check if we can continue in current direction
        if self._can_move_to(new_x, new_y, maze):
            self.center_x = new_x
            self.center_y = new_y
        else:
            # Hit a wall, choose new direction
            self._choose_new_direction(maze, speed)
        
        # At intersections, randomly change direction
        if self._is_at_intersection(maze) and random.random() < 0.1:
            self._choose_new_direction(maze, speed)
    
    def _can_move_to(self, x: float, y: float, maze) -> bool:
        """
        Check if fox can move to position.
        
        Args:
            x: Target x position
            y: Target y position
            maze: Maze object
            
        Returns:
            True if movement is possible
        """
        import math
        
        # Check 4 points around the circle
        num_points = 4
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            point_x = x + self.radius * math.cos(angle)
            point_y = y + self.radius * math.sin(angle)
            
            if maze.is_wall_at_pixel(point_x, point_y):
                return False
        
        return True
    
    def _is_at_intersection(self, maze) -> bool:
        """
        Check if fox is at an intersection (can turn).
        
        Args:
            maze: Maze object
            
        Returns:
            True if at intersection
        """
        tile_x = int(self.center_x // TILE_SIZE)
        tile_y = int(self.center_y // TILE_SIZE)
        
        # Check how many directions are open
        open_directions = 0
        
        # Check all 4 directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if not maze.is_wall(tile_x + dx, tile_y + dy):
                open_directions += 1
        
        # Intersection if more than 2 directions are open
        return open_directions > 2
    
    def _choose_new_direction(self, maze, speed: float):
        """
        Choose a new valid direction to move.
        
        Args:
            maze: Maze object
            speed: Movement speed
        """
        tile_x = int(self.center_x // TILE_SIZE)
        tile_y = int(self.center_y // TILE_SIZE)
        
        # Get all valid directions
        valid_directions = []
        
        # Right
        if not maze.is_wall(tile_x + 1, tile_y):
            valid_directions.append((speed, 0, 0))
        # Left
        if not maze.is_wall(tile_x - 1, tile_y):
            valid_directions.append((-speed, 0, 2))
        # Up
        if not maze.is_wall(tile_x, tile_y + 1):
            valid_directions.append((0, speed, 1))
        # Down
        if not maze.is_wall(tile_x, tile_y - 1):
            valid_directions.append((0, -speed, 3))
        
        # Choose random valid direction
        if valid_directions:
            self.change_x, self.change_y, self.direction = random.choice(valid_directions)
    
    def set_state(self, new_state: FoxState):
        """
        Change fox state.
        
        Args:
            new_state: New FoxState
        """
        self.state = new_state
        
        # Adjust speed based on new state
        if new_state == FoxState.FRIGHTENED:
            self.speed = FOX_SCARED_SPEED
        else:
            self.speed = FOX_SPEED
    
    def check_collision_with_chicken(self, chicken_x: float, chicken_y: float, chicken_radius: float) -> bool:
        """
        Check if fox collides with chicken.
        
        Args:
            chicken_x: Chicken X position
            chicken_y: Chicken Y position
            chicken_radius: Chicken collision radius
            
        Returns:
            True if collision detected
        """
        dx = self.center_x - chicken_x
        dy = self.center_y - chicken_y
        distance = (dx * dx + dy * dy) ** 0.5
        
        return distance < (self.radius + chicken_radius)
    
    def get_tile_position(self) -> Tuple[int, int]:
        """
        Get fox position in tile coordinates.
        
        Returns:
            Tuple of (tile_x, tile_y)
        """
        tile_x = int(self.center_x // TILE_SIZE)
        tile_y = int(self.center_y // TILE_SIZE)
        return tile_x, tile_y


class FoxManager:
    """
    Manages all foxes in the game.
    """
    
    def __init__(self):
        """Initialize the fox manager."""
        self.foxes: List[Fox] = []
    
    def create_foxes(self, maze):
        """
        Create all 4 foxes at spawn points.
        
        Args:
            maze: The Maze object
        """
        self.foxes.clear()
        
        # Calculate center spawn position
        spawn_x = maze.width // 2 * TILE_SIZE + TILE_SIZE // 2
        spawn_y = maze.height // 2 * TILE_SIZE + TILE_SIZE // 2
        
        # Create 4 foxes with different colors and names
        self.foxes.append(Fox(spawn_x, spawn_y + TILE_SIZE * 2, "Rusty", COLOR_FOX_RUSTY))
        self.foxes.append(Fox(spawn_x - TILE_SIZE, spawn_y, "Ginger", COLOR_FOX_GINGER))
        self.foxes.append(Fox(spawn_x + TILE_SIZE, spawn_y, "Copper", COLOR_FOX_COPPER))
        self.foxes.append(Fox(spawn_x, spawn_y - TILE_SIZE, "Amber", COLOR_FOX_AMBER))
        
        print(f"🦊 Created {len(self.foxes)} foxes at spawn")
    
    def update(self, maze, chicken_x: float, chicken_y: float):
        """
        Update all foxes.
        
        Args:
            maze: The Maze object
            chicken_x: Chicken X position
            chicken_y: Chicken Y position
        """
        for fox in self.foxes:
            fox.update(maze, chicken_x, chicken_y)
    
    def draw(self):
        """Draw all foxes."""
        for fox in self.foxes:
            fox.draw()
    
    def set_all_frightened(self, frightened: bool):
        """
        Set all foxes to frightened or normal state.
        
        Args:
            frightened: True to frighten all foxes
        """
        for fox in self.foxes:
            if frightened:
                fox.set_state(FoxState.FRIGHTENED)
            else:
                # Return to chase or scatter (for now just chase)
                fox.set_state(FoxState.CHASE)
    
    def check_collisions_with_chicken(self, chicken_x: float, chicken_y: float, chicken_radius: float) -> List[Fox]:
        """
        Check which foxes collide with chicken.
        
        Args:
            chicken_x: Chicken X position
            chicken_y: Chicken Y position
            chicken_radius: Chicken collision radius
            
        Returns:
            List of foxes that collided
        """
        colliding_foxes = []
        
        for fox in self.foxes:
            if fox.check_collision_with_chicken(chicken_x, chicken_y, chicken_radius):
                colliding_foxes.append(fox)
        
        return colliding_foxes
