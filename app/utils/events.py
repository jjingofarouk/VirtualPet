import random

def generate_random_event(pet_name):
    events = [
        f"{pet_name} found a toy and is happily playing on their own!",
        f"{pet_name} looks sad... maybe they want attention.",
        f"{pet_name} is trying to get into the food cabinet!",
        f"{pet_name} seems bored. Try playing with them!",
        f"{pet_name} got dirty and needs a bath!",
        f"{pet_name} is feeling lonely and wants to socialize."
    ]
    return random.choice(events)