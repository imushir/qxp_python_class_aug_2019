from calculator_function import *
#from calculator_function import add, mul, div, sub


if __name__ == "__main__":

    print("File path from module is ", file_path)
    continue_flag = "Y"
    while continue_flag.lower() == "y":
        num_i = int(input("Enter the first number : "))
        num_ii = int(input("Enter the second number : "))
        choice = input(("Enter your choice\n1 for Addition\n2 for Substraction\n3" \
            " for Multiplication\n4 for Division\n"))
        if choice == "1":
            print("Addition of {} and {} is {}".format(num_i, num_ii,
                                                add(num_i, num_ii)))
        elif choice == "2":
            print("Substraction of {} and {} is {}".format(num_i, num_ii,
                                                sub(num_i, num_ii)))
        elif choice == "3":
            print("Multiplication of {} and {} is {}".format(num_i, num_ii,
                                                mul(num_i, num_ii)))
        elif choice == "4":
            print("Division of {} and {} is {}".format(num_i, num_ii,
                                                div(num_i, num_ii)))
        else:
            print("Invalid choice")
        continue_flag = input("Do want to you continue y or n : ")


