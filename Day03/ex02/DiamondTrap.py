from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King inheriting from Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for King."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """Set the eye color of the King."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Set the hair color of the King."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self) -> str:
        """Get the hair color of the King."""
        return self.hairs
