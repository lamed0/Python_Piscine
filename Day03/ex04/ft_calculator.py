class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        result = sum(V1[i] * V2[i] for i in range(len(V1)))
        print("Dot product is:", result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the element-wise sum of two vectors."""
        result = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print("Add Vector is:", result)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the element-wise difference of two vectors."""
        result = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print("Sous Vector is:", result)


a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
