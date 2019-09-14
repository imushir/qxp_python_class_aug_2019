a = 10
b = 0
numbers = [1, 2, 3, 4, 5, 6]
lenght_list = len(numbers)

try:
    div_val = a / b
    list_val = numbers[lenght_list  + 1]
except IndexError as indx_except:
    print("LIST index is out of range") 
except ZeroDivisionError as zero_excpt:
    print("Cannot divide by Zero.")
except Exception as base_except:
    print("In BASE exception ")
    print("Base Error is ", base_except)
else:
    print("In else")  # else block will excecuted when try block is success.
finally:
    print("Success")
    print("Do all database, file closing in final block")
    print("Finally Executed required statements")
