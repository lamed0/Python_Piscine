import sys


def main():
    if len(sys.argv) < 3:
        print("AssertionError: the arguments are bad")
        return (1)
    elif sys.argv[1].isdigit() or sys.argv[2].isalpha():
        print("AssertionError: the arguments are bad")
        return (1)
    words = [
            word for word in sys.argv[1].split()
            if (len(word) > int(sys.argv[2]))
        ]
    print(words)


if __name__ == "__main__":
    main()
