# credit card company

# outstanding limit - 5000
# min repayment - 10%


def main():
    outstanding_balance = get_validated_outstanding_balance()

    repayment = get_validated_repayment(outstanding_balance)

    new_balance = outstanding_balance - repayment
    print("Payment received. Your balance is now: ${}".format(new_balance))


def get_validated_outstanding_balance():
    outstanding_balance = get_valid_int("Enter the outstanding balance:",
                                        "Outstanding balance must be between 0 and 5000",
                                        0,
                                        5000)
    return outstanding_balance


def get_validated_repayment(outstanding_balance):
    min_repayment = outstanding_balance * .1
    repayment = get_valid_int("Enter your repayment:",
                              "Payment must be at least 10% of the outstanding payment. You must pay at least ${}".format(min_repayment),
                              min_repayment,
                              outstanding_balance)
    return repayment


def get_valid_int(prompt, error_message, minimum_value, maximum_value):
    """ Gets an int from the user, ensuring it is between a minimum and maximum value (inclusive)

    Parameters
    ----------
    prompt : str
        The prompt to display asking the user for input (expects an int)
    error_message : str
        The message to displays if the user puts in a wrong value
    minimum_value : int
        The minimum the value can be (inclusive)
    maximum_value : int
        The maximum the value can be (inclusive)

    Returns
    -------
    The int value entered by the user between the minimum and maximum
    """
    value = int(input(prompt))
    while value < minimum_value or value > maximum_value:
        print(error_message)
        value = int(input(prompt))
    return value


main()
