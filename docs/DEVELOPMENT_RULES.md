# 📐 Development Rules & Guidelines

**Verze:** 1.0  
**Projekt:** Pacman Game - Junior.guru Challenge  
**Účel:** Zajistit konzistentní, čistý a maintainovatelný kód

---

## 🎯 Cíle projektu

1. **Publikovatelnost** - Kód musí být GitHub-ready a profesionální
2. **Edukativnost** - Struktura musí být srozumitelná pro juniory
3. **Rozšiřitelnost** - Snadné přidávání nových funkcí
4. **Testovatelnost** - Vše musí jít otestovat
5. **Kvalita** - Maintainovatelný kód s dokumentací

---

## 📏 Kódovací standardy

### Python Style Guide

**Striktně dodržujeme PEP 8 s následujícími rozšířeními:**

#### Formátování

```python
# ✅ SPRÁVNĚ
class Player(arcade.Sprite):
    """
    Třída reprezentující hráče (Pacmana).
    
    Attributes:
        speed (float): Rychlost pohybu v pixelech za sekundu
        lives (int): Počet zbývajících životů
        score (int): Aktuální skóre hráče
    """
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.speed = PLAYER_SPEED
        self.lives = STARTING_LIVES
        self.score = 0
        self.setup_animations()
    
    def update(self, delta_time: float) -> None:
        """Aktualizuje stav hráče každý frame."""
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time

# ❌ ŠPATNĚ
class player:  # PascalCase pro třídy!
    def __init__(self,x,y):  # mezery po čárkách!
        self.Speed=5  # snake_case pro atributy!
```

#### Názvosloví

```python
# ✅ Třídy - PascalCase
class PowerPellet:
class GhostAI:
class LevelLoader:

# ✅ Funkce a metody - snake_case
def calculate_distance():
def load_level_from_file():
def check_collision_with_walls():

# ✅ Konstanty - UPPER_SNAKE_CASE
SCREEN_WIDTH = 800
MAX_LIVES = 5
GHOST_SCARED_TIME = 10.0

# ✅ Proměnné - snake_case
player_position = (x, y)
current_score = 0
is_game_over = False

# ❌ NEPOUŽÍVAT jednopísmenné proměnné (kromě iterátorů)
# Špatně:
for i in ghosts:
    g = ghosts[i]
    
# Dobře:
for ghost_id, ghost in enumerate(ghosts):
```

#### Type Hints

**POVINNÉ pro všechny funkce a metody:**

```python
from typing import List, Optional, Tuple, Dict

# ✅ SPRÁVNĚ
def calculate_path(
    start: Tuple[int, int],
    end: Tuple[int, int],
    obstacles: List[Tuple[int, int]]
) -> Optional[List[Tuple[int, int]]]:
    """
    Vypočítá cestu od startu do cíle.
    
    Args:
        start: Startovní pozice (x, y)
        end: Cílová pozice (x, y)
        obstacles: Seznam pozic překážek
        
    Returns:
        Seznam pozic tvořících cestu, nebo None pokud cesta neexistuje
    """
    pass

# ❌ ŠPATNĚ - chybí type hints
def calculate_path(start, end, obstacles):
    pass
```

#### Délka řádku

- **Maximum: 88 znaků** (Black default)
- Pro delší řádky použij lomení:

```python
# ✅ SPRÁVNĚ
result = some_function(
    very_long_parameter_name_one,
    very_long_parameter_name_two,
    very_long_parameter_name_three
)

# nebo
player_stats = {
    "name": "Pacman",
    "lives": 3,
    "score": 0,
}
```

---

## 📝 Dokumentace kódu

### Docstrings

**Každá třída, funkce a metoda musí mít docstring!**

#### Formát: Google Style

