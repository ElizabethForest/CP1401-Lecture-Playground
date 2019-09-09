# This is not a complete answer to activity 2 - only the start
# Try doing the rest for yourself!


def main():
    value = int(input("Enter a number between 1 and 26 to decode: "))

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z']

    index = value - 1
    print(letters[index])


main()
