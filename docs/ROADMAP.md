# 🗺️ Development Roadmap - Chickman Game

## Projekt: Chickman - Junior.guru Challenge
**Start:** 6. listopadu 2025  
**Aktuální stav:** 7. listopadu 2025  
**Očekávaný Release:** Prosinec 2025

---

## ✅ HOTOVO - Co už máme (7. listopadu 2025)

### ✨ Kompletní rebrand: Pacman → Chickman
- [x] Všechny herní prvky přejmenovány (chicken, foxes, seeds)
- [x] Dokumentace aktualizována (README, CONTRIBUTING, CREDITS, PROJECT_SUMMARY)
- [x] GitHub repository: November_2025_Chickman_game
- [x] Všechny URL a odkazy aktualizovány

### 🎮 Základní gameplay implementovaný
- [x] Projekt setup a struktura
- [x] Git repository a dokumentace
- [x] Main game loop (ChickmanGame class)
- [x] Player (Chicken) s pohybem (šipky/WASD)
- [x] Buffered input pro plynulý pohyb
- [x] Maze rendering (32x24 grid → 24x18 grid po úpravě)
- [x] 8-point collision detection
- [x] Teleport tunely

### 🌾 Collectibles systém
- [x] Seeds (běžná semínka, 10 bodů)
- [x] Super Seeds (power pellets, 50 bodů, oranžové, blikající)
- [x] Flood fill algoritmus pro reachable tiles
- [x] Score tracking
- [x] Collision detection se seeds

### 🦊 Fox (nepřátelé) systém
- [x] 4 lišky: Rusty, Ginger, Copper, Amber
- [x] Různé barvy pro každou lišku
- [x] FoxState (CHASE, SCATTER, FRIGHTENED, EATEN)
- [x] Power mode (10s frightened mode po super seed)
- [x] Základní AI movement
- [x] Collision detection s chicken

### 📐 Vizuální vylepšení
- [x] Zvětšení sprite: CHICKEN_SIZE a FOX_SIZE na 48px
- [x] Zvětšení TILE_SIZE z 32px na 50px
- [x] Rozlišení upraveno na 1200x900 (24x18 grid)
- [x] Rychlosti upraveny úměrně (CHICKEN_SPEED=5, FOX_SPEED=4)
- [x] Vytvořen SPRITE_TEMPLATE.md s design guide

---

## � CO DĚLAT PŘÍŠTĚ - Další kroky

### Priorita 1: Grafické assety 🎨
**Důležité:** Hra nyní používá pouze barevné kruhy!

**TODO:**
- [ ] Vytvořit sprite pro kuře (chicken):
  - [ ] chicken_idle.png (48x48px)
  - [ ] chicken_right.png
  - [ ] chicken_left.png  
  - [ ] chicken_up.png
  - [ ] chicken_down.png
