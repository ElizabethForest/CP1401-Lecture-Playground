# Leap Year Task


def main():
    year = int(input("Enter the year"))
    # call the function calculate_leap_year passing in the variable `year`
    calculate_leap_year(year)


def calculate_leap_year(year):
    """ Prints whether a given year is a leap year """
    if year % 400 == 0:
        print(year, "is a leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


main()

# Magic 8-ball task
import random


def main():
    print("Welcome to magic 8-ball!")
    playing = True

    while playing:
        question = input("What would you like to ask the Magic 8-ball?")

        # call the function get_random_answer and assign the value that is returned to the variable `answer`
        answer = get_random_answer()
        print("the answer to:\n", question, "\n is:", answer)

        play_again = input("Would you like to play again?").lower()
        # set playing to the boolean (True/False) value of whether the value for play_again equals "yes"
        playing = play_again == "yes"

    print("Thanks for playing!")


# get_random answer takes no parameters and returns a randomly selected magic 8-ball answer
def get_random_answer():
    possible_answers = ["No", "Yes", "Ask again later", "Definitely", "Maybe", "Doubtful", "I don't know",
                        "That's not a good question"]
    return random.choice(possible_answers)


main()
