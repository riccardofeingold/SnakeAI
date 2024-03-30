from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def spawn(self) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def selfDestroy(self) -> None:
        pass