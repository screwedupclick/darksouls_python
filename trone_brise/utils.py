import json

def sauvegarder_partie(scene_actuelle, fichier="data/saves.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump({"scene": scene_actuelle}, f)

def charger_partie(fichier="data/saves.json"):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("scene", "prologue")
    except FileNotFoundError:
        return "prologue"
