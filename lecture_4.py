# lecture 4 activities

# activity 2

num = int(input("Enter your number:"))

# use mod (%) to work out if the number is even or odd - an even number will always evenly divide by 2
if (num % 2) == 0:
    print("number is even")
else:
    print("number is odd")


# activity 3 and 4

num = int(input("Please enter a number:"))
# keep getting the user to enter a number until the number is between 0 and 100
while not 0 < num < 100:  # this is the same as `while num <= 0 or num >= 100` or `not (0 < num and num < 100)`
    print("Number should be between 0 and 100")
    num = int(input("Please enter a number:"))

print("The times table for", num, "is:")

# for each value from 1 - 12 print out the times table
for multiple in range(1, 13):  # range is inclusive of the start value (1) but exclusive of the end value (13)
    total = multiple * num
    print(num, "*", multiple, "=", total)


# activity 5

rows = int(input("enter number of rows:"))

stars = ""

for i in range(rows):
    stars += "* "
    print(stars)
