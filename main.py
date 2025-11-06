"""
Pacman-Style Game
=================
A modern implementation of classic Pacman game with custom modifications.
Created for junior.guru Discord community challenge.

Entry point for the game application.
"""

import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from pacman.game import PacmanGame


def main():
    """Main entry point for the game."""
    game = PacmanGame()
    game.run()


if __name__ == "__main__":
    main()
