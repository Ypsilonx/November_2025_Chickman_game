"""
Collectible items (seeds, super seeds, bonuses).
"""

import arcade
from typing import List
from pacman.utils.constants import (
    TILE_SIZE,
    COLOR_SEED,
    COLOR_SUPER_SEED,
    SEED_POINTS,
    SUPER_SEED_POINTS
)


class Seed:
    """
    Represents a small seed to collect.
    
    Attributes:
        x: X position in pixels
        y: Y position in pixels
        collected: Whether the seed has been collected
        points: Points awarded for collecting
    """
    
    def __init__(self, x: float, y: float):
        """
        Initialize a seed.
        
        Args:
            x: X position in pixels (center of tile)
            y: Y position in pixels (center of tile)
        """
        self.x = x
        self.y = y
        self.collected = False
        self.points = SEED_POINTS
        self.radius = 3  # Small seed
        
    def draw(self):
        """Draw the seed if not collected."""
        if not self.collected:
            arcade.draw_circle_filled(
                self.x,
                self.y,
                self.radius,
                COLOR_SEED
            )
    
    def check_collision(self, chicken_x: float, chicken_y: float, chicken_radius: float) -> bool:
        """
        Check if chicken collides with this seed.
        
        Args:
            chicken_x: Chicken X position
            chicken_y: Chicken Y position
            chicken_radius: Chicken collision radius
            
        Returns:
            True if collision detected and seed collected
        """
        if self.collected:
            return False
        
        # Simple distance check
        dx = self.x - chicken_x
        dy = self.y - chicken_y
        distance = (dx * dx + dy * dy) ** 0.5
        
        if distance < chicken_radius:
            self.collected = True
            return True
        
        return False


class SuperSeed(Seed):
    """
    Represents a super seed (larger seed that gives special power).
    """
    
    def __init__(self, x: float, y: float):
        """
        Initialize a super seed.
        
        Args:
            x: X position in pixels
            y: Y position in pixels
        """
        super().__init__(x, y)
        self.points = SUPER_SEED_POINTS
        self.radius = 8  # Larger than normal seed
        self.blink_timer = 0
        
    def draw(self):
        """Draw the super seed with blinking effect."""
        if not self.collected:
            # Blink effect - visible/invisible based on timer
            import time
            self.blink_timer = time.time()
            
            # Blink every 0.3 seconds (visible for 0.15s, hidden for 0.15s)
            if int(self.blink_timer * 3) % 2 == 0:
                arcade.draw_circle_filled(
                    self.x,
                    self.y,
                    self.radius,
                    COLOR_SUPER_SEED
                )


