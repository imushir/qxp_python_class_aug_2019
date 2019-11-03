import sys

if __name__ == "__main__":

    sys_args = sys.argv
    print("System argument are : ", sys_args)
    if len(sys_args) == 3:
        first_num, second_num = int(sys_args[1]), int(sys_args[2])
        add_result = first_num + second_num
        print("Addition is ", add_result)
    else:
        print("Two parameters are required ")
    