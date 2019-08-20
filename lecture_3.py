# lecture 3 activities

# activity 3

# get the number to be converted from the user
number = int(input("Enter a number between 1 and 5 to be coverted to a roman numeral:"))

# decide what to print based on the number entered
if number == 1:
    print("The roman numeral is I")
elif number == 2:
    print("The roman numeral is II")
elif number == 3:
    print("The roman numeral is III")
elif number == 4:
    print("The roman numeral is IV")
elif number == 5:
    print("The roman numeral is V")
else:  # if the number isn't between 1 and 5 print an error message
    print("Error! The value must be between 1 and 5")


# activity 4

# get the number of books purchased from the user
books_purchased = int(input("Enter the number of books purchased:"))

# by default (if no books are purchased) they are given 0 points
points = 0

# assign points based on the number of books purchased
if books_purchased == 1:
    points = 5
elif books_purchased == 2:
    points = 15
elif books_purchased == 3:
    points = 30
elif books_purchased >= 4:
    points = 60

print("You have been awarded", points, "points!")
