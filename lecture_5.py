# lecture 5

# Activity 1 - colour picker

print("\nACTIVITY 1\n")

# create the primary colours as constants
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

PRIMARY_COLOURS = [RED, YELLOW, BLUE]

# get the first colour from the user
colour1 = input("Enter the first colour:").lower()
while colour1 not in PRIMARY_COLOURS:
    print("The colour must be a primary colour.").lower()
    colour1 = input("Enter the first colour:")

# get the second colour from the user
colour2 = input("Enter the first colour:").lower()
while colour2 not in PRIMARY_COLOURS or colour1 == colour2:
    print("The colour must be a primary colour and be different to the previous colour.")
    colour2 = input("Enter the first colour:").lower()

# work out the secondary colour based on the two primary colours
if (colour1 == RED and colour2 == BLUE) or (colour1 == BLUE and colour2 == RED):
    secondary_colour = "purple"
elif (colour1 == YELLOW and colour2 == BLUE) or (colour1 == BLUE and colour2 == YELLOW):
    secondary_colour = "green"
else:
    secondary_colour = "orange"

# print the result
print("{} and {} makes {}".format(colour1, colour2, secondary_colour))


# Activity 2 (from class) - sum of numbers

print("\nACTIVITY 2\n")


total = 0

num = int(input("Enter a number"))
while num > 0:
    total += num
    num = int(input("Enter a number"))

print("The sum of the numbers is:", total)


# Activity 3 (from class) - Average rainfall

print("\nACTIVITY 3\n")


monthly_rainfall = []

num_of_years = int(input("Enter the number of years"))

for year in range(1, num_of_years+1):
    for month in range(1, 13):
        inches = float(input("Enter the rainfall for Year {} Month {} (in inches)".format(year, month)))
        monthly_rainfall.append(inches)

month_count = len(monthly_rainfall)
total_inches = sum(monthly_rainfall)
average_rainfall = total_inches/month_count

# Use a constant to hold the format since it is a string that is repeated in multiple places and never changed
PRINT_FORMAT = "{:>20}: {:>5.2f}"

print(PRINT_FORMAT.format("Num of Months", month_count))
print(PRINT_FORMAT.format("Total Rainfall", total_inches))
print(PRINT_FORMAT.format("Average Rainfall", average_rainfall))

