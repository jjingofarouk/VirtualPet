def check_level_up(pet):
    if pet.xp >= pet.level * 100:
        pet.level += 1
        pet.xp = 0
        return f"{pet.name} leveled up to level {pet.level}!"
    return None