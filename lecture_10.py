# lecture 10

# string concatenation combines strings
hello_everyone = "hello " + "everyone"
print(hello_everyone)

# strings are sequences so they can be iterated over and have characters directly accessed
for char in hello_everyone:
    print(char)

print(hello_everyone[1], hello_everyone[-1])

# acts the same as a string
my_string = ['h', 'e', 'l', 'l', 'o']
print(my_string[1], my_string[-1])

# can use splicing to get substrings [start:end:step]
print(hello_everyone[0:5])
print(hello_everyone[1:-1:3])
print(my_string[1:4:2])

# string functions

"123".isdigit()  # true
"abc".isdigit()  # false
"abc123".isdigit()  # false
" ".isdigit()  # false
":)".isdigit()  # false

"123".isalpha()  # false
"abc".isalpha()  # true
"abc123".isalpha()  # false
" ".isalpha()  # false
":)".isalpha()  # false

"123".isalnum()  # true
"abc".isalnum()  # true
"abc123".isalnum()  # true
" ".isalnum()  # false
":)".isalnum()  # false

# example use of .isdigit()
value = input("age")
if value.isdigit():
    num = int(value)
else:
    print("must enter a number")

# use split to split a string by a character
print(hello_everyone.split())  # defaults to a space

print("10/10/19".split('/'))

# functions like .lower() and .upper() don't effect the underlying variable, only return the new value
name = "Joe"
print(name.lower())
print(name.upper())
print(name)
