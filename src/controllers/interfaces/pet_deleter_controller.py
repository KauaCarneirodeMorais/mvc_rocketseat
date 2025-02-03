from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):

    @abstractmethod
    def deleter(self, name: str) -> None:
        pass
