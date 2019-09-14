def addition_function(first_num, secnd_num):
    """
    This function will return the addition of two
    number.

    :param first_num: contain the first number.
    :type first_num: integer
    :param secnd_num: contain the second number.
    :type secnd_num: integer
    :returns: return the addition of given two numbers.
    :return type: integer
    :author: qxp

    """
    add_val = first_num + secnd_num
    return add_val


if __name__ == "__main__":

    first_val = int(input("Enter the first number : "))
    second_val = int(input("Enter the second number : "))
    addition_val = addition_function(first_val, second_val)
    print("Addition of {0} and {1} is {2}".format(first_val, second_val,
                                                          addition_val))