
def main():
    enrolled = get_boolean("Are you enrolled to vote?")
    citizen = get_boolean("Are you an australian citizen?")

    if enrolled and citizen:
        print("You should vote!")


def get_boolean(prompt):
    value = input(prompt).lower()
    while value not in ["yes", "no"]:
        print("Answer must be yes or no.")
        value = input(prompt).lower()

    is_yes = (value == "yes")
    return is_yes


main()