class SeedManager:
    """
    Manages all collectible seeds in the maze.
    """
    
    def __init__(self):
        """Initialize the seed manager."""
        self.seeds: List[Seed] = []
        self.super_seeds: List[SuperSeed] = []
        
    def _flood_fill_reachable(self, maze, start_x: int, start_y: int) -> set:
        """
        Use flood fill algorithm to find all reachable tiles from start position.
        
        Args:
            maze: The Maze object
            start_x: Starting tile X coordinate
            start_y: Starting tile Y coordinate
            
        Returns:
            Set of (x, y) tuples representing reachable tiles
        """
        reachable = set()
        to_visit = [(start_x, start_y)]
        
        while to_visit:
            x, y = to_visit.pop()
            
            # Skip if already visited or out of bounds
            if (x, y) in reachable:
                continue
            if x < 0 or x >= maze.width or y < 0 or y >= maze.height:
                continue
            
            # Skip if wall
            if maze.grid[y][x] == 1:
                continue
            
            # Mark as reachable
            reachable.add((x, y))
            
            # Add neighbors to visit (4-directional)
            to_visit.append((x + 1, y))  # Right
            to_visit.append((x - 1, y))  # Left
            to_visit.append((x, y + 1))  # Up
            to_visit.append((x, y - 1))  # Down
        
        return reachable
        
    def create_seeds_for_maze(self, maze, start_x: int = None, start_y: int = None):
        """
        Create seeds only for reachable spaces in the maze.
        Uses flood fill algorithm to detect reachable areas.
        
        Args:
            maze: The Maze object
            start_x: Starting tile X (defaults to center)
            start_y: Starting tile Y (defaults to center)
        """
        self.seeds.clear()
        self.super_seeds.clear()
        
        # Default start position is center of maze
        if start_x is None:
            start_x = maze.width // 2
        if start_y is None:
            start_y = maze.height // 2
        
        # Find all reachable tiles using flood fill
        print(f"🧠 Running flood fill from tile ({start_x}, {start_y})...")
        reachable_tiles = self._flood_fill_reachable(maze, start_x, start_y)
        print(f"✓ Found {len(reachable_tiles)} reachable tiles")
        
        # Find corner tiles for super seeds (furthest from center in each quadrant)
        corner_candidates = {
            'bottom_left': None,
            'bottom_right': None,
            'top_left': None,
            'top_right': None
        }
        
        center_x = maze.width // 2
        center_y = maze.height // 2
        
        # Find best corner in each quadrant
        for tile_x, tile_y in reachable_tiles:
            # Bottom-left quadrant
            if tile_x < center_x and tile_y < center_y:
                if corner_candidates['bottom_left'] is None:
                    corner_candidates['bottom_left'] = (tile_x, tile_y)
                else:
                    curr_x, curr_y = corner_candidates['bottom_left']
                    # Find tile furthest from center
                    if (tile_x + tile_y) < (curr_x + curr_y):
                        corner_candidates['bottom_left'] = (tile_x, tile_y)
            
            # Bottom-right quadrant
            elif tile_x >= center_x and tile_y < center_y:
                if corner_candidates['bottom_right'] is None:
                    corner_candidates['bottom_right'] = (tile_x, tile_y)
                else:
                    curr_x, curr_y = corner_candidates['bottom_right']
                    if (tile_x - tile_y) > (curr_x - curr_y):
                        corner_candidates['bottom_right'] = (tile_x, tile_y)
            
            # Top-left quadrant
            elif tile_x < center_x and tile_y >= center_y:
                if corner_candidates['top_left'] is None:
                    corner_candidates['top_left'] = (tile_x, tile_y)
                else:
                    curr_x, curr_y = corner_candidates['top_left']
                    if (tile_x - tile_y) < (curr_x - curr_y):
                        corner_candidates['top_left'] = (tile_x, tile_y)
            
            # Top-right quadrant
            else:  # tile_x >= center_x and tile_y >= center_y
                if corner_candidates['top_right'] is None:
                    corner_candidates['top_right'] = (tile_x, tile_y)
                else:
                    curr_x, curr_y = corner_candidates['top_right']
                    if (tile_x + tile_y) > (curr_x + curr_y):
                        corner_candidates['top_right'] = (tile_x, tile_y)
        
        # Store corner positions
        corner_positions = set()
        for corner_name, corner_pos in corner_candidates.items():
            if corner_pos is not None:
                corner_positions.add(corner_pos)
                print(f"  🌟 Super seed at {corner_name}: {corner_pos}")
        
        # Create seeds only on reachable tiles
        for tile_x, tile_y in reachable_tiles:
            # Calculate center of tile
            pixel_x = tile_x * TILE_SIZE + TILE_SIZE // 2
            pixel_y = tile_y * TILE_SIZE + TILE_SIZE // 2
            
            # Check if this is a corner position for super seed
            if (tile_x, tile_y) in corner_positions:
                self.super_seeds.append(SuperSeed(pixel_x, pixel_y))
            else:
                self.seeds.append(Seed(pixel_x, pixel_y))
        
        print(f"🌾 Created {len(self.seeds)} seeds and {len(self.super_seeds)} super seeds (only on reachable tiles)")
    
    def draw(self):
        """Draw all seeds and super seeds."""
        for seed in self.seeds:
            seed.draw()
        for super_seed in self.super_seeds:
            super_seed.draw()
    
    def check_collisions(self, chicken_x: float, chicken_y: float, chicken_radius: float) -> tuple[int, bool]:
        """
        Check collisions with chicken and return points earned.
        
        Args:
            chicken_x: Chicken X position
            chicken_y: Chicken Y position
            chicken_radius: Chicken collision radius
            
        Returns:
            Tuple of (points earned, ate_super_seed)
        """
        points = 0
        ate_super_seed = False
        
        # Check regular seeds
        for seed in self.seeds:
            if seed.check_collision(chicken_x, chicken_y, chicken_radius):
                points += seed.points
        
        # Check super seeds
        for super_seed in self.super_seeds:
            if super_seed.check_collision(chicken_x, chicken_y, chicken_radius):
                points += super_seed.points
                ate_super_seed = True
        
        return points, ate_super_seed
    
    def get_remaining_seeds(self) -> int:
        """
        Get count of uncollected seeds.
        
        Returns:
            Number of seeds not yet collected
        """
        count = sum(1 for seed in self.seeds if not seed.collected)
        count += sum(1 for super_seed in self.super_seeds if not super_seed.collected)
        return count
    
    def all_seeds_collected(self) -> bool:
        """
        Check if all seeds have been collected.
        
        Returns:
            True if all seeds collected
        """
        return self.get_remaining_seeds() == 0
