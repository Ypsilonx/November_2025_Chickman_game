# 🗺️ Development Roadmap

## Projekt: Pacman Game - Junior.guru Challenge
**Start:** 6. listopadu 2025  
**Očekávaný Release:** Prosinec 2025

---

## 📅 Phase 1: Foundation (Týden 1-2)
**Cíl:** Základní infrastruktura a core gameplay

### Week 1: Projekt Setup ✅
- [x] Projektová struktura
- [x] Git repository setup
- [x] Documentation (README, CONTRIBUTING, etc.)
- [x] Development rules
- [x] Game design document

### Week 2: Core Gameplay
- [ ] Basic game loop v Arcade
- [ ] Player (Pacman) třída
- [ ] Keyboard input handling
- [ ] Simple maze rendering
- [ ] Basic collision detection
- [ ] Camera/viewport setup

**Deliverable:** Hráč se může pohybovat v jednoduchém bludišti

---

## 📅 Phase 2: Game Entities (Týden 3-4)
**Cíl:** Všechny herní entity a základní mechaniky

### Week 3: Collectibles
- [ ] Dot system (malé tečky)
- [ ] Power pellets
- [ ] Score system
- [ ] Collision with collectibles
- [ ] Basic sound effects

### Week 4: Maze System
- [ ] TMX map loader
- [ ] Wall collision perfect
- [ ] Teleport tunnels
- [ ] Multiple level support
- [ ] Spawn points system

**Deliverable:** Funkční bludiště se sbíráním teček

---

## 📅 Phase 3: Enemies & AI (Týden 5-6)
**Cíl:** Duchové a jejich AI

### Week 5: Ghost Basics
- [ ] Ghost base class
- [ ] 4 duchové (Blinky, Pinky, Inky, Clyde)
- [ ] Ghost animations
- [ ] Basic movement
- [ ] Spawn system & timing

### Week 6: Ghost AI
- [ ] A* pathfinding algorithm
- [ ] Chase mode strategies:
  - [ ] Blinky (direct chase)
  - [ ] Pinky (ambush)
  - [ ] Inky (patrol)
  - [ ] Clyde (random)
- [ ] Scatter mode
- [ ] State machine (chase/scatter/frightened)

**Deliverable:** Duchové s fungující AI pronásledují hráče

---

## 📅 Phase 4: Advanced Mechanics (Týden 7)
**Cíl:** Power-ups a pokročilé mechaniky

### Week 7: Game Mechanics
- [ ] Frightened mode (po power pellet)
- [ ] Eating ghosts
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
