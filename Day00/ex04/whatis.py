import sys


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            return
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
