from setuptools import setup, find_packages

setup(
    name="pacman-game",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "arcade>=2.6.17",
        "pytmx>=3.31",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "isort>=5.12.0",
            "pylint>=2.17.5",
            "pre-commit>=3.3.3",
        ],
    },
    entry_points={
        "console_scripts": [
            "pacman=pacman.game:main",
        ],
    },
    python_requires=">=3.9",
)
