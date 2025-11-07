# 🎨 Chickman - Sprite Template Guide

Tento dokument obsahuje specifikace a template pro vytvoření grafických assetů pro hru Chickman.

---

## 📐 Technické specifikace

### Základní informace
- **Formát:** PNG s transparencí (alpha channel)
- **Velikost sprite:** 48x48 px (zvětšeno z původních 28px pro lepší viditelnost)
- **Barvy:** RGB, 32-bit
- **Background:** Transparentní
- **Grid:** Hra používá 32px tile grid, sprite jsou 48px pro překrytí

### Struktura složek
```
src/pacman/assets/sprites/
├── chicken/           # Kuře (hráč)
│   ├── chicken_idle.png
│   ├── chicken_right.png
│   ├── chicken_left.png
│   ├── chicken_up.png
│   └── chicken_down.png
│
├── foxes/             # Lišky (nepřátelé)
│   ├── rusty.png      # Červeno-oranžová liška
│   ├── ginger.png     # Oranžová liška
│   ├── copper.png     # Hnědá liška
│   ├── amber.png      # Žluto-oranžová liška
│   └── scared.png     # Vystrašená liška (modrá)
│
└── items/             # Sběratelné předměty
    ├── seed.png       # Semínko (6x6 px)
    └── super_seed.png # Super semínko (16x16 px)
```

---

## 🐔 Kuře (Chicken) - Hlavní postava

