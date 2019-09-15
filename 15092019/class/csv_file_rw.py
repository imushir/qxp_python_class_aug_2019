import csv
import os

file_location = os.path.abspath(os.path.dirname(__file__))
file_name = "test_write.csv"
file_path = os.path.join(file_location, file_name)
file_obj = open(file_path, "a", newline="\n")
csv_write_obj = csv.writer(file_obj, delimiter="#")
csv_write_obj.writerow(["HI", "Hello"])