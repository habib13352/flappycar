# 🚗 Flappy Car — Pygame Project

Flappy Car is a Python game inspired by Flappy Bird — but with a twist: you're flying a **car** through obstacles.  
Built from scratch using **modular Python code** and **Pygame**, this project is designed for clean code structure, easy version tracking, and feature expansion.

---

## 🛠 v2.4-dev Progress CHECKLIST

> This section tracks new features and updates added during v2.4 development.

- [x] Added `v2.4-dev` branch for upcoming features  
- [x] Set up sprite loading system  
  - [x] For the car  
  - [x] For the pipes (this was harder than expected)  
  - [x] For the background  
- [ ] Designed and implemented car sprite animation  
  - [x] Basic rotation on jump and fall  
- [x] Add sound effects (jump, crash)  
- [x] Add background music  
- [ ] Created main menu screen  
- [ ] Add pause and resume functionality

---

<details>
<summary>🛠 <strong>v2.4-dev Progress Log</strong></summary>

> Ongoing updates and feature additions for version 2.4

- ✅ Tweaked physics and scale for better playability  
- ✅ Integrated new pixel art **Mazda RX-7 style sprite** (side view, red)  
- ✅ Scaled sprite with **transparent background**  
- ✅ Integrated new pixel art **Classic style pipes** (top & bottom shared sprite, green)  
- ✅ Tiled and cropped automatically to preserve resolution and size  
- ✅ Added toggleable **Dev Debug Mode** using the `D` key  
- ✅ Visualized the car's **collision box** (red outline)  
- ✅ Fine-tuned hitbox for accurate gameplay feel  
- ✅ Refactored draw methods to support `debug_mode` flag cleanly  
- ✅ "DEBUG MODE ON" label in debug mode  
- ✅ Custom **Flappy Bird–like skyline background** (blue gradient, 3-tone buildings, clouds)

</details>

---

<details>
<summary>🐞 <strong>Ongoing Bug Fixes / Improvements</strong></summary>

- ✅ Collision box doesn't match top pipe closely enough  
- 🔧 Collision box can be reshaped to better fit the car sprite(s)  
- 🔧 Limit pipe gap randomness in `pipe_pair_gen()`  
- 🔧 Limit max speed  
- 🔧 Try different scroll speeds and pipe gap values

</details>

---

<details>
<summary>🔧 <strong>Small Changes BIG Differences</strong></summary>

- Tweaked gravity and jump strength  
- Tweaked pipe scroll speed  
- Tweaked gap size  
- Tweaked pipe size  
- Tweaked car size and resolution  
- Added sound!  
- Sorted assets into folders

</details>

---

<details>
<summary>🚀 <strong>How to Build & Run</strong></summary>

To get the game running locally:

### 🧾 Prerequisites
- Python 3.7 or later installed
- Pygame library installed

### 📥 Clone the Repository
```bash
git clone https://github.com/habib13352/flappycar
```

### 📦 Install Dependencies
```bash
pip install pygame
```

### ▶️ Run the Game
```bash
python main.py
```

</details>
