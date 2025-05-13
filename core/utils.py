import os
import json
from core import settings

# Save highscores in a "data" folder alongside main.py
HIGHSCORE_FILE = os.path.join("data", "highscores.json")

def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            return json.load(file)
    return []

def save_highscores(scores):
    # Ensure the data folder exists
    os.makedirs("data", exist_ok=True)
    with open(HIGHSCORE_FILE, "w") as file:
        json.dump(scores, file, indent=2)

def is_highscore(scores, current_score):
    if len(scores) < settings.MAX_SCORES:
        return True
    return current_score > scores[-1]["score"]

def insert_highscore(scores, name, score):
    scores.append({"name": name, "score": score})
    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:settings.MAX_SCORES]
