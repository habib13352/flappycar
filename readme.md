# 🚗 Flappy Car — Pygame Project

Flappy Car is a Python game inspired by Flappy Bird — but with a twist: you're flying a **car** through obstacles.  
Built from scratch using **modular Python code** and **Pygame**, this project is designed for clean code structure, easy version tracking, and feature expansion.

This version (`v2.3`) introduces:
- 🚀 New gravity and speed settings
- 🏆 A fully working highscore system with 1–3 character initials
- 🧠 Better modular code for easier updates

---

## 🎮 Features

- Car controlled with spacebar (flap-style movement)
- Randomized vertical pipe gaps for replayability
- Top-10 highscore tracking using arrow keys + Enter
- All code separated into clean modules:
  - `game.py`: Game loop and input
  - `logic.py`: Movement, pipe creation, collisions
- Highscore data stored in `highscores.json` (not tracked in Git)

---

## 🧠 Technologies Used

- **Python 3.11+**
- **Pygame**

---

## 🛠️ Installation

Make sure Python and Pygame are installed:

```bash
pip install pygame

<!-- Started v2.4-dev branch -->

## 🛠 v2.4-dev Progress Log

> This section tracks new features and updates added during v2.4 development.

- [ X ] Added `v2.4-dev` branch for upcoming features
- [ ] Set up sprite loading system
- [ ] Designed and implemented car sprite animation
- [ ] Added sound effects (jump, crash)
- [ ] Created main menu screen
- [ ] Added pause and resume functionality