from src.models.slqlite.settings.connection import db_connection_handler
from src.models.slqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PersonListerView

def pet_lister_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetListerController(model)
    view = PersonListerView(controller)

    return view
