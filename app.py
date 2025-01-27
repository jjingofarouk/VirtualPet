from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Pet class
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.mood = 100
        self.hunger = 50
        self.energy = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.mood = min(100, self.mood + 10)

    def play(self):
        if self.energy >= 20:
            self.mood = min(100, self.mood + 20)
            self.energy -= 20
            self.hunger = min(100, self.hunger + 10)

    def rest(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 5)

    def pass_time(self):
        self.hunger = min(100, self.hunger + 10)
        self.energy = max(0, self.energy - 10)
        self.mood = max(0, self.mood - 5)

    def random_event(self):
        events = [
            f"{self.name} found a toy and is happily playing on their own!",
            f"{self.name} looks sad... maybe they want attention.",
            f"{self.name} is trying to get into the food cabinet!",
            f"{self.name} seems bored. Try playing with them!"
        ]
        return random.choice(events)

    def check_status(self):
        if self.hunger >= 100:
            return f"{self.name} ran away because you didn’t feed them in time!"
        elif self.mood <= 0:
            return f"{self.name} is too sad and has left you..."
        elif self.energy <= 0:
            return f"{self.name} collapsed from exhaustion! Game over."
        return None


# Initialize pet
pet = VirtualPet("Buddy")  # Default name for the pet

@app.route("/")
def home():
    random_event = None
    if random.randint(1, 5) == 1:  # 1 in 5 chance of a random event
        random_event = pet.random_event()

    status = pet.check_status()
    if status:
        return render_template("game_over.html", pet=pet, message=status)

    return render_template("index.html", pet=pet, random_event=random_event)

@app.route("/action", methods=["POST"])
def action():
    action = request.form.get("action")
    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "rest":
        pet.rest()

    pet.pass_time()
    return redirect(url_for("home"))


@app.route("/reset")
def reset():
    global pet
    pet = VirtualPet("Buddy")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
