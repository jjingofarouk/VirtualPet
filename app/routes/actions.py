from flask import Blueprint, request, redirect, url_for, current_app
from ..utils.persistence import save_pet_state

actions_bp = Blueprint('actions', __name__)

@actions_bp.route("/action", methods=["POST"])
def action():
    pet = current_app.pet  # Access the pet object from the app context
    action = request.form.get("action")
    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "rest":
        pet.rest()
    elif action == "clean":
        pet.clean()
    elif action == "socialize":
        pet.socialize()

    pet.pass_time()
    save_pet_state(pet)
    return redirect(url_for("home.home"))