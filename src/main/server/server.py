from flask import Flask
from flask_cors import CORS
from src.models.slqlite.settings.connection import db_connection_handler

# importar blueprints
from src.main.routes.pets_route import pet_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp)
