def square(number):
    """Return the square of a number."""
    return number * number


def pow(number):
    """Return a number raised to its own power."""
    return number ** number


def outer(number, function):
    """Return a callable that repeatedly applies function to number."""
    count = 0

    def inner():
        nonlocal number, count
        count += 1
        number = function(number)
        return number

    return inner