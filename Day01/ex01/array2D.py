import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the array shapes and return the selected rows."""
    if (not isinstance(family, list)
        or not isinstance(start, int)
            or not isinstance(end, int)):
        raise AssertionError("The arguments are incorrect.")

    array = np.array(family)
    sliced = array[start:end]

    print("My shape is :", array.shape)
    print("My new shape is :", sliced.shape)

    return sliced.tolist()
