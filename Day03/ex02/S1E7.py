from S1E9 import Character 

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive = True, family_name = "Baratheon", eyes = "brown", hairs = "dark"):
            self.first_name = first_name
            self.is_alive = is_alive
            self.family_name = family_name
            self.eyes = eyes
            self.hairs = hairs

    def __str__(self) -> str:
        return (
            f"'first_name': '{self.first_name}', "
            f"'is_alive': {self.is_alive}, "
            f"'family_name': '{self.family_name}', "
            f"'eyes': '{self.eyes}', "
            f"'hairs': '{self.hairs}'"
        )

    def __repr__(self) -> str:
          return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
          self.is_alive = False

class Lannister(Character):
    def __init__(self, first_name, is_alive = True, family_name = "Lannister", eyes = "blue", hairs = "light"):
            self.first_name = first_name
            self.is_alive = is_alive
            self.family_name = family_name
            self.eyes = eyes
            self.hairs = hairs

    def __str__(self) -> str:
        return (
            f"'first_name': '{self.first_name}', "
            f"'is_alive': {self.is_alive}, "
            f"'family_name': '{self.family_name}', "
            f"'eyes': '{self.eyes}', "
            f"'hairs': '{self.hairs}'"
            )

    def __repr__(self) -> str:
          return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        return cls(first_name, is_alive)
