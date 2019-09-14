# for loop and while loop

"""
msg = "Hello World"
days = ["Monday", "Tuesay","Wed", "Thur", "Fri", "Sat", "Sun"]
print("Number of days is ", len(days))
"""

"""
for ech_char in msg:
    print("Each char is ", ech_char)

for each_day in days:
    if each_day == "Sun":
        print("Today is", each_day, "and holiday..")
    if each_day.startswith("S"):
        if each_day == "Sat":
            continue
        print(each_day, "Its weekends")

# Get the values of dictionary

days_color = {"Mon": "Red", "Tue": "Green", "Wed": "Blue"}
print("Method and attributes are : ", dir(days_color))
for day, color in days_color.items():
    print("Day ", day)
    print("Color ", color)

for element in days_color.items():
    print("Day ", element[0])
    print("Color ", element[1])
"""

a = 0
while(a < 10):
    a = a + 1
    if a % 2 == 0 or a == 5:
    #    break
        continue
    print("Number is ", a)
