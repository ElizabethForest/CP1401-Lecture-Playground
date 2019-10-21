# Lecture 11 - week 12

# files

file = open("test.txt", "w")  # opens the file with write - will override
file.write("This file contains some text")
file.close()

file = open("test.txt", "r")  # opens the file to read from it
for line in file:
    print(line)
file.close()

# Exception handling

try:
    num1 = int(input("num1"))
    num2 = int(input("num2"))
    print(num1 / num2)
except ValueError:
    # will occur when there is a value (cannot convert value to int in int())
    print("You must enter two numbers")
except ZeroDivisionError:
    # will occur when there is a divide by 0 error (num2 == 0)
    print("You cannot divide by 0")
except Exception as e:
    # will occur if any other error occurs
    print("Could not do division because of ", type(e), "error:", e)
