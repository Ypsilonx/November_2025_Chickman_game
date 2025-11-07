"""
Ghost entities and AI.
Handles ghost behavior, pathfinding, and states.
"""

import arcade
import random
from enum import Enum
from typing import Tuple, List
from pacman.utils.constants import (
    TILE_SIZE,
    GHOST_SPEED,
    GHOST_SCARED_SPEED,
    COLOR_GHOST_SCARED,
    COLOR_GHOST_BLINKY,
    COLOR_GHOST_PINKY,
    COLOR_GHOST_INKY,
    COLOR_GHOST_CLYDE
)


class GhostState(Enum):
    """Ghost AI states."""
    CHASE = "chase"       # Actively hunting player
    SCATTER = "scatter"   # Moving to home corner
    FRIGHTENED = "frightened"  # Running away (blue)
    EATEN = "eaten"       # Returning to spawn after being eaten


class Ghost:
    """
    Base ghost class with AI and pathfinding.
    
    Attributes:
        center_x: X position in pixels
        center_y: Y position in pixels
        name: Ghost name (Blinky, Pinky, Inky, Clyde)
        color: Ghost color
        state: Current AI state
    """
    
    def __init__(self, x: float, y: float, name: str, color: Tuple[int, int, int]):
        """
        Initialize a ghost.
        
        Args:
            x: Starting x position in pixels
            y: Starting y position in pixels
            name: Ghost name
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
        self.speed = GHOST_SPEED
        self.change_x = 0
        self.change_y = 0
        self.direction = 0  # 0=right, 1=up, 2=left, 3=down
        
        # AI State
        self.state = GhostState.SCATTER
        
        # Size
        self.radius = 14
        
        # Spawn point (for returning after eaten)
        self.spawn_x = x
        self.spawn_y = y
        
        # Target tile for pathfinding
        self.target_tile_x = 0
        self.target_tile_y = 0
        
    def draw(self):
        """Draw the ghost."""
        # Use scared color if frightened, otherwise base color
        if self.state == GhostState.FRIGHTENED:
            draw_color = COLOR_GHOST_SCARED
        elif self.state == GhostState.EATEN:
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
        
        # Draw ghost body (circle for now)
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
    
    def update(self, maze, player_x: float, player_y: float):
        """
        Update ghost AI and position.
        
        Args:
            maze: The Maze object
            player_x: Player X position
            player_y: Player Y position
        """
        # Adjust speed based on state
        if self.state == GhostState.FRIGHTENED:
            current_speed = GHOST_SCARED_SPEED
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
        Check if ghost can move to position.
        
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
        Check if ghost is at an intersection (can turn).
        
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
    
    def set_state(self, new_state: GhostState):
        """
        Change ghost state.
        
        Args:
            new_state: New GhostState
        """
        self.state = new_state
        
        # Adjust speed based on new state
        if new_state == GhostState.FRIGHTENED:
            self.speed = GHOST_SCARED_SPEED
        else:
            self.speed = GHOST_SPEED
    
    def check_collision_with_player(self, player_x: float, player_y: float, player_radius: float) -> bool:
        """
        Check if ghost collides with player.
        
        Args:
            player_x: Player X position
            player_y: Player Y position
            player_radius: Player collision radius
            
        Returns:
            True if collision detected
        """
        dx = self.center_x - player_x
        dy = self.center_y - player_y
        distance = (dx * dx + dy * dy) ** 0.5
        
        return distance < (self.radius + player_radius)
    
    def get_tile_position(self) -> Tuple[int, int]:
        """
        Get ghost position in tile coordinates.
        
        Returns:
            Tuple of (tile_x, tile_y)
        """
        tile_x = int(self.center_x // TILE_SIZE)
        tile_y = int(self.center_y // TILE_SIZE)
        return tile_x, tile_y


class GhostManager:
    """
    Manages all ghosts in the game.
    """
    
    def __init__(self):
        """Initialize the ghost manager."""
        self.ghosts: List[Ghost] = []
    
    def create_ghosts(self, maze):
        """
        Create all 4 ghosts at spawn points.
        
        Args:
            maze: The Maze object
        """
        self.ghosts.clear()
        
        # Calculate center spawn position
        spawn_x = maze.width // 2 * TILE_SIZE + TILE_SIZE // 2
        spawn_y = maze.height // 2 * TILE_SIZE + TILE_SIZE // 2
        
        # Create 4 ghosts with different colors
        self.ghosts.append(Ghost(spawn_x, spawn_y + TILE_SIZE * 2, "Blinky", COLOR_GHOST_BLINKY))
        self.ghosts.append(Ghost(spawn_x - TILE_SIZE, spawn_y, "Pinky", COLOR_GHOST_PINKY))
        self.ghosts.append(Ghost(spawn_x + TILE_SIZE, spawn_y, "Inky", COLOR_GHOST_INKY))
        self.ghosts.append(Ghost(spawn_x, spawn_y - TILE_SIZE, "Clyde", COLOR_GHOST_CLYDE))
        
        print(f"👻 Created {len(self.ghosts)} ghosts at spawn")
    
    def update(self, maze, player_x: float, player_y: float):
        """
        Update all ghosts.
        
        Args:
            maze: The Maze object
            player_x: Player X position
            player_y: Player Y position
        """
        for ghost in self.ghosts:
            ghost.update(maze, player_x, player_y)
    
    def draw(self):
        """Draw all ghosts."""
        for ghost in self.ghosts:
            ghost.draw()
    
    def set_all_frightened(self, frightened: bool):
        """
        Set all ghosts to frightened or normal state.
        
        Args:
            frightened: True to frighten all ghosts
        """
        for ghost in self.ghosts:
            if frightened:
                ghost.set_state(GhostState.FRIGHTENED)
            else:
                # Return to chase or scatter (for now just chase)
                ghost.set_state(GhostState.CHASE)
    
    def check_collisions_with_player(self, player_x: float, player_y: float, player_radius: float) -> List[Ghost]:
        """
        Check which ghosts collide with player.
        
        Args:
            player_x: Player X position
            player_y: Player Y position
            player_radius: Player collision radius
            
        Returns:
            List of ghosts that collided
        """
        colliding_ghosts = []
        
        for ghost in self.ghosts:
            if ghost.check_collision_with_player(player_x, player_y, player_radius):
                colliding_ghosts.append(ghost)
        
        return colliding_ghosts
