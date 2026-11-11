import sys
from ft_filter import ft_filter


def main():
    """Filters words from a string that have a length greater than N."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        text = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        assert all(c.isalnum() or c.isspace() for c in text), (
            "the arguments are bad"
        )
        result = [
            word for word in ft_filter(lambda w: len(w) > n, text.split())
        ]
        print(result)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
