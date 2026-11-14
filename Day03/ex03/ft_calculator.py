class calculator:
    """A calculator class that performs scalar operations on a vector."""

    def __init__(self, vector: list):
        """Initialize the calculator with a vector."""
        self.total = list(vector) if vector is not None else []

    def __add__(self, scalar: float) -> None:
        """Add a scalar to each element in the vector."""
        self.total = [val + scalar for val in self.total]
        print(self.total)

    def __mul__(self, scalar: float) -> None:
        """Multiply each element in the vector by a scalar."""
        self.total = [val * scalar for val in self.total]
        print(self.total)

    def __sub__(self, scalar: float) -> None:
        """Subtract a scalar from each element in the vector."""
        self.total = [val - scalar for val in self.total]
        print(self.total)

    def __truediv__(self, scalar: float) -> None:
        """Divide each element in the vector by a scalar."""
        if scalar == 0:
            raise ZeroDivisionError("division by zero is not allowed.")
        self.total = [val / scalar for val in self.total]
        print(self.total)
