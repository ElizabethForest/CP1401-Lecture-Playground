# activity 1 - pig latin
# TODO add more comments explaining whats happening
VOWELS = "aeiou"


def main():
    word = input("enter a word").lower()
    while word != '.':
        if word[0] in VOWELS:
            pig_latin = word + "yay"

        else:
            pig_latin = translate_1(word)

        print(pig_latin)
        word = input("enter a word")

    print("Thanks for playing")


def translate_1(word):
    """ This function develops the pig latin word by keeping count of the current index until the first vowel is reached
    and then using the index to split the string """
    count = 0
    for char in word:
        if char not in VOWELS:
            count += 1
        else:
            return word[count:] + word[:count] + "ay"


def translate_2(word):
    """ This function keeps track of both sections of the word, removing from the beginning of the word and adding to
    the result until the first letter of the word is a vowel"""
    result = ""

    while len(word) != 0 and word[0] not in VOWELS:
        result += word[0]
        word = word[1:]

    return word + result + "ay"


def translate_3(word):
    """ This function works very similarly to translate_1 but instead of keeping track of the current index uses the
    .index() function to find the first occurrence of a vowel """

    for char in word:
        if char in VOWELS:
            first_vowel = word.index(char)
            return word[first_vowel:] + word[:first_vowel] + "ay"


main()