- [ ] Vytvořit sprite pro lišky (foxes):
  - [ ] rusty.png (#FF4500)
  - [ ] ginger.png (#FF8C00)
  - [ ] copper.png (#B87333)
  - [ ] amber.png (#FFBF00)
  - [ ] scared.png (#2121FF)
- [ ] Vytvořit sprite pro seeds:
  - [ ] seed.png (6x6px)
  - [ ] super_seed.png (16x16px)

**Nástroje:** Viz SPRITE_TEMPLATE.md (Piskel, Aseprite, GIMP)

### Priorita 2: Načítání sprite do hry 🖼️
- [ ] Implementovat sprite loading v Player class
- [ ] Implementovat sprite loading v Fox class
- [ ] Animace pro pohyb (směry)
- [ ] Sprite manager/cache

### Priorita 3: Vylepšit Fox AI 🦊
- [ ] A* pathfinding algoritmus
- [ ] Lepší chase strategies:
  - [ ] Rusty: Direct chase (agresivní)
  - [ ] Ginger: Ambush (4 tiles ahead)
  - [ ] Copper: Patrol (pomalý, stabilní)
  - [ ] Amber: Random/Unpredictable
- [ ] Scatter mode s časováním
- [ ] Smooth movement mezi tiles
- [ ] Corner turning optimalizace

### Priorita 4: Lives systém a Game Over ❤️
- [ ] Lives counter (3 životy na start)
- [ ] Respawn mechanika po smrti
- [ ] Death animace pro chicken
- [ ] Game Over screen
- [ ] Restart možnost

### Priorita 5: Level systém 🗺️
- [ ] TMX map loader (Tiled)
- [ ] Multiple levels
- [ ] Level complete screen
- [ ] Level progression
- [ ] Složitější maze layouts

---

## 📅 BUDOUCÍ FEATURES - Pro později

### Audio 🔊
- [ ] Zvuky pro:
  - [ ] Eating seeds
  - [ ] Super seed power up
  - [ ] Fox caught
  - [ ] Death
  - [ ] Level complete
- [ ] Background music
- [ ] Mute option

### UI/UX vylepšení 🎨
- [ ] Main menu
- [ ] Pause menu
- [ ] Settings (volume, controls)
- [ ] High score table
- [ ] Better HUD design

### Bonus features ⭐
- [ ] Bonus fruits (500 bodů)
- [ ] Combo system
- [ ] Achievements
- [ ] Speed running mode
- [ ] Difficulty levels

### Polish & Testing ✨
- [ ] Unit testy
- [ ] Performance optimalizace
- [ ] Bug fixing
- [ ] Playtesting s komunitou
- [ ] Balance tweaking

---

## 📊 Aktuální statistiky

**Kód:**
- ✅ ChickmanGame (game.py) - 390 řádků
- ✅ Player (player.py) - 213 řádků  
- ✅ Fox (fox.py) - 404 řádků
- ✅ Collectibles (collectibles.py) - 311 řádků
- ✅ Maze (maze.py) - funkční
- ✅ Constants - kompletní konfigurace

**Gameplay:**
- ✅ Základní mechaniky fungují
- ✅ Power mode implementován (10s)
- ✅ Collision detection hotovo
- ✅ Score tracking funguje
- ⚠️ **CHYBÍ:** Grafické sprite (používají se kruhy)
- ⚠️ **CHYBÍ:** Lives systém
- ⚠️ **CHYBÍ:** Advanced AI

---

## 💡 Poznámky pro příští session

### Kde začít:
1. **NEJDŘÍV:** Vytvoř základní sprite (viz SPRITE_TEMPLATE.md)
   - Stačí jednoduchý pixel art v Piskel
   - Začni s chicken_idle.png (48x48px, žluté kuře)
   
2. **PAK:** Implementuj načítání sprite do Player class
   - arcade.load_texture()
   - Nahraď draw_circle_filled() za sprite

3. **NAKONEC:** Stejně pro lišky

### Technické detaily:
- Screen: 1200x900 (24x18 grid)
- Tile size: 50px
- Sprite size: 48x48px (vejdou se do 50px tiles)
- Speeds: CHICKEN=5, FOX=4, FOX_SCARED=2.5

### Užitečné odkazy:
- SPRITE_TEMPLATE.md - kompletní návod na tvorbu sprite
- Piskel (online): https://www.piskelapp.com/
- Aseprite: https://www.aseprite.org/

---

**Poslední commit:** `feat: complete Chickman rebrand and improve game visuals`  
**Branch:** master  
**Status:** ✅ Vše commitnuto a pushnuto na GitHub

🐔 Happy coding! 🦊


- [ ] Eaten mode (ghost eyes returning)
- [ ] Fruit bonuses
- [ ] Lives system
- [ ] Level completion
- [ ] Difficulty progression

**Deliverable:** Kompletní herní mechaniky jako v originálu

---

## 📅 Phase 5: UI & Menus (Týden 8)
**Cíl:** User interface a herní flow

### Week 8: UI Development
- [ ] Main menu
  - [ ] New game
  - [ ] High scores
  - [ ] Options
  - [ ] Quit
- [ ] In-game HUD
  - [ ] Score display
  - [ ] Lives display
  - [ ] Level indicator
- [ ] Pause menu
- [ ] Game Over screen
- [ ] Level transition screens

**Deliverable:** Kompletní UI flow od menu po game over

---

## 📅 Phase 6: Polish & Audio (Týden 9)
**Cíl:** Zvuky, efekty, "game juice"

### Week 9: Audio & Effects
- [ ] Background music
- [ ] Sound effects:
  - [ ] Waka waka (eating dots)
  - [ ] Power pellet activate
  - [ ] Ghost eaten
  - [ ] Death sound
  - [ ] Level complete
  - [ ] Extra life
- [ ] Particle effects
- [ ] Screen shake
- [ ] Smooth animations
- [ ] Visual feedback

**Deliverable:** Polished hra s audio a efekty

---

## 📅 Phase 7: Testing & Optimization (Týden 10)
**Cíl:** Bug fixing a performance

### Week 10: Quality Assurance
- [ ] Unit tests completion (80%+ coverage)
- [ ] Integration tests
- [ ] Performance profiling
- [ ] Memory leak checks
- [ ] Bug fixing
- [ ] Balance adjustments
- [ ] Playtesting
- [ ] Code cleanup

**Deliverable:** Stabilní, otestovaná verze

---

## 📅 Phase 8: Documentation & Release (Týden 11-12)
**Cíl:** Release preparation

### Week 11: Documentation
- [ ] API documentation
- [ ] Tutorial/How to play
- [ ] Developer guide
- [ ] Architecture documentation
- [ ] Code comments review
- [ ] README polish
- [ ] Screenshots & GIFs

### Week 12: Release
- [ ] Version 0.1.0 release
- [ ] GitHub release notes
- [ ] Executable builds (PyInstaller)
- [ ] Release announcement
- [ ] junior.guru Discord share
- [ ] Feedback collection

**Deliverable:** v0.1.0 Public Release 🚀

---

## 🎯 Future Enhancements (Post-Release)

### v0.2.0 - Content Update
- [ ] 10+ nových map
- [ ] Nové typy ovoce
- [ ] Achievement systém
- [ ] High score leaderboard
- [ ] Skins pro Pacmana

### v0.3.0 - Multiplayer
- [ ] Local co-op mode
- [ ] Competitive mode
- [ ] Online leaderboards
- [ ] Replay system

### v0.4.0 - Customization
- [ ] Level editor
- [ ] Custom skins
- [ ] Modding support
- [ ] Workshop integration

---

## 📊 Success Metrics

**Technical:**
- ✅ 80%+ test coverage
- ✅ 60 FPS performance
- ✅ < 100MB memory usage
- ✅ Zero critical bugs

**Community:**
- 🎯 50+ GitHub stars
- 🎯 10+ contributors
- 🎯 Featured on junior.guru
- 🎯 Positive feedback from community

---

## 🔄 Agile Practices

### Daily:
- Commit daily
- Run tests
- Update documentation

### Weekly:
- Review progress
- Adjust roadmap if needed
- Community update

### Bi-weekly:
- Sprint planning
- Demo/showcase
- Retrospective

---

## 🆘 Risk Management

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Scope creep | Medium | High | Strict feature freeze po phase 7 |
| Performance issues | Low | Medium | Profiling každý týden |
| Time overrun | Medium | Medium | MVP approach, nice-to-have jako v0.2+ |
| Team availability | Low | Low | Solo projekt, flexibilní timeline |

---

## 📞 Support & Communication

- **GitHub Issues** - bug reports & features
- **GitHub Discussions** - Q&A
- **Discord** - real-time help
- **Weekly Updates** - progress reports

---

**Status:** 🟢 On Track  
**Current Phase:** Phase 1 - Foundation  
**Next Milestone:** Basic game loop  
**Last Updated:** 6. listopadu 2025