```python
def spawn_ghost(
    ghost_type: str,
    position: Tuple[int, int],
    difficulty: int = 1
) -> Ghost:
    """
    Vytvoří a vrátí novou instanci ducha.
    
    Tato funkce inicializuje ducha na zadané pozici s AI
    odpovídající typu ducha a obtížnosti.
    
    Args:
        ghost_type: Typ ducha ("blinky", "pinky", "inky", "clyde")
        position: Spawn pozice ducha (x, y) v tile souřadnicích
        difficulty: Úroveň obtížnosti 1-10, ovlivňuje rychlost
            a agresivitu AI (default: 1)
    
    Returns:
        Nová instance Ghost s nakonfigurovaným AI
    
    Raises:
        ValueError: Pokud ghost_type není validní typ ducha
        
    Example:
        >>> ghost = spawn_ghost("blinky", (10, 10), difficulty=3)
        >>> ghost.speed
        3.5
    """
    pass
```

### Komentáře v kódu

```python
# ✅ DOBRÉ komentáře - vysvětlují PROČ, ne CO

# Použijeme A* algoritmus místo BFS, protože potřebujeme
# nejkratší cestu v reálném čase s heuristikou
path = astar_pathfinding(start, end, heuristic=manhattan_distance)

# Duchové musí čekat 3 sekundy před opuštěním domečku
# aby měl hráč čas se zorientovat
if time_since_spawn < GHOST_SPAWN_DELAY:
    return

# ❌ ŠPATNÉ komentáře - opakují kód

# Inkrementuj skóre o 10
score += 10

# Nastav x na 0
x = 0
```

---

## 🏗️ Architektura a struktura

### Organizace modulů

```
src/pacman/
├── entities/           # Herní entity
│   ├── __init__.py
│   ├── base.py        # Abstraktní base třídy
│   ├── player.py      # Pacman
│   ├── ghost.py       # Duchové
│   ├── collectibles.py # Tečky, pellety, ovoce
│   └── ghost_ai.py    # AI logika pro duchy
│
├── maps/              # Mapy a level management
│   ├── __init__.py
│   ├── maze.py        # Reprezentace bludiště
│   ├── tile.py        # Jednotlivé dlaždice
│   └── level_loader.py # Načítání map ze souborů
│
├── ui/                # User interface
│   ├── __init__.py
│   ├── menu.py        # Hlavní menu
│   ├── hud.py         # HUD během hry
│   ├── pause.py       # Pause menu
│   └── game_over.py   # Game over screen
│
├── utils/             # Pomocné moduly
│   ├── __init__.py
│   ├── constants.py   # Konstanty a config
│   ├── helpers.py     # Helper funkce
│   └── pathfinding.py # A* a path algoritmy
│
├── assets/            # Assety (ne Python)
│   ├── sprites/
│   ├── sounds/
│   └── maps/
│
└── game.py           # Hlavní game class
```

### Dependency pravidla

```
1. entities/ může záviset na: utils/
2. maps/ může záviset na: utils/, entities/
3. ui/ může záviset na: utils/, entities/, maps/
4. game.py může záviset na všem
5. utils/ NESMÍ záviset na ničem kromě stdlib

❌ NIKDY circular imports!
```

### Class design principy

#### 1. Single Responsibility Principle

```python
# ✅ SPRÁVNĚ - každá třída má jednu odpovědnost

class Ghost(arcade.Sprite):
    """Reprezentuje ducha - pouze vizuální a fyzický stav."""
    pass

class GhostAI:
    """Řídí AI chování ducha."""
    pass

class GhostSpawner:
    """Spravuje spawn timing a pozice duchů."""
    pass

# ❌ ŠPATNĚ - třída dělá příliš mnoho

class Ghost(arcade.Sprite):
    """Dělá všechno - vizuál, AI, spawn, scoring..."""
    def update_ai(self): pass
    def spawn(self): pass
    def calculate_score(self): pass  # Too much!
```

#### 2. Composition over Inheritance

```python
# ✅ SPRÁVNĚ - použij composition

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.input_handler = InputHandler()
        self.animator = PlayerAnimator()
        self.collision_detector = CollisionDetector()

# ❌ ŠPATNĚ - deep inheritance

class Entity: pass
class MovableEntity(Entity): pass
class AnimatedEntity(MovableEntity): pass
class Player(AnimatedEntity): pass  # Too deep!
```

