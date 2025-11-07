"""
Basic smoke test to verify Chickman project structure.
"""

import sys
from pathlib import Path


def test_imports():
    """Test that all main modules can be imported."""
    try:
        import pacman
        from pacman import utils
        from pacman.utils import constants
        assert pacman.__version__ == "0.1.0"
        assert constants.SCREEN_WIDTH == 1024
    except ImportError as e:
        assert False, f"Import failed: {e}"


def test_project_structure():
    """Test that all required directories exist."""
    project_root = Path(__file__).parent.parent
    
    required_dirs = [
        "src/pacman",
        "src/pacman/entities",
        "src/pacman/maps",
        "src/pacman/ui",
        "src/pacman/utils",
        "src/pacman/assets",
        "tests",
        "docs",
    ]
    
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        assert full_path.exists(), f"Directory {dir_path} does not exist"


def test_required_files():
    """Test that all required files exist."""
    project_root = Path(__file__).parent.parent
    
    required_files = [
        "README.md",
        "LICENSE",
        "requirements.txt",
        "pyproject.toml",
        ".gitignore",
        "main.py",
        "src/pacman/__init__.py",
        "src/pacman/game.py",
        "src/pacman/utils/constants.py",
    ]
    
    for file_path in required_files:
        full_path = project_root / file_path
        assert full_path.exists(), f"File {file_path} does not exist"


def test_constants_values():
    """Test that Chickman constants are properly defined."""
    from pacman.utils.constants import (
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN_TITLE,
        FPS,
        TILE_SIZE,
        CHICKEN_SPEED,
        STARTING_LIVES,
    )
    
    # Verify types and reasonable values
    assert isinstance(SCREEN_WIDTH, int) and SCREEN_WIDTH > 0
    assert isinstance(SCREEN_HEIGHT, int) and SCREEN_HEIGHT > 0
    assert isinstance(SCREEN_TITLE, str) and len(SCREEN_TITLE) > 0
    assert isinstance(FPS, int) and FPS > 0
    assert isinstance(TILE_SIZE, int) and TILE_SIZE > 0
    assert isinstance(CHICKEN_SPEED, (int, float)) and CHICKEN_SPEED > 0
    assert isinstance(STARTING_LIVES, int) and STARTING_LIVES > 0
