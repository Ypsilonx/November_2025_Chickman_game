# 🎮 Game Design Document - Pacman Style Game

**Version:** 0.1.0  
**Datum:** 6. listopadu 2025  
**Projekt:** Junior.guru Discord Community Challenge

---

## 📋 Executive Summary

Moderní implementace klasické hry Pacman s vlastními modifikacemi a vylepšeními. Hra kombinuje nostalgický gameplay s moderními herními mechanikami a je postavena na frameworku Python Arcade pro zajištění čisté architektury a rozšiřitelnosti.

---

## 🎯 Herní koncept

### High Concept
"Klasický Pacman se zkroutkou" - zachováváme základní mechaniky legendární hry, ale přidáváme moderní prvky jako power-upy, různé herní režimy a vylepšené AI duchů.

### Cílová skupina
- Začínající programátoři z junior.guru komunity
- Hráči, kteří si pamatují klasický Pacman
- Lidé, kteří hledají jednoduchou, ale zábavnou arkádovou hru

### Platforma
- PC (Windows, Linux, macOS)
- Python 3.9+
- Python Arcade framework

---

## 🕹️ Core Gameplay Mechaniky

### 1. Pohyb hráče (Pacman)

**Základní pohyb:**
- 4směrný pohyb (nahoru, dolů, vlevo, vpravo)
- Ovládání: šipky nebo WASD
- Plynulý pohyb po mřížce
- Nemožnost procházet zdmi

**Speciální pohyb:**
- **Teleport tunely** - tunely na okrajích mapy teleportují na opačnou stranu
- **Momentum** - Pacman pokračuje v posledním směru, dokud nenarazí na překážku

**Animace:**
- Žvýkací animace (ústa se otevírají/zavírají)
- Rotace podle směru pohybu
- Animace smrti

### 2. Bludiště (Maze)

**Struktura:**
- Tile-based mřížkový systém
- Rozměr: 25x25 dlaždic (konfigurovatelné)
- Velikost dlaždice: 32x32 pixelů

**Prvky bludiště:**
- **Zdi** - neprostupné překážky (modré)
- **Chodby** - cesty kde se pohybuje Pacman
- **Domek duchů** - centrální oblast, kde duchové spawnou
- **Teleport tunely** - levá a pravá strana pro teleportaci

**Levely:**
- Level 1: Klasický layout
- Level 2+: Postupně komplexnější mapy
- Možnost načítat mapy ze souborů (TMX formát)

### 3. Sbíratelné předměty (Collectibles)

#### 3.1 Základní tečky (Dots)
- **Počet:** ~240 na mapu
- **Body:** 10 bodů za tečku
- **Vzhled:** Malé bílé tečky
- **Cíl:** Sebrat všechny tečky = dokončení levelu

#### 3.2 Power Pellety
- **Počet:** 4 na mapu (rohy bludiště)
- **Body:** 50 bodů
- **Efekt:** Aktivuje "Frightened Mode" u duchů na 10 sekund
- **Vzhled:** Větší růžové/bílé blikající tečky

#### 3.3 Ovoce bonusy (🍒🍓🍊🍋)
- **Spawn:** Objeví se po sebrání X% teček
- **Body:** 100-500 bodů podle typu
- **Timeout:** Zmizí po 10 sekundách
- **Typy:**
  - 🍒 Cherry (100 bodů)
  - 🍓 Strawberry (300 bodů)
  - 🍊 Orange (500 bodů)
  - 🍋 Melon (700 bodů)

### 4. Duchové (Ghosts)

**Počet:** 4 duchové s různými barvami a AI strategiemi

#### 4.1 Blinky (Červený) 🔴
- **Strategie:** "Chase" - přímo pronásleduje Pacmana
- **Chování:** Nejagresivnější, vždy míří na aktuální pozici hráče
- **Spawn:** První duchový start hned na začátku

#### 4.2 Pinky (Růžový) 🩷
- **Strategie:** "Ambush" - míří 4 políčka před Pacmana
- **Chování:** Snaží se Pacmana obklíčit
- **Spawn:** Start po 5 sekundách

#### 4.3 Inky (Azurový) 🩵
- **Strategie:** "Patrol" - kombinace pozice Pacmana a Blinkyho
- **Chování:** Nejméně předvídatelný
- **Spawn:** Start po 10 sekundách

