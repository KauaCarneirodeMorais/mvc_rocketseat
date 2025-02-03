from src.models.slqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetDeleterController:
    def __init__(self, pet_repository: PetsRepositoryInterface):
        self.__pet_repository = pet_repository

    def deleter(self, name: str) -> None:
        self.__pet_repository.delete_pets(name)
