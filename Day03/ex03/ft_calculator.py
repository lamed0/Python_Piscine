class calculator:
        def __init__(self, vector=None):
            """Initialize the calculator with a vector of values."""
            self.total = list(vector) if vector is not None else []

        def __add__(self, object):
            """Add a scalar to every value in the vector."""
            self.total = [value + object for value in self.total]
            print (self.total)

        def __mul__(self, object) -> None:
            """Multiply every value in the vector by a scalar."""
            self.total = [value * object for value in self.total]
            print (self.total)

        def __sub__(self, object) -> None:
            """Subtract a scalar from every value in the vector."""
            self.total = [value - object for value in self.total]
            print(self.total)

        def __truediv__(self, object) -> None:
            """Divide every value in the vector by a scalar."""
            if object == 0:
                raise AssertionError("It's not allowed")
            self.total = [value / object for value in self.total]
            print(self.total)