#### 4.4 Clyde (Oranžový) 🧡
- **Strategie:** "Random" - když je daleko: chase, když je blízko: scatter
- **Chování:** Nejvíce "plachý"
- **Spawn:** Start po 15 sekund

#### Ghost Režimy:

**1. Chase Mode (Normální)**
- Duchové pronásledují hráče podle svých strategií
- Rychlost: 2.5 tiles/sec
- Barva: Originální (červená, růžová, atd.)

**2. Frightened Mode (Vystrašený)**
- Aktivováno po sebrání Power Pelletu
- Duchové utíkají náhodným směrem
- Rychlost: 1.5 tiles/sec (pomalejší)
- Barva: Modrá
- Trvání: 10 sekund
- Jídlo: Pacman může ducha sníst za 200 bodů

**3. Eaten Mode (Snědený)**
- Pouze oči se vrací do domečku duchů
- Rychlost: 4 tiles/sec (rychlé)
- Po návratu: respawn do normálního módu

**4. Scatter Mode**
- Duchové se rozptýlí do rohů mapy
- Aktivuje se periodicky (každých 20 sekund na 7 sekund)

### 5. Kolize a interakce

**Pacman vs. Zeď:**
- Zastavení pohybu
- Nemožnost projít

**Pacman vs. Tečka:**
- Tečka zmizí
- +10 bodů
- Zvukový efekt

**Pacman vs. Power Pellet:**
- Pellet zmizí
- +50 bodů
- Aktivace Frightened Mode
- Zvukový efekt

**Pacman vs. Duch (Normal):**
- Ztráta 1 života
- Reset pozic všech entit
- Animace smrti
- Game over při 0 životech

**Pacman vs. Duch (Frightened):**
- Duch snědený
- +200 bodů (combo: 400, 800, 1600)
- Duch přejde do Eaten Mode

**Pacman vs. Ovoce:**
- Ovoce zmizí
- +bonus bodů
- Zvukový efekt

---

## 🎨 Vizuální design

### Barevná paleta
```
- Pozadí: Černá (#000000)
- Zdi: Modrá (#2121DE)
- Tečky: Bílá (#FFFFFF)
- Power Pellet: Růžová (#FFB8FF)
- Pacman: Žlutá (#FFFF00)
- Blinky: Červená (#FF0000)
- Pinky: Růžová (#FFB8FF)
- Inky: Azurová (#00FFFF)
- Clyde: Oranžová (#FFB852)
- Frightened Ghost: Modrá (#2121FF)
```

### Grafický styl
- **Retro pixel art** s moderním vyhlazením
- Sprite size: 28x28 pixelů
- Tile size: 32x32 pixelů
- Animace: 4-6 snímků per akce

---

## 🎵 Audio design

### Zvukové efekty
- **Waka waka** - Pacman jí tečky (loop)
- **Power pellet** - Aktivace power módu
- **Eat ghost** - Snězení ducha
- **Death** - Smrt Pacmana
- **Fruit** - Sebrání ovoce
- **Extra life** - Získání extra života

### Hudba
- **Menu theme** - úvodní hudba
- **Gameplay loop** - během hry (v pozadí)
- **Intermission** - mezi levely

---

## 🎮 Herní režimy a UI

### Hlavní menu
```
┌─────────────────────────┐
│   PACMAN GAME           │
│                         │
│   [NEW GAME]            │
│   [HIGH SCORES]         │
│   [OPTIONS]             │
│   [QUIT]                │
└─────────────────────────┘
```

### HUD (Heads-Up Display)
```
╔═══════════════════════════════════════╗
║ SCORE: 000000    HI: 999999          ║
║ ❤️❤️❤️ Lives: 3                      ║
╠═══════════════════════════════════════╣
║                                       ║
║         [GAME AREA]                   ║
║                                       ║
╠═══════════════════════════════════════╣
║ LEVEL: 1    🍒                       ║
╚═══════════════════════════════════════╝
```

### Pauza menu
- **ESC** - otevře pauza menu
- Možnosti: Resume, Restart, Quit to Menu

