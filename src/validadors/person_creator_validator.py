from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.errors_types.http_unprocessable_entity import HttpUnProcessableEntityError

def person_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        first_name: constr(min_length=1) # type: ignore
        last_name: constr(min_length=1) # type: ignore
        age: int  = None # type: ignore
        pet_id: int # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnProcessableEntityError(e.errors()) from e
