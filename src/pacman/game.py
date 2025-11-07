"""
Main game module.
Handles game initialization, main loop, and window management.
"""

import arcade
from pacman.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    FPS,
    TILE_SIZE,
    FOX_SCARED_TIME
)
from pacman.entities.player import Player
from pacman.maps.maze import Maze
from pacman.entities.collectibles import SeedManager
from pacman.entities.fox import FoxManager


class ChickmanGame(arcade.Window):
    """
    Main game class that manages the game window and states.
    
    Attributes:
        current_view: The currently active game view (menu, gameplay, etc.)
    """
    
    def __init__(self):
        """Initialize the game window."""
        super().__init__(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            SCREEN_TITLE,
            update_rate=1/FPS
        )
        
        arcade.set_background_color(arcade.color.BLACK)
        
        # Game state
        self.frame_count = 0
        self.game_started = False
        
        # Track pressed keys for smooth multi-key handling
        self.keys_pressed = set()
        
        # Chicken (player)
        self.player = None
        
        # Maze
        self.maze = None
        
        # Collectibles
        self.seed_manager = None
        
        # Foxes
        self.fox_manager = None
        
        # Score
        self.score = 0
        
        # Power mode (frightened ghosts)
        self.power_mode = False
        self.power_timer = 0.0
        
    def setup(self):
        """Set up the game. Called to initialize or restart the game."""
        print("🐔 Chickman Game initialized!")
        print(f"📐 Window size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        print(f"⚡ Target FPS: {FPS}")
        
        # Create maze
        self.maze = Maze()
        print(f"🧱 Maze created: {self.maze.width}x{self.maze.height} tiles")
        
        # Create chicken (player) in center of screen
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        print(f"� Chicken created at ({self.player.center_x}, {self.player.center_y})")
        
        # Create seeds (using flood fill from chicken's starting position)
        self.seed_manager = SeedManager()
        player_tile_x = int(self.player.center_x // TILE_SIZE)
        player_tile_y = int(self.player.center_y // TILE_SIZE)
        self.seed_manager.create_seeds_for_maze(self.maze, player_tile_x, player_tile_y)
        
        # Create foxes
        self.fox_manager = FoxManager()
        self.fox_manager.create_foxes(self.maze)
        
        # Reset score
        self.score = 0
        
        # Reset power mode
        self.power_mode = False
        self.power_timer = 0.0
        
    def on_draw(self):
        """
        Render the screen.
        Called automatically by Arcade at target FPS.
        """
        # Clear the screen
        self.clear()
        
        if not self.game_started:
            # Draw welcome screen
            arcade.draw_text(
                "CHICKMAN - Junior.guru Challenge",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 50,
                arcade.color.YELLOW,
                20,
                anchor_x="center"
            )
            
            arcade.draw_text(
                "Press SPACE to start...",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 50,
                arcade.color.WHITE,
                16,
                anchor_x="center"
            )
        else:
            # Draw maze first (background)
            if self.maze:
                self.maze.draw()
            
            # Draw seeds
            if self.seed_manager:
                self.seed_manager.draw()
            
            # Draw foxes
            if self.fox_manager:
                self.fox_manager.draw()
            
            # Draw chicken on top
            if self.player:
                self.player.draw()
            
            # Draw score (top-left)
            arcade.draw_text(
                f"SCORE: {self.score}",
                10,
                SCREEN_HEIGHT - 70,
                arcade.color.YELLOW,
                18,
                bold=True
            )
            
            # Draw remaining seeds count
            if self.seed_manager:
                remaining = self.seed_manager.get_remaining_seeds()
                arcade.draw_text(
                    f"Seeds: {remaining}",
                    10,
                    SCREEN_HEIGHT - 100,
                    arcade.color.WHITE,
                    14
                )
            
            # Draw power mode indicator
            if self.power_mode:
                arcade.draw_text(
                    f"💪 POWER MODE: {self.power_timer:.1f}s",
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT - 50,
                    arcade.color.YELLOW,
                    20,
                    bold=True,
                    anchor_x="center"
                )
            
            # Draw instructions
            arcade.draw_text(
                "Use Arrow Keys or WASD to move | ESC to quit",
                SCREEN_WIDTH // 2,
                20,
                arcade.color.WHITE,
                12,
                anchor_x="center"
            )
        
        # Draw FPS counter for debugging (top-left corner)
        arcade.draw_text(
            f"FPS: {int(arcade.get_fps())}",
            10,
            SCREEN_HEIGHT - 30,
            arcade.color.WHITE,
            14
        )
        
        # Draw player position for debugging
        if self.player and self.game_started:
            arcade.draw_text(
                f"Position: ({int(self.player.center_x)}, {int(self.player.center_y)})",
                10,
                SCREEN_HEIGHT - 60,
                arcade.color.WHITE,
                12
            )
    
    def on_update(self, delta_time: float):
        """
        Update game logic.
        Called automatically by Arcade at target FPS.
        
        Args:
            delta_time: Time elapsed since last update (in seconds)
        """
        self.frame_count += 1
        
        # Update power mode timer
        if self.power_mode:
            self.power_timer -= delta_time
            if self.power_timer <= 0:
                self.power_mode = False
                self.power_timer = 0.0
                print("⚡ Power mode ended!")
                # Set ghosts back to normal
                if self.ghost_manager:
                    self.ghost_manager.set_all_frightened(False)
        
        # Update player if game started
        if self.game_started and self.player:
            self.player.update(self.maze)  # Pass maze for collision detection
            
            # Update ghosts
            if self.ghost_manager:
                self.ghost_manager.update(self.maze, self.player.center_x, self.player.center_y)
                
                # Check ghost collisions
                colliding_ghosts = self.ghost_manager.check_collisions_with_player(
                    self.player.center_x,
                    self.player.center_y,
                    self.player.radius
                )
                
                for ghost in colliding_ghosts:
                    if ghost.state.value == "frightened":
                        # Eat the ghost
                        ghost.set_state(ghost.state.__class__["EATEN"])
                        self.score += 200
                        print(f"👻 Ate {ghost.name}! +200 points")
                    elif ghost.state.value != "eaten":
                        # Ghost caught chicken
                        print("💀 Game Over! Ghost caught the chicken!")
                        # TODO: Implement lives system
            
            # Check seed collisions
            if self.seed_manager:
                points_earned, ate_super_seed = self.seed_manager.check_collisions(
                    self.player.center_x,
                    self.player.center_y,
                    self.player.radius
                )
                
                if points_earned > 0:
                    self.score += points_earned
                    print(f"� +{points_earned} points! Total: {self.score}")
                
                # Activate power mode if ate super seed
                if ate_super_seed:
                    self.power_mode = True
                    self.power_timer = FOX_SCARED_TIME
                    print(f"💪 SUPER SEED! Foxes frightened! ({FOX_SCARED_TIME}s)")
                    # Set all foxes to frightened
                    if self.fox_manager:
                        self.fox_manager.set_all_frightened(True)
                
                # Check if level completed
                if self.seed_manager.all_seeds_collected():
                    print("🎉 Level Complete! All seeds collected!")
                    # TODO: Load next level
        
        # DEBUG: Print every 60 frames (roughly 1 second)
        if self.frame_count % 60 == 0:
            print(f"✓ Game running... Frame: {self.frame_count}, FPS: {int(arcade.get_fps())}")
    
    def on_key_press(self, key: int, modifiers: int):
        """
        Handle key press events.
        
        Args:
            key: The key that was pressed
            modifiers: Modifier keys (shift, ctrl, etc.)
        """
        if key == arcade.key.ESCAPE:
            print("👋 Exiting game...")
            self.close()
        elif key == arcade.key.SPACE and not self.game_started:
            print("🚀 Game started!")
            self.game_started = True
        
        # Movement controls (only if game started)
        if self.game_started and self.player:
            # Add key to pressed keys set
            if key in [
                arcade.key.UP, arcade.key.DOWN, 
                arcade.key.LEFT, arcade.key.RIGHT,
                arcade.key.W, arcade.key.S, 
                arcade.key.A, arcade.key.D
            ]:
                self.keys_pressed.add(key)
            
            # Arrow keys
            if key == arcade.key.UP:
                self.player.move_up()
                print("⬆️ Moving UP")
            elif key == arcade.key.DOWN:
                self.player.move_down()
                print("⬇️ Moving DOWN")
            elif key == arcade.key.LEFT:
                self.player.move_left()
                print("⬅️ Moving LEFT")
            elif key == arcade.key.RIGHT:
                self.player.move_right()
                print("➡️ Moving RIGHT")
            
            # WASD keys
            elif key == arcade.key.W:
                self.player.move_up()
                print("⬆️ Moving UP (W)")
            elif key == arcade.key.S:
                self.player.move_down()
                print("⬇️ Moving DOWN (S)")
            elif key == arcade.key.A:
                self.player.move_left()
                print("⬅️ Moving LEFT (A)")
            elif key == arcade.key.D:
                self.player.move_right()
                print("➡️ Moving RIGHT (D)")
    
    def on_key_release(self, key: int, modifiers: int):
        """
        Handle key release events.
        
        Args:
            key: The key that was released
            modifiers: Modifier keys (shift, ctrl, etc.)
        """
        # Remove key from pressed keys
        if key in self.keys_pressed:
            self.keys_pressed.discard(key)
        
        # Stop player ONLY if no movement keys are pressed
        if self.game_started and self.player:
            if key in [
                arcade.key.UP, arcade.key.DOWN, 
                arcade.key.LEFT, arcade.key.RIGHT,
                arcade.key.W, arcade.key.S, 
                arcade.key.A, arcade.key.D
            ]:
                # Check if any other movement key is still pressed
                movement_keys = {
                    arcade.key.UP, arcade.key.DOWN,
                    arcade.key.LEFT, arcade.key.RIGHT,
                    arcade.key.W, arcade.key.S,
                    arcade.key.A, arcade.key.D
                }
                
                still_pressed = self.keys_pressed & movement_keys
                
                if not still_pressed:
                    # No movement keys pressed - stop
                    self.player.stop()
                    print("🛑 Stopped")
                else:
                    # Another key is still pressed - apply its direction
                    last_key = list(still_pressed)[-1]  # Get last pressed key
                    
                    if last_key == arcade.key.UP or last_key == arcade.key.W:
                        self.player.move_up()
                        print("⬆️ Continue UP")
                    elif last_key == arcade.key.DOWN or last_key == arcade.key.S:
                        self.player.move_down()
                        print("⬇️ Continue DOWN")
                    elif last_key == arcade.key.LEFT or last_key == arcade.key.A:
                        self.player.move_left()
                        print("⬅️ Continue LEFT")
                    elif last_key == arcade.key.RIGHT or last_key == arcade.key.D:
                        self.player.move_right()
                        print("➡️ Continue RIGHT")
    
    def run(self):
        """Start the game."""
        self.setup()
        arcade.run()


def main():
    """Entry point for the game."""
    game = ChickmanGame()
    game.run()


if __name__ == "__main__":
    main()
