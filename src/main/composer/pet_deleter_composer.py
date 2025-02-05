from src.models.slqlite.settings.connection import db_connection_handler
from src.models.slqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.pet_deleter_view import PersonDeleterView

def pet_deleter_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetDeleterController(model)
    view = PersonDeleterView(controller)

    return view
