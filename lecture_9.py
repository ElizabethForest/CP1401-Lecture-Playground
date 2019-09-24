# A list holds a series of data - defined using []
eg_list = [1, 2, 3]
print(eg_list)

# can use [] to directly access an element at that index
print(eg_list[2])

# lists are mutable so they can be modified
eg_list.reverse()
print(eg_list)

# A tuple also holds a series of data
# A tuple is immutable - cannot be modified
eg_tuple = (1, 2, 3)
print(eg_tuple)

# can still use [] to directly access an element at that index
print(eg_tuple[2])

# tuples are defined using a , and optional () - must have a ,
a = (1, 2)  # tuple
b = 1, 2  # tuple
c = 1,  # tuple
e = (1)  # int

f = ("fish" == "animal")  # boolean
g = ("fish" == "animal",)  # tuple

# a dictionary holds a series of key value pairs - defined by {} with a : to seperate the key and value
eg_dict = {"sven": 34, "bob": 56}
print(eg_dict)

# can use [] to directly access a value by its key
print(eg_dict["sven"])

# can set/override values using dict[key] = value
eg_dict["bob"] = 45
eg_dict["john"] = 23
print(eg_dict)

# can use .update() to combine dictionaries
eg_dict.update({"smith": 39})
print(eg_dict)

# can use the del keyword to remove an element from the dictionary
del eg_dict["john"]
print(eg_dict)

# when iterating over a dictionary the key is the iterator
for key in eg_dict:
    print(key, eg_dict[key])


# Lecture Activity 2
def get_sum_of_list(list):
    total = sum(list)
    return total


print(get_sum_of_list([2, 2, 3, 4, 5]))


# Lecture Activity 3 - States

states_caps = {
    "QLD": "Brisbane",
    "NQ": "Townsville",
    "NSW": "Melbourne",
    "VIC": "Sydney"
}

print(len(states_caps))
print(states_caps)

del states_caps["NQ"]
states_caps["ACT"] = "Canberra"
states_caps["NT"] = "Darwin"
states_caps.update({"SA": "Adelaide", "TAS": "Hobart", "NSW": 'Sydney'})

states_caps["VIC"] = "Melbourne"

print(len(states_caps))
print(states_caps)


# Lecture Activity 4 - Rainfall

def main():
    print("This program calculates average rainfall")
    years = int(input("how many years?"))

    rainfall_values = []

    for year in range(1, years + 1):
        rainfall = float(input("Enter rainfall for year " + str(year)))
        rainfall_values.append(rainfall)

    # convert the list to a tuple - can use list() to turn back
    rainfall_tuple = tuple(rainfall_values)

    total = sum(rainfall_tuple)
    count = len(rainfall_tuple)
    avg = total / count

    print("avg rainfall = ", avg)


main()


def retirement_calculator():
    people = int(input("How many peoples retirement year would you like to calculate?"))

    people_dict = {}

    for person in range(1, people + 1):
        print("Details for person number", person)
        name = input("What is their name?")
        birth_year = int(input("What year were they born in?"))
        people_dict[name] = birth_year

    print(people_dict)

    for person in people_dict:
        print(person, "will be able to retire in:", people_dict[person] + 70)


retirement_calculator()