---

## 🧪 Testování

### Test Coverage cíl: 80%+

#### Co MUSÍ být otestováno:

1. **Entity logika**
   - Pohyb
   - Kolize
   - State changes

2. **Game mechaniky**
   - Skóre kalkulace
   - Level progrese
   - Power-up efekty

3. **AI systémy**
   - Pathfinding
   - Ghost strategie
   - Decision making

4. **Utility funkce**
   - Distance calculations
   - Tile conversions
   - Helper methods

#### Test struktura

```python
# tests/test_entities/test_player.py

import pytest
from pacman.entities.player import Player
from pacman.utils.constants import PLAYER_SPEED

class TestPlayer:
    """Test suite pro Player třídu."""
    
    @pytest.fixture
    def player(self):
        """Vytvoří player instanci pro testy."""
        return Player(x=100, y=100)
    
    def test_player_initialization(self, player):
        """Test správné inicializace hráče."""
        assert player.center_x == 100
        assert player.center_y == 100
        assert player.lives == 3
        assert player.score == 0
    
    def test_player_movement(self, player):
        """Test pohybu hráče."""
        player.change_x = PLAYER_SPEED
        player.update(delta_time=1.0)
        assert player.center_x == 100 + PLAYER_SPEED
    
    def test_player_collision_with_wall(self, player):
        """Test kolize hráče se zdí."""
        # Setup wall
        # Test collision
        # Assert player stopped
        pass
    
    @pytest.mark.parametrize("dots,expected_score", [
        (1, 10),
        (5, 50),
        (10, 100),
    ])
    def test_score_calculation(self, player, dots, expected_score):
        """Test výpočtu skóre za různý počet teček."""
        for _ in range(dots):
            player.collect_dot()
        assert player.score == expected_score
```

### Test Coverage commands

```bash
# Spusť všechny testy
pytest

# S coverage reportem
pytest --cov=src/pacman --cov-report=html --cov-report=term

# Spusť konkrétní test
pytest tests/test_entities/test_player.py::TestPlayer::test_player_movement

# S verbose výstupem
pytest -v

# Rychlý test (fail fast)
pytest -x
```

---

## 🔄 Git workflow

### Branch naming

```bash
# Feature branches
feature/player-movement
feature/ghost-ai-blinky
feature/power-pellet-system

# Bugfix branches
fix/collision-detection-bug
fix/memory-leak-sprites

# Documentation
docs/update-readme
docs/add-api-documentation

# Refactoring
refactor/entity-base-class
refactor/simplify-pathfinding
```

### Commit messages

**Format:** `<type>(<scope>): <subject>`

```bash
# ✅ DOBRÉ commit messages

feat(player): add diagonal movement support
fix(ghost): correct pathfinding in tight corners
docs(readme): update installation instructions
test(entities): add tests for collision detection
refactor(maze): simplify tile loading logic
style(all): format code with black
chore(deps): update arcade to 2.6.17

# ❌ ŠPATNÉ commit messages

update
fixed bug
changes
stuff
wip
```

### Pull Request proces

1. **Vytvoř feature branch** z `main`
2. **Implementuj** změny
3. **Přidej testy** pro novou funkcionalitu
4. **Zkontroluj linting**: `black`, `flake8`, `isort`
5. **Spusť testy**: `pytest`
6. **Update dokumentace** pokud je to potřeba
7. **Vytvoř PR** s jasným popisem
8. **Code review** - počkej na schválení
9. **Merge** po schválení

---

## ⚡ Performance guidelines

### Optimalizační pravidla

```python
# ✅ DOBŘE - efektivní sprite batching

# Použij SpriteList pro skupiny spritů
self.dot_list = arcade.SpriteList()
self.ghost_list = arcade.SpriteList()

# Jeden draw call pro všechny
self.dot_list.draw()
self.ghost_list.draw()

# ❌ ŠPATNĚ - individual sprite drawing

for dot in dots:
    dot.draw()  # Pomalé! Jeden draw call per sprite
```

