import sys


def main():
    MORSE_CODE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    res = ""

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return (1)
    for i in sys.argv[1]:
        if not i.isalnum() and not i.isspace():
            print("AssertionError: the arguments are bad")
            return (1)
        res += MORSE_CODE[i.upper()] + " "
    print(res.rstrip())


if __name__ == "__main__":
    main()
