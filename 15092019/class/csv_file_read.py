import csv
import os

file_location = os.path.abspath(os.path.dirname(__file__))
file_name = "test.csv"
file_path = os.path.join(file_location, file_name)
file_obj = open(file_path)
csv_read_obj = csv.reader(file_obj, delimiter="|")
for each_line in csv_read_obj:
    print("Each line is ", each_line)
file_obj.close()