### Game Over
- Zobrazení finálního skóre
- Možnost zadat jméno pro high score
- Tlačítka: Retry, Main Menu

---

## 🏆 Progresní systém

### Skóre
- **Tečky:** 10 bodů
- **Power Pellet:** 50 bodů
- **Duch 1:** 200 bodů
- **Duch 2:** 400 bodů
- **Duch 3:** 800 bodů
- **Duch 4:** 1600 bodů
- **Ovoce:** 100-700 bodů

### Extra životy
- **10,000 bodů** - první extra život
- **Každých dalších 20,000** - další život
- **Maximum:** 5 životů

### Levely
- **Level 1:** Základní rychlost
- **Level 2+:** +10% rychlost duchů
- **Level 5+:** Kratší frightened mode
- **Level 10+:** Duchové začínají v chase módu

---

## 🔧 Modifikace oproti klasickému Pacmanovi

### ✨ Naše vylepšení:

1. **Moderní grafika a animace**
   - Smooth pixel art
   - Particle effects
   - Better animations

2. **Power-up systém**
   - Speed boost (2x rychlost na 5s)
   - Invincibility (neviditelnost na 3s)
   - Time slow (zpomalení času na 5s)

3. **Achievementy a milníky**
   - "Ghost Hunter" - sněz 100 duchů
   - "Perfectionist" - dokonči level bez ztráty života
   - "Speed Runner" - dokonči level pod 60s

4. **Lokální multiplayer (BUDOUCNOST)**
   - 2 hráči: Kooperace
   - Sdílený skóre
   - Rozdělená obrazovka?

5. **Level editor (BUDOUCNOST)**
   - Vlastní mapy
   - Sdílení s komunitou
   - Steam Workshop style

---

## 📊 Technical specifications

### Performance cíle
- **FPS:** 60 fps konstantně
- **Input lag:** < 16ms
- **Load time:** < 2s

### Platformy
- Windows 10/11
- Ubuntu 20.04+
- macOS 11+

### Minimální požadavky
- Python 3.9+
- 512 MB RAM
- 100 MB disk space
- Integrated graphics

---

## 📅 Development milestones

### Phase 1: Core Gameplay (2 týdny)
- [x] Projektová struktura
- [ ] Základní game loop
- [ ] Pohyb hráče
- [ ] Bludiště a kolize
- [ ] Základní sbírání teček

### Phase 2: Enemies & AI (2 týdny)
- [ ] Duchové základní chování
- [ ] AI strategie pro každého ducha
- [ ] Ghost režimy (chase, frightened, scatter)
- [ ] Kolize s duchy

### Phase 3: Game Systems (1 týden)
- [ ] Skóre systém
- [ ] Životy a game over
- [ ] Levely a progrese
- [ ] Power pellety a bonusy

### Phase 4: UI & Polish (1 týden)
- [ ] Hlavní menu
- [ ] HUD
- [ ] Pause menu
- [ ] Game over screen

### Phase 5: Audio & Juice (1 týden)
- [ ] Zvukové efekty
- [ ] Hudba
- [ ] Particle effects
- [ ] Screen shake

### Phase 6: Testing & Release (1 týden)
- [ ] Bug fixing
- [ ] Performance optimization
- [ ] Documentation
- [ ] Release na GitHub

---

## 🧪 Testing strategie

### Unit testy
- Entity chování
- Kolize detekce
- Score kalkulace
- AI path finding

### Integration testy
- Game states
- Level loading
- Save/Load system

### Playtesting
- Balance duchů
- Obtížnost levelů
- User experience

---

## 🚀 Budoucí rozšíření

### v0.2.0 - Content Update
- 10+ nových map
- Nové bonusové ovoce
- Boss duchové

### v0.3.0 - Multiplayer
- Local co-op
- Competitive mode
- Online leaderboards

### v0.4.0 - Customization
- Skin systém
- Level editor
- Modding support

---

## 📚 Reference a inspirace

- **Pacman (1980)** - Namco - originální hra
- **Ms. Pac-Man (1982)** - lepší AI a mapy
- **Pac-Man Championship Edition** - moderní grafika
- **Python Arcade Examples** - technické reference

---

**Autor:** Junior.guru Community  
**Poslední update:** 6. listopadu 2025  
**Status:** 🟡 In Development
