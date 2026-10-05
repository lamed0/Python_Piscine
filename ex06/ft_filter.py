
def ft_filter(function, it):
    """Return an iterator containing items that pass the function."""
    if function is None:
        return iter([x for x in it if x])
    return iter([x for x in it if function(x)])
