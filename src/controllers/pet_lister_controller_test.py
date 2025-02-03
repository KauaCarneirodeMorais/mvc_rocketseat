from src.models.slqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluff", type="Cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=17)
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expeted_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluff", "id": 4 },
                {"name": "Buddy", "id": 17 }
            ]
        }
    }

    assert response == expeted_response
