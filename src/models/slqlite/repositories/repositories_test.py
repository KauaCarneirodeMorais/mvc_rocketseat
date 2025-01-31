# pytest -s -v src/models/slqlite/repositories/repositories_test.py
import pytest
from src.models.slqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_delete_pet():
    name = 'belinha'
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)
