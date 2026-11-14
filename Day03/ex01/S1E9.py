from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change the state of the character to dead."""
        pass


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark character."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Change the state of the character to dead."""
        self.is_alive = False
