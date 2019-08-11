# comment    single line comment

"""
comment   multiline comment
comment 
comment

"""

"""
first_num = int(input("Enter first number "))
secnd_num = int(input("Enter second number "))
add_result = first_num + secnd_num
sub_result = first_num - secnd_num
mul = first_num * secnd_num
div = first_num / secnd_num

remainder = first_num % secnd_num
print("---------Calculator--------")
print("Addition is ", add_result)
print("Substraction is", sub_result)
print("Mulptiplication is", mul)
print("Division is", div)
print("Remainder is ", remainder)
print("--- End Calculator ---")
"""

msg = "Hello World"
print("First char is", msg[0])
greet = "Good morning"
#print("Methods of string are : ", dir(msg))
#print("Message is %s and Greeting is %s " %(msg, greet))
#print("Message is {0} and Greeting is {1} ".format(msg, greet))
print("String method is ", msg.index("W"))
print("String method is ", msg.isupper())
print("String method is ", msg.upper())
print("String method is ", msg.strip())
print("Number of character are ", len(msg))
# var_name[start_index: end_index]   slicing operator
firsr_char = msg[0: msg.index("r") + 1]
print("Slicing values is ", firsr_char)
print("Character at even position are ", msg[::2])


