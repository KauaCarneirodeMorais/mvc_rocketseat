from typing import Dict
from src.models.slqlite.repositories.people_repository import PeopleRepositoryInterface
from src.models.slqlite.entities.people import PeopleTable
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Pessoal não encontrada!")

        return person

    def __format_response(self, person: PeopleTable) -> Dict:
        return{
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pets_name": person.pets_name,
                    "pets_type": person.pets_type
                }
            }
        }
