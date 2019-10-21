SEP = ','
FILE = "word_list.txt"


def main():
    print("What would you like to do?")
    choice = input("(W)rite\n(R)ead\n(Q)uit\n").lower()
    while choice != "q":
        if choice == "w":
            write_to_file()
        elif choice == "r":
            read_from_file()
        else:
            print("Must enter w, r, or q")
        choice = input("(W)rite\n(R)ead\n(Q)uit\n").lower()


def write_to_file():
    amount_of_words = 0
    valid = False
    while not valid:
        try:
            amount_of_words = int(input("Enter the amount of words to add:"))
            valid = True
        except ValueError:
            print("Must enter a number")

    word_string = ""
    for i in range(amount_of_words):
        word = input("Enter word {}:".format(i+1))
        word_string += word + SEP

    print(word_string)

    try:
        file = open(FILE, 'w')
        file.write(word_string[:-1])
        file.close()
    except IOError as e:
        print("Could not write to file because:", e)


def read_from_file():
    try:
        file = open(FILE, 'r')
    except FileNotFoundError:
        print("File not found, run (w)rite first.")
    else:
        contents = file.read()
        file.close()

        word_list = contents.split(SEP)
        word_lengths = []
        longest_word = ""
        for word in word_list:
            length = len(word)
            word_lengths.append(length)
            if length > len(longest_word):
                longest_word = word

        print(word_list)
        print("Number of words:", len(word_list))
        print("The longest word is:", longest_word)
        print("The avg word length is:", sum(word_lengths)/len(word_lengths))


main()