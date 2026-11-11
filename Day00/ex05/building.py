import sys
import string


def check_text(text: str) -> None:
    """Counts and displays the sums of upper-case characters, lower-case

    characters, punctuation marks, spaces, and digits in the provided text.
    """
    upp_let = sum(1 for c in text if c.isupper())
    low_let = sum(1 for c in text if c.islower())
    ponct_mar = sum(1 for c in text if c in string.punctuation)
    space = sum(1 for c in text if c.isspace())
    digit = sum(1 for c in text if c.isdigit())
    char_count = len(text)

    print(f"The text contains {char_count} characters:")
    print(f"{upp_let} upper letters")
    print(f"{low_let} lower letters")
    print(f"{ponct_mar} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """Main function to handle argument validation and prompt
    user if needed."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1 or sys.argv[1] is None or sys.argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        check_text(text)
    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
