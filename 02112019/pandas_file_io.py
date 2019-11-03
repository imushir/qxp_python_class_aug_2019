import pandas as pd
import os

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, "demo_file.csv")
out_put_csv = os.path.join(current_path, "marks.csv")

data_table = pd.read_csv(file_path, encoding="utf-8")
print("Data table is\n", data_table)


# to get each row
for each_row in data_table.iterrows():
    print("Each row is row ", each_row)



# list of name, degree, score 
students_name = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"] 
scr = [90, 40, 80, 98] 
   
# dictionary  
student_details = {'name': students_name, 'degree': deg, 'score': scr}
     
student_table = pd.DataFrame(student_details) 
  
# saving the dataframe 
student_table.to_csv(out_put_csv, index=False)