import random
from flask import Blueprint, render_template, current_app
from ..utils.events import generate_random_event
from ..utils.status_checker import check_pet_status
from ..utils.leveling import check_level_up

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    pet = current_app.pet  # Access the pet object from the app context
    pet.pass_time()

    random_event = None
    if random.randint(1, 5) == 1:  # 1 in 5 chance of a random event
        random_event = generate_random_event(pet.name)

    status = check_pet_status(pet)
    if status:
        return render_template("game_over.html", pet=pet, message=status)

    level_up_message = check_level_up(pet)
    return render_template("index.html", pet=pet, random_event=random_event, level_up_message=level_up_message)