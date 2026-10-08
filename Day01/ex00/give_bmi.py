

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI for each matching height and weight."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("arguments must be lists")

    if len(height) != len(weight):
        print(len(height), "+", len(weight))
        raise AssertionError("lists must have the same length")

    bmi = []

    for i in range(len(height)):
        if not isinstance(height[i], (int, float)):
            raise AssertionError("height values must be int or float")
        if not isinstance(weight[i], (int, float)):
            raise AssertionError("weight values must be int or float")
        if height[i] == 0:
            raise AssertionError("height cannot be zero")

        bmi.append(weight[i] / (height[i] ** 2))

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return whether each BMI value is above the specified limit."""
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise AssertionError("arguments should be a list and a digit.")
    bool = []
    for i in range(len(bmi)):
        if not isinstance(bmi[i], (int, float)):
            raise AssertionError("bmi values must be int or float")
        if bmi[i] > limit:
            bool.append("True")
        else:
            bool.append("False")
    return bool
