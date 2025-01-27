import json
import os
from datetime import datetime
from ..models.pet import VirtualPet

def save_pet_state(pet):
    state = {
        "name": pet.name,
        "mood": pet.mood,
        "hunger": pet.hunger,
        "energy": pet.energy,
        "health": pet.health,
        "happiness": pet.happiness,
        "hygiene": pet.hygiene,
        "social": pet.social,
        "age": pet.age,
        "xp": pet.xp,
        "level": pet.level,
        "personality": pet.personality,
        "last_updated": pet.last_updated.isoformat()
    }
    with open("pet_state.json", "w") as f:
        json.dump(state, f)

def load_pet_state():
    if os.path.exists("pet_state.json"):
        with open("pet_state.json", "r") as f:
            state = json.load(f)
            pet = VirtualPet(state["name"])
            pet.mood = state["mood"]
            pet.hunger = state["hunger"]
            pet.energy = state["energy"]
            pet.health = state["health"]
            pet.happiness = state["happiness"]
            pet.hygiene = state["hygiene"]
            pet.social = state["social"]
            pet.age = state["age"]
            pet.xp = state["xp"]
            pet.level = state["level"]
            pet.personality = state["personality"]
            pet.last_updated = datetime.fromisoformat(state["last_updated"])
            return pet
    return VirtualPet("Buddy")  # Default pet