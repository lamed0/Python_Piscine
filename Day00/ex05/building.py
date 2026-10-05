import sys


def check_text(object: str) -> int:
    """
    This function checks the string passed in
        argv and counts the character
    """
    Upp_Let = 0
    Low_Let = 0
    Ponct_Mar = 0
    Space = 0
    Digit = 0
    char = 0

    for i in object:
        if i.isupper():
            Upp_Let += 1
        elif i.islower():
            Low_Let += 1
        elif not i.isalnum() and not i.isspace():
            Ponct_Mar += 1
        elif i.isspace():
            Space += 1
        elif i.isdigit():
            Digit += 1
    char = Upp_Let + Low_Let + Ponct_Mar + Space + Digit
    print("The text contains", char, "characters:")
    print(Upp_Let, "upper letters")
    print(Low_Let, "lower letters")
    print(Ponct_Mar, "punctuation marks")
    print(Space, "spaces")
    print(Digit, "digits")
    return (0)


def main():

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return (1)
    if len(sys.argv) == 1:
        print("What is the text to count?", end="\n", flush=True)
        text = sys.stdin.read()
        check_text(text)
        return (0)
    check_text(sys.argv[1])


if __name__ == "__main__":
    main()
