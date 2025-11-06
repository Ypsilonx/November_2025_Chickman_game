"""
Main game module.
Handles game initialization, main loop, and window management.
"""

import arcade
from pacman.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    FPS
)


class PacmanGame(arcade.Window):
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
        self.current_view = None
        
    def setup(self):
        """Set up the game. Called to initialize or restart the game."""
        # TODO: Initialize game views and switch to menu
        pass
    
    def run(self):
        """Start the game."""
        self.setup()
        arcade.run()


def main():
    """Entry point for the game."""
    game = PacmanGame()
    game.run()


if __name__ == "__main__":
    main()
