def check_pet_status(pet):
    if pet.hunger >= 100:
        return f"{pet.name} ran away because you didn’t feed them in time!"
    elif pet.mood <= 0:
        return f"{pet.name} is too sad and has left you..."
    elif pet.energy <= 0:
        return f"{pet.name} collapsed from exhaustion! Game over."
    elif pet.health <= 0:
        return f"{pet.name} got too sick and passed away... Game over."
    elif pet.happiness <= 0:
        return f"{pet.name} is too unhappy and has left you..."
    elif pet.hygiene <= 0:
        return f"{pet.name} got too dirty and ran away!"
    elif pet.social <= 0:
        return f"{pet.name} is too lonely and has left you..."
    return None