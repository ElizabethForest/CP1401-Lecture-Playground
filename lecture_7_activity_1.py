def main():
    print("Welcome to your pay calculator :)")

    hours_worked = get_number_greater_than("Please enter the number of hours you worked this week (must be a positive whole number): ", 0)

    pay_rate = get_number_greater_than("Please enter your hourly pay rate (must be over 15): $", 15)

    pay = hours_worked * pay_rate
    print("This week you have earned $" + str(pay))


def get_number_greater_than(prompt, min_value):
    number = int(input(prompt))
    while number < min_value:
        print("That is not a valid value.")
        number = int(input(prompt))
    return number


main()
