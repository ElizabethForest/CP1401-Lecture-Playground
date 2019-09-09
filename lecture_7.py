# Lecture 7
# Lists, Functions, and Scope

# imports go at the top of the file
import random
import math

# constants after imports
MAX_TEMP = 40


# main is the first function
def main():
    fahrenheit = convert_to_fahrenheit(int(input("what is the temp:")))
    print("fahrenheit:", fahrenheit)

    list = ["a", "b", "A", "B"]  # define a list
    list.append("c")  # appends "c" to the end of the list
    list.remove("B")  # removes the first instance matching "B" from the list
    list.sort()  # sorts the list (ascending order)
    list.reverse()  # reverses the order of the list
    print(list)


# then any other functions
def convert_to_fahrenheit(celsius):
    """ Converts a celsius value to fahrenheit """
    print("The celsius value is:", celsius)
    fahrenheit = celsius * 8 / 5 + 32
    return fahrenheit


# the last thing in the file is the call to main
main()
