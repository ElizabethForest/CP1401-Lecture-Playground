# activity 1 - pig latin
# TODO add more comments explaining whats happening


def main():
    word = input("enter a word").lower()
    vowels = "aeiou"

    while word != '.':
        if word[0] in vowels:
            pig_latin = word + "yay"

        else:
            # TODO include other possible methods
            count = 0
            for char in word:
                if char not in vowels:
                    count += 1
                else:
                    break
            pig_latin = word[count:] + word[:count] + "ay"

        print(pig_latin)
        word = input("enter a word")

    print("Thanks for playing")


main()
