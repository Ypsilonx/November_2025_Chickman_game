# 🎮 Pacman Game - Junior.guru Community Challenge

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Moderní implementace klasické hry Pacman s vlastními modifikacemi, vytvořená jako výzva pro komunitu [junior.guru](https://junior.guru) na Discordu.

![Game Screenshot](docs/screenshot.png)
*Screenshot bude přidán po implementaci*

## ✨ Features

- 🕹️ Klasická Pacman mechanika s moderními vylepšeními
- 👻 Inteligentní AI pro duchy s různými strategiemi
- 🎨 Čistá a modulární kódová struktura
- 🎵 Zvukové efekty a hudba
- 📊 Systém skóre a žebříčků
- 🎯 Několik úrovní obtížnosti
- 🔧 Snadno rozšiřitelné a modifikovatelné

## 🚀 Rychlý start

### Požadavky

- Python 3.9 nebo vyšší
- pip (správce balíčků)

### Instalace

1. **Naklonuj repozitář:**
   ```bash
   git clone https://github.com/yourusername/pacman-game.git
   cd pacman-game
   ```

2. **Vytvoř virtuální prostředí:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Nainstaluj závislosti:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Spusť hru:**
   ```bash
   python main.py
   ```

## 🎮 Jak hrát

- **Šipky / WASD** - Pohyb
- **ESC** - Pauza/Menu
- **R** - Restart hry

### Cíl hry
- Sněz všechny tečky v bludišti
- Vyhýbej se duchům (nebo je sněz po power pelletu!)
- Získej co nejvyšší skóre

## 🏗️ Struktura projektu

```
pacman-game/
├── src/pacman/          # Hlavní zdrojové soubory
│   ├── entities/        # Hráč, duchové, sbíratelné předměty
│   ├── maps/            # Bludiště a level design
│   ├── ui/              # Menu, HUD, UI komponenty
│   ├── utils/           # Pomocné funkce a konstanty
│   └── assets/          # Grafika, zvuky, mapy
├── tests/               # Unit testy
├── docs/                # Dokumentace
└── main.py              # Vstupní bod aplikace
```

## 🛠️ Vývoj

### Instalace dev závislostí

```bash
pip install -r requirements.txt
pip install -e ".[dev]"
```

### Spuštění testů

```bash
pytest
```

### Code formatting

```bash
# Formátování kódu
black src/ tests/

# Kontrola importů
isort src/ tests/

# Linting
flake8 src/ tests/
```

### Pre-commit hooks

```bash
pre-commit install
pre-commit run --all-files
```

## 📖 Dokumentace

- [Game Design Document](docs/GAME_DESIGN.md) - Herní mechaniky a design
- [Development Rules](docs/DEVELOPMENT_RULES.md) - Pravidla pro vývoj
- [Contributing Guide](CONTRIBUTING.md) - Jak přispět do projektu

## 🤝 Přispívání

Příspěvky jsou vítány! Prosím přečti si [CONTRIBUTING.md](CONTRIBUTING.md) pro více informací.

## 📜 Licence

Tento projekt je licencován pod MIT licencí - viz [LICENSE](LICENSE) soubor.

## 🙏 Poděkování

- [Junior.guru](https://junior.guru) komunita za inspiraci a podporu
- [Python Arcade](https://api.arcade.academy/) za skvělý herní framework
- Původní Pacman od Namco za ikonickou hru

## 📞 Kontakt

- Discord: [junior.guru](https://junior.guru/discord/)
- Issues: [GitHub Issues](https://github.com/yourusername/pacman-game/issues)

---

Vytvořeno s ❤️ pro junior.guru komunitu
