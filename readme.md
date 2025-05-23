# 🚗 Flappy Car — Pygame Project

Flappy Car is a Python game inspired by Flappy Bird — but with a twist: you're flying a **car** through obstacles.  
Built from scratch using **modular Python code** and **Pygame**, this project is designed for clean code structure, easy version tracking, and feature expansion.

---

## 🛠 v2.4-dev Progress Log

> Ongoing updates and feature additions for version 2.4

- ✅ Tweaked physics and scale for better playability
- ✅ Integrated new pixel art **Mazda RX-7 style sprite** (side view, red)
- ✅ Scaled sprite with **transparent background** 
- ✅ Integrated new pixel art **Classic style pipes** (top  bottom shared sprite, green)
- ✅ Tiled and cropped automaticlly to preserve resolution and size
- ✅ Added toggleable **Dev Debug Mode** using the `D` key
- ✅ Visualized the car's **collision box** (red outline)
- ✅ Fine-tuned hitbox for accurate gameplay feel
- ✅ Refactored draw methods to support `debug_mode` flag cleanly
- ✅ "DEBUG MODE ON" label in debug mode
- ✅ Custom **Flapy Bird like skyline background** (blue gradient, 3 tone buidings, clouds)

## 🛠 Ongoing Bug Fixes / Improvments

- ❌ collision box doesnt match top pipe closely enough
- 🔧 collision box can be re-shaped to better fit the car sprite(s)


## 🛠 v2.4-dev Progress CHECKLIST

> This section tracks new features and updates added during v2.4 development.

- [x] Added `v2.4-dev` branch for upcoming features
- [x] Set up sprite loading system  
  - [x] For the car  
  - [x] For the pipes  (this was harder than expected)
  - [x] For the background
- [ ] Designed and implemented car sprite animation  
  - [x] Basic rotation on jump and fall
- [x] Add sound effects (jump, crash)
- [x] Add background music
- [ ] Created main menu screen
- [ ] Add pause and resume functionality

## Small Changes BIG Differences

- Tweaked gravity and jump strength
- Tweaked pipe scroll speed
- Tweaked gap size
- Tweaked pipe size
- Tweaked car size and resolution

- Added sound!

- Sorted assets into folders