### Specifikace
- **Velikost:** 48x48 px
- **Základní barva:** Žlutá (#FFFF00)
- **Styl:** Roztomilý, cartoon styl
- **Směry:** 4 směry (nahoru, dolů, vlevo, vpravo) + idle

### Design návrhy:

**Chicken Idle (chicken_idle.png):**
```
Kuře ze předu:
- Kulaté tělo
- Malý zobák (uprostřed)
- Dvě tečky jako oči
- Křídla po stranách
- Krátké nožky
```

**Chicken Right (chicken_right.png):**
```
Kuře z boku (doprava):
- Tělo v profilu
- Jedno oko viditelné
- Zobák směrem doprava
- Křídlo viditelné
- Nožky v pohybu
```

**Chicken Left (chicken_left.png):**
```
Zrcadlový obraz chicken_right
```

**Chicken Up (chicken_up.png):**
```
Kuře zezadu:
- Zaoblené tělo
- Ocásek nahoře
- Křídla po stranách
- Nožky zdola
```

**Chicken Down (chicken_down.png):**
```
Kuře zepředu:
- Podobné jako idle
- Zobák více viditelný
- Křídla lehce rozpažené
```

### Barevná paleta pro kuře:
```
Tělo: #FFFF00 (žlutá)
Zobák: #FFA500 (oranžová)
Oči: #000000 (černá)
Nožky: #FF8C00 (tmavě oranžová)
Obrys: #CC9900 nebo #000000
```

---

## 🦊 Lišky (Foxes) - Nepřátelé

### Specifikace
- **Velikost:** 48x48 px
- **Styl:** Lehce hrozivé, ale cute
- **4 různé lišky** s různými barvami
- **Scared mode:** Modrá varianta pro všechny

### 1. Rusty (Červeno-oranžová liška)
```
Barva: #FF4500 (červeno-oranžová)
Osobnost: Agresivní, rychlá
Template:
- Špičaté uši
- Kulatá hlava
- Bílý obrys kolem očí
- Špičatý čumák
- Ocas za tělem
```

### 2. Ginger (Oranžová liška)
```
Barva: #FF8C00 (jasně oranžová)
Osobnost: Lstivá, chytrá
Template:
- Podobná struktura jako Rusty
- Lehce odlišný tvar uší
- Stejný base design
```

### 3. Copper (Hnědá liška)
```
Barva: #B87333 (měděně hnědá)
Osobnost: Pomalá, stabilní
Template:
- Zaoblenější tvary
- Širší tělo
- Kratší uši
```

### 4. Amber (Žluto-oranžová liška)
```
Barva: #FFBF00 (jantarová)
Osobnost: Nepředvídatelná
Template:
- Menší tělo
- Delší ocas
- Větší oči
```

### Scared Fox (scared.png)
```
Barva: #2121FF (modrá)
- Všechny lišky používají tento sprite když jsou vystrašené
- Třesoucí se animace (možno zajistit v kódu)
- Bílé oči (vyděšený výraz)
```

### Barevná paleta pro lišky:
```
Rusty:  #FF4500
Ginger: #FF8C00
Copper: #B87333
Amber:  #FFBF00
Scared: #2121FF

Oči:    #FFFFFF (bílé) + #000000 (zorničky)
Čumák:  #FFA07A (světlý lososový)
Obrys:  #000000 (černý)
```

---

## 🌾 Semínka (Seeds)

### Běžné semínko (seed.png)
- **Velikost:** 6x6 px
- **Barva:** #FFFFFF (bílá)
- **Tvar:** Malý kulatý bod nebo jednoduché semínko
- **Styl:** Jednoduchý, minimalistický

### Super semínko (super_seed.png)
- **Velikost:** 16x16 px
- **Barva:** #FFB852 (oranžová)
- **Tvar:** Větší semínko s blikajícím efektem (animace v kódu)
- **Styl:** Výraznější, s leskem

---

## 🎨 Jak vytvořit sprite

### Metoda 1: Pixel Art Editor (Doporučeno)
1. **Aseprite** (placený, $19.99) - https://www.aseprite.org/
2. **Piskel** (zdarma, online) - https://www.piskelapp.com/
3. **GraphicsGale** (zdarma) - https://graphicsgale.com/

### Metoda 2: Standartní grafický editor
1. **GIMP** (zdarma) - https://www.gimp.org/
2. **Krita** (zdarma) - https://krita.org/
3. **Photoshop** (placený)

### Postup vytvoření:
1. Vytvoř nový projekt 48x48 px
2. Zapni grid (8x8 nebo 16x16)
3. Použij transparentní pozadí
4. Nakresli sprite podle templatu výše
5. Exportuj jako PNG s průhledností
6. Ulož do správné složky

---

## 📏 Template šablony

### Grid šablona 48x48 px

```
Pro vytištění nebo jako vodítko:

+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   6px
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   | C E N T E R |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
        48px width
```

---

## 🎭 Jednoduché textové templaty

Pokud nechceš hned kreslit, můžeš začít s jednoduchými tvary:

### Kuře (zjednodušené):
```
  ___
 /o o\    <- oči
 \ < /    <- zobák
  |_|     <- tělo
  | |     <- nožky
```

### Liška (zjednodušené):
```
  /\ /\   <- uši
 ( o.o )  <- oči a nos
  > ^ <   <- čumák
   ---    <- tělo
```

---

## 🚀 Rychlý start

Pokud chceš začít hned:

1. **Stáhni Piskel** (online, zdarma): https://www.piskelapp.com/
2. **Vytvoř nový sprite** 48x48 px
3. **Použij tyto základní barvy:**
   - Kuře: #FFFF00
   - Rusty liška: #FF4500
   - Ginger liška: #FF8C00
   - Copper liška: #B87333
   - Amber liška: #FFBF00

4. **Nakresli základní tvary:**
   - Kruh pro hlavu
   - Menší kruhy pro oči
   - Trojúhelník pro zobák/čumák
   - Zaoblené tělo

5. **Exportuj jako PNG** s transparencí

6. **Ulož do složky:**
   ```
   src/pacman/assets/sprites/chicken/chicken_idle.png
   src/pacman/assets/sprites/foxes/rusty.png
   ```

---

## 🎨 Alternativa: AI generované sprite

Můžeš také použít AI pro generování:

**DALL-E / Midjourney prompt:**
```
"pixel art sprite, cute yellow chicken character, 48x48 pixels, 
transparent background, cartoon style, simple design, 
8-bit retro game aesthetic, front view"

"pixel art sprite, orange fox character, 48x48 pixels,
transparent background, cartoon style, simple design,
8-bit retro game aesthetic, side view"
```

---

## 📝 Checklist před použitím

- [ ] Sprite je 48x48 px
- [ ] PNG formát s průhledností
- [ ] Sprite je centrovaný v rámečku
- [ ] Barvy odpovídají paletě
- [ ] Soubor má správný název
- [ ] Soubor je ve správné složce
- [ ] Sprite je čitelný na černém pozadí

---

## 💡 Tipy

1. **Start simple** - Začni s jednoduchými tvary
2. **Use symmetry** - Využij symetrii (levá/pravá strana)
3. **Test in-game** - Zkus sprite ve hře, jak vypadá
4. **Keep consistent** - Zachovej konzistentní styl mezi všemi sprites
5. **Add personality** - Dej každé lišce vlastní osobnost barvou a detaily

---

Hodně štěstí s tvorbou! 🎨🐔🦊

