"""
days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday", 12, 13)
print("Type of days is ", type(days))
print("First day is", days[0])
print("First three days are :", days[:3])
print("Even days are ", days[::2])
print("Number of days are ", len(days))

num_word = ["A", "B", "C", "D", 1, 2, 3, 4]
print("Type of varible is ", type(num_word))
print("First element ", num_word[0])
print("Element are ", num_word[0: 5])
num_word[0] = "Hello"
print("Changed list is ", num_word)
num_word.append("Z")
print("New list is ", num_word)
num_word.extend(["X", "Y", "M", 100, 200])
print("New extended list is ", num_word)
print("Number of elements are ", len(num_word))


var_month_map = {1: "Jan", 2: "Feb", 3: "Mar",
                 4: "Apr", 5: "May",
                 "Platform1": ["Koyna express", "Delhi Express"]}
print("First month is ", var_month_map[1])
print("Month value is ", var_month_map.get(5, "Non valid Month"))
print("Keys are : ", var_month_map.keys())
print("Values are : ", var_month_map.values())
var_month_map[6] = "Jun"
var_month_map.update({7: "July", 8: "Aug", 9: "Sep",
                      10: "Oct", 11: "Nov", 12: "Dec"})
print("Updated months are : ", var_month_map)
"""

set_one = {12, 14, "Demo"} # set((elements))
set_one.add(20)
set_one.update([10, 12, 50, "Hi"])
print("Set one is ", set_one)
print("Set dir is ", dir(set_one))
print("Length of set one is ", len(set_one))
set_two = set((1, 2, 3, "Hi", "Hello"))
print("Set two  is  ", set_two)
print("Length of set two is ", len(set_two))
combo_set = set_one.union(set_two)
print("Element of both sets are ", combo_set)
print("Length of combined sets is ", len(combo_set) )