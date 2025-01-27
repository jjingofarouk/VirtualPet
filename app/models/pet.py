import random
import datetime

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.mood = 100
        self.hunger = 50
        self.energy = 50
        self.health = 100
        self.happiness = 100
        self.hygiene = 100
        self.social = 100
        self.age = 0  # in days
        self.xp = 0
        self.level = 1
        self.personality = random.choice(["playful", "lazy", "curious", "grumpy"])
        self.last_updated = datetime.datetime.now()

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.mood = min(100, self.mood + 10)
        self.happiness = min(100, self.happiness + 5)
        self.xp += 5

    def play(self):
        if self.energy >= 20:
            self.mood = min(100, self.mood + 20)
            self.energy -= 20
            self.hunger = min(100, self.hunger + 10)
            self.happiness = min(100, self.happiness + 10)
            self.social = min(100, self.social + 10)
            self.xp += 10
        else:
            self.mood = max(0, self.mood - 10)

    def rest(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 5)
        self.health = min(100, self.health + 10)
        self.xp += 5

    def clean(self):
        self.hygiene = min(100, self.hygiene + 30)
        self.happiness = min(100, self.happiness + 10)
        self.xp += 5

    def socialize(self):
        self.social = min(100, self.social + 20)
        self.happiness = min(100, self.happiness + 15)
        self.xp += 10

    def pass_time(self):
        time_passed = (datetime.datetime.now() - self.last_updated).seconds // 60  # in minutes
        self.hunger = min(100, self.hunger + time_passed * 0.1)
        self.energy = max(0, self.energy - time_passed * 0.1)
        self.mood = max(0, self.mood - time_passed * 0.05)
        self.hygiene = max(0, self.hygiene - time_passed * 0.05)
        self.social = max(0, self.social - time_passed * 0.05)
        self.health = max(0, self.health - time_passed * 0.02)
        self.happiness = max(0, self.happiness - time_passed * 0.03)
        self.age += time_passed / (60 * 24)  # convert minutes to days
        self.last_updated = datetime.datetime.now()