### Memory management

```python
# ✅ DOBŘE - reuse objektů

class ParticlePool:
    """Pool partiklů pro reuse."""
    def __init__(self, size=100):
        self.particles = [Particle() for _ in range(size)]
        self.active = []
    
    def get_particle(self):
        if self.particles:
            p = self.particles.pop()
            self.active.append(p)
            return p
        return None

# ❌ ŠPATNĚ - constant allocation

def create_particle_effect():
    for _ in range(100):
        Particle()  # Nový objekt každý frame!
```

### Profiling

```bash
# Profile kódu
python -m cProfile -o output.prof main.py

# Vizualizace
snakeviz output.prof
```

---

## 📊 Metriky a monitoring

### Code Quality metriky

```bash
# Complexity check
radon cc src/pacman -a -nc

# Maintainability index
radon mi src/pacman -s

# Cílové hodnoty:
# - Cyclomatic Complexity: < 10
# - Maintainability Index: > 65
# - Test Coverage: > 80%
```

---

## 🚫 Co NEDĚLAT

### Anti-patterns

```python
# ❌ Magic numbers
if player.score > 10000:
    player.lives += 1

# ✅ Pojmenované konstanty
if player.score > EXTRA_LIFE_THRESHOLD:
    player.lives += 1

# ❌ God classes
class Game:
    def update_player(self): pass
    def update_ghosts(self): pass
    def draw_everything(self): pass
    def handle_collisions(self): pass
    def load_levels(self): pass
    def play_sounds(self): pass
    # Too much responsibility!

# ✅ Rozdělené odpovědnosti
class Game:
    def __init__(self):
        self.entity_manager = EntityManager()
        self.level_manager = LevelManager()
        self.audio_manager = AudioManager()

# ❌ Mutable default arguments
def create_ghost(position=[0, 0]):  # BUG!
    pass

# ✅ None default
def create_ghost(position=None):
    if position is None:
        position = [0, 0]
```

---

## 📚 Doporučené zdroje

### Knihy
- "Clean Code" - Robert C. Martin
- "Python Tricks" - Dan Bader
- "Fluent Python" - Luciano Ramalho

### Online
- [Real Python](https://realpython.com/)
- [Python Arcade Documentation](https://api.arcade.academy/)
- [PEP 8 Style Guide](https://pep8.org/)

### Tools
- **Black** - code formatter
- **isort** - import sorting
- **flake8** - linting
- **mypy** - type checking
- **pytest** - testing
- **coverage** - test coverage

---

## ✅ Checklist před commitem

```bash
- [ ] Kód je naformátován (black)
- [ ] Imports jsou seřazené (isort)
- [ ] Žádné linting errors (flake8)
- [ ] Type hints jsou správné (mypy)
- [ ] Všechny testy prošly (pytest)
- [ ] Coverage neklesl pod 80%
- [ ] Dokumentace je aktuální
- [ ] Commit message je descriptive
- [ ] Žádné TODO/FIXME v kódu
- [ ] No print() statements (use logging)
```

---

## 🎓 Pro začátečníky

### Když nevíš, zeptej se:

1. **GitHub Discussions** - pro obecné otázky
2. **Issues** - pro konkrétní problémy
3. **Discord junior.guru** - pro rychlou pomoc
4. **Code Review** - pro feedback na kód

### Dobrá first issue kritéria:

- 🟢 **good first issue** - jasně definované, malé
- 🟡 **help wanted** - potřebujeme pomoct
- 🔵 **documentation** - práce na docs
- 🟣 **enhancement** - nové featury

---

**Poslední aktualizace:** 6. listopadu 2025  
**Verze:** 1.0  
**Maintainer:** Junior.guru Community

---

*Tato pravidla jsou živý dokument. Pokud máš návrh na vylepšení, otevři issue nebo PR!*
