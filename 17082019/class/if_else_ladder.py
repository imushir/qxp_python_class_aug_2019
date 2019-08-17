num = int(input("Enter number : "))
even_check = num % 2 == 0
odd_check = num % 3 == 0
if(even_check):
    if(num < 10):
        print(num, "is even number and it is less than 10.")
    elif(num <= 50):
       print(num, "is even number and it is lies between 10 to 50")
    else:
        print(num, "is even number and it is greater than 50.")
else:
    if(odd_check):
       print(num, "is odd number and it is multiple of 3.")
    else:
        print(num, "is odd number and it not multiple of 3.")