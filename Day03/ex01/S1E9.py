from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive
    @abstractmethod
    def __str__(self):
        pass
    def die(self):
        pass



class Stark(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive = True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        return f"'first_name':", "'", "{self.first_name}", "'", ",", "'is_alive':", "{self.is_alive}"

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False