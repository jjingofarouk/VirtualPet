from flask import Blueprint, redirect, url_for, current_app
from ..models.pet import VirtualPet
from ..utils.persistence import save_pet_state

reset_bp = Blueprint('reset', __name__)

@reset_bp.route("/reset")
def reset():
    current_app.pet = VirtualPet("Buddy")  # Reset the pet object in the app context
    save_pet_state(current_app.pet)
    return redirect(url_for("home.home"))