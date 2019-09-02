# Lecture 6

# refresher on mod
num = int(input("Enter a number:"))

if num % 2 == 0:  # Check if a number is even using num mod 2
    print(num, "is just even")
elif (num % 2 == 0) and (num % 3 == 0):
    # this condition will never run because the condition before would run first
    # the most specific condition should always be first
    print(num, "is even and divisible by 3")
else:
    print(num, "is odd")


# Activity 1

def main():
    print("Welcome to tropical Auto")

    name = input("Enter your name:")

    age = int(input("Enter your age:"))

    # use .lower() to convert the string to lower case
    car_type = input("Please choose your car type: (C) Compact - $25, (S) SUV - $45, (H) Hummer - $100").lower()
    while car_type not in ["c", "s", "h"]:
        print("Car type must be c, s, or h")
        car_type = input("Please choose your car type: (C) Compact - $25, (S) SUV - $45, (H) Hummer - $100").lower()

    days = int(input("Please enter the number of days for the rental: (must be greater than 0)"))
    while not (days > 0):
        days = int(input("Sorry days for rental must be greater than 0. Please enter days for rental again:"))

    print("Thank you for your reservation")

    if car_type == "c":
        base_price = 25 * days
    elif car_type == "s":
        base_price = 45 * days
    else:
        base_price = 100 * days

    if age < 25:
        youth_tax = base_price * .3
    else:
        youth_tax = 0

    total_price = base_price + youth_tax

    print("Your total is as follows:")
    # see the last 3 slides of the week 5 lecture for details on the .format() function
    print("Base rental: ${:.2f}".format(base_price))
    print("Youth tax: ${:.2f}".format(youth_tax))
    print("Total rental cost: ${:.2f}".format(total_price))


main()
