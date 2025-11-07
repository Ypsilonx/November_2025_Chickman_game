# Assets Directory

Tato složka obsahuje všechny herní assety (grafika, zvuky, mapy).

## 📁 Struktura

```
assets/
├── sprites/        # Grafika (PNG, sprite sheets)
│   ├── chicken/    # Chickman (kuře) animace
│   ├── foxes/      # Lišky animace
│   ├── tiles/     # Dlaždice bludiště
│   └── ui/        # UI elementy
│
├── sounds/         # Zvukové efekty (WAV, OGG)
│   ├── sfx/       # Sound effects
│   └── music/     # Hudba
│
└── maps/          # Mapy v TMX formátu
    ├── level1.tmx
    ├── level2.tmx
    └── ...
```

## 🎨 Sprite Specifications

- **Formát:** PNG s transparencí
- **Velikost:**
  - Chicken: 28x28 px
  - Foxes: 28x28 px
  - Tiles: 32x32 px
  - UI: variable
- **Barvy:** RGB, 32-bit

## 🎵 Audio Specifications

- **Formát:** WAV nebo OGG
- **Sample rate:** 44.1 kHz
- **Bit depth:** 16-bit
- **Channels:** Stereo (music), Mono (SFX)

## 🗺️ Map Specifications

- **Editor:** Tiled Map Editor
- **Formát:** TMX (XML)
- **Tile size:** 32x32 px
- **Map size:** 25x25 tiles (800x800 px)

## 📝 Asset Checklist

### Sprites (TODO)
- [ ] Chickman idle
- [ ] Chickman moving (4 directions)
- [ ] Chickman power mode
- [ ] Fox sprites (4 colors x 2 directions)
- [ ] Fox frightened
- [ ] Fox eyes (eaten state)
- [ ] Seeds & super seeds
- [ ] Fruits (bonus items)
- [ ] Wall tiles

### Sounds (TODO)
- [ ] Eating seeds sound
- [ ] Super seed power up
- [ ] Fox caught
- [ ] Game over
- [ ] Level complete
- [ ] Menu select
- [ ] Background music

### Maps (TODO)
- [ ] Classic layout
- [ ] Level 2 layout
- [ ] Level 3 layout

## 🎨 Asset Sources

Pro tvorbu assetů můžeme použít:
- **Grafika:** Aseprite, Piskel, GIMP
- **Audio:** Audacity, Bfxr, ChipTone
- **Mapy:** Tiled Map Editor

## 📜 Licence

Všechny assety v tomto projektu jsou:
- Vytvořené komunitou junior.guru
- Nebo použité z public domain/free sources
- Řádně atribuované v [CREDITS.md](../CREDITS.md)

## 🔗 Užitečné zdroje

- [OpenGameArt.org](https://opengameart.org/) - free game assets
- [Freesound.org](https://freesound.org/) - free sound effects
- [Tiled](https://www.mapeditor.org/) - map editor
