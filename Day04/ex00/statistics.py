from math import sqrt
from numbers import Real


def ft_statistics(*args: Real, **kwargs: object) -> None:
    """Print the statistics requested by the keyword arguments."""
    operations = {"mean", "median", "quartile", "std", "var"}

    if not args or any(isinstance(value, bool) or not isinstance(value, Real)
                       for value in args):
        print("ERROR")
        return
    requested = [operation for operation in kwargs.values()
                 if isinstance(operation, str)]
    if any(operation not in operations for operation in requested):
        print("ERROR")
        return

    values = sorted(float(value) for value in args)
    count = len(values)
    mean = sum(values) / count

    if "mean" in requested:
        print("mean :", mean)

    if "median" in requested:
        middle = count // 2
        median = values[middle] if count % 2 else (
            values[middle - 1] + values[middle]
        ) / 2
        print("median :", median)

    if "quartile" in requested:
        def percentile(percent: float) -> float:
            position = (count - 1) * percent
            lower = int(position)
            upper = min(lower + 1, count - 1)
            fraction = position - lower
            return values[lower] + (values[upper] - values[lower]) * fraction

        print("quartile :", [percentile(0.25), percentile(0.75)])

    variance = sum((value - mean) ** 2 for value in values) / count

    if "std" in requested:
        print("std :", sqrt(variance))
    if "var" in requested:
        print("var :", variance)
