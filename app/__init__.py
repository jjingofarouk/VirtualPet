from flask import Flask
from .models.pet import VirtualPet
from .utils.persistence import load_pet_state

# Initialize the pet globally
pet = load_pet_state()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # Point to the templates and static folders in the root directory
    app.config.from_pyfile('../config.py')

    # Make the pet object available to the app context
    app.pet = pet

    # Register blueprints
    from .routes.home import home_bp
    from .routes.actions import actions_bp
    from .routes.reset import reset_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(actions_bp)
    app.register_blueprint(reset_bp)

    return app