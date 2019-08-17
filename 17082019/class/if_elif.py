day_val = input("Enter Day Char m or t or w or th or f or sa or su: ")
day_char = day_val.lower()
if day_char in ["m", "t", "w", "th", "f", "sa", "su"]:
    if day_char == "m":
        print("Today is Monday.")
    elif day_char == "t":
        print("Today is Tuesday.")
    elif day_char == "w":
        print("Today is Wednesday.")
    elif day_char == "th":
        print("Today is Thursday.")
    elif day_char == "f":
        print("Today is Friday.")
    elif day_char.startswith("s"):
        print("Today is Weekend.")
        if day_char == "sa":
            print("Weekend is Saturday.")
        else:
            print("Weekend is Sunday.")
    else:
        print("Day is not valid")
else:
    print("Invalid Day char")