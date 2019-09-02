# Lecture 6 Activity 2

# import the randint function so we can use it later
from random import randint


def main():
    print("Welcome to Tropical Bowling")

    # initialise the variable that will hold the cumulative total
    running_total = 0

    # use a for loop for the 10 frames of the game
    for frame_num in range(1, 11):
        # \n in a string inserts a line break
        print("\nFrame", frame_num)

        # get a random number between 0 and 10 (inclusive)
        ball_one = randint(0, 10)
        print("Ball one:", ball_one)

        # get the number of pins remaining then get a random number between 0 and the number of pins remaining
        remaining_pins = 10 - ball_one
        ball_two = randint(0, remaining_pins)
        print("Ball two:", ball_two)

        # caculate the total for this frame
        frame_total = ball_one + ball_two
        print("Frame Total:", frame_total)

        # add the total for this frame to the running total
        running_total += frame_total
        print("Current Total:", running_total)

    print("\nThanks for playing! \nYour total score was {}!".format(running_total))


main()
