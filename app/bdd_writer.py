import os
import re

def sanitize_filename(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)[:50]

def save_bdd_to_file(story: str, bdd: str) -> str:
    folder = "bdd_output"
    os.makedirs(folder, exist_ok=True)
    filename = sanitize_filename(story) + ".feature"
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(bdd)
    return path