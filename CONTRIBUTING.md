# Přispívání do Pacman Game

Děkujeme za zájem o přispění do tohoto projektu! 🎉

## 📋 Obsah

- [Code of Conduct](#code-of-conduct)
- [Jak přispět](#jak-přispět)
- [Vývojové workflow](#vývojové-workflow)
- [Kódovací standardy](#kódovací-standardy)
- [Reportování bugů](#reportování-bugů)
- [Navrhování nových funkcí](#navrhování-nových-funkcí)

## Code of Conduct

Tento projekt dodržuje [Code of Conduct](CODE_OF_CONDUCT.md). Účastí souhlasíte s dodržováním těchto pravidel.

## Jak přispět

### 1. Fork a Clone

```bash
# Fork repozitář přes GitHub UI
# Pak naklonuj svůj fork
git clone https://github.com/TVŮJ_USERNAME/pacman-game.git
cd pacman-game
```

### 2. Vytvoř Branch

```bash
git checkout -b feature/tvoje-nova-funkcnost
# nebo
git checkout -b fix/oprava-bugu
```

Konvence názvů branchí:
- `feature/` - nové funkce
- `fix/` - opravy bugů
- `docs/` - změny v dokumentaci
- `refactor/` - refaktoring kódu
- `test/` - přidání testů

### 3. Nastav vývojové prostředí

```bash
# Vytvoř virtuální prostředí
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Nainstaluj závislosti včetně dev nástrojů
pip install -r requirements.txt
pip install -e ".[dev]"

# Nastav pre-commit hooks
pre-commit install
```

### 4. Proveď změny

- Piš čistý, čitelný kód
- Dodržuj [kódovací standardy](#kódovací-standardy)
- Přidej testy pro nové funkce
- Aktualizuj dokumentaci

### 5. Testuj

```bash
# Spusť všechny testy
pytest

# S pokrytím
pytest --cov=src/pacman --cov-report=html

# Spusť linting
flake8 src/ tests/
black --check src/ tests/
isort --check-only src/ tests/
mypy src/
```

### 6. Commit

```bash
git add .
git commit -m "feat: přidání XYZ funkce"
```

Konvence commit zpráv:
- `feat:` - nová funkce
- `fix:` - oprava bugu
- `docs:` - změny v dokumentaci
- `style:` - formátování, chybějící středníky, atd.
- `refactor:` - refaktoring kódu
- `test:` - přidání testů
- `chore:` - údržba, aktualizace závislostí

### 7. Push a Pull Request

```bash
git push origin feature/tvoje-nova-funkcnost
```

Pak vytvoř Pull Request na GitHubu s:
- Jasným popisem změn
- Referencemi na související issues (#123)
- Screenshots pro UI změny
- Potvrzení, že testy prošly

## Vývojové workflow

### Struktura kódu

```
src/pacman/
├── entities/      # Herní entity (player, ghost, etc.)
├── maps/          # Bludiště a level loading
├── ui/            # UI komponenty
├── utils/         # Pomocné funkce
└── game.py        # Hlavní game loop
```

### Přidání nové entity

1. Vytvoř soubor v `src/pacman/entities/`
2. Zděď z `arcade.Sprite` nebo vlastní base class
3. Implementuj potřebné metody (`update()`, `on_collision()`, atd.)
4. Přidej testy do `tests/test_entities/`
5. Aktualizuj dokumentaci

### Přidání nové mapy

1. Vytvoř TMX soubor v `src/pacman/assets/maps/`
2. Přidej loader do `maps/level_loader.py`
3. Přidej testy pro načítání mapy
4. Dokumentuj nové map features

## Kódovací standardy

### Python Style Guide

Dodržujeme **PEP 8** s těmito rozšířeními:

```python
# Maximální délka řádku: 88 (Black default)
# Uvozovky: dvojité " (Black preference)
# Imports: seřazené pomocí isort

# ✅ Dobrý příklad
class Ghost(arcade.Sprite):
    """
    Představuje ducha v bludišti.
    
    Attributes:
        speed: Rychlost ducha
        state: Aktuální stav (chase, scatter, frightened)
    """
    
    def __init__(self, color: str, spawn_x: float, spawn_y: float):
        super().__init__()
        self.speed = GHOST_SPEED
        self.color = color
        
    def update(self, delta_time: float) -> None:
        """Aktualizuje pozici ducha."""
        # Implementation
        pass
```

### Type Hints

Používáme type hints pro lepší čitelnost:

```python
from typing import List, Optional, Tuple

def calculate_path(
    start: Tuple[int, int],
    end: Tuple[int, int],
    obstacles: List[Tuple[int, int]]
) -> Optional[List[Tuple[int, int]]]:
    """Vypočítá cestu od start do end."""
    pass
```

### Dokumentace

- Každá třída musí mít docstring
- Veřejné metody musí mít docstring
- Používej Google style docstrings

```python
def power_pellet_collected(self, player: Player) -> int:
    """
    Zpracuje sebrání power pelletu.
    
    Args:
        player: Instance hráče, který sebral pellet
        
    Returns:
        Počet bodů získaných za pellet
        
    Raises:
        ValueError: Pokud player není validní instance
    """
    pass
```

## Reportování bugů

### Před reportováním

1. Zkontroluj [existující issues](https://github.com/yourusername/pacman-game/issues)
2. Ujisti se, že používáš nejnovější verzi
3. Zkus reprodukovat bug

### Vytvoření bug reportu

Použij [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md) a zahrň:

- **Popis**: Jasný popis problému
- **Kroky k reprodukci**: 1. Krok 1, 2. Krok 2, atd.
- **Očekávané chování**: Co by se mělo stát
- **Skutečné chování**: Co se stalo
- **Screenshots**: Pokud je to možné
- **Prostředí**:
  - OS: [např. Windows 11]
  - Python verze: [např. 3.11.0]
  - Arcade verze: [např. 2.6.17]

## Navrhování nových funkcí

### Feature Request

Použij [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md) a zahrň:

- **Problém**: Jaký problém tato funkce řeší?
- **Navrhované řešení**: Jak by funkce měla fungovat?
- **Alternativy**: Jaké jsou alternativní přístupy?
- **Dodatečný kontext**: Screenshots, mockupy, atd.

### Diskuze před implementací

Pro větší změny prosím:
1. Otevři issue s návrhem
2. Počkej na zpětnou vazbu od maintainerů
3. Diskutuj design a přístup
4. Pak začni implementovat

## Pull Request Process

### Checklist před PR

- [ ] Kód prošel všemi testy (`pytest`)
- [ ] Kód prošel lintingem (automaticky přes pre-commit)
- [ ] Přidány testy pro novou funkcionalitu
- [ ] Dokumentace je aktualizovaná
- [ ] Commit zprávy následují konvence
- [ ] Branch je aktuální s main/master

### Review Process

1. Maintainer zkontroluje PR během 48 hodin
2. Může požádat o změny
3. Po schválení bude PR mergenut
4. Automatické testy musí projít

## Otázky?

- 💬 Discord: [junior.guru](https://junior.guru/discord/)
- 📧 Issues: [GitHub Issues](https://github.com/yourusername/pacman-game/issues)

---

Děkujeme za tvůj čas a příspěvek! 🙏
