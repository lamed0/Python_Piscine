

def count_in_list(lst: list, word: str) -> int:
    """Return how many times word appears in lst."""
    return sum(item == word for item in lst)