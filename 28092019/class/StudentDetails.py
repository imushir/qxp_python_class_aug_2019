class Student:
    def __init__(self, *student_info):
        self.student_name = student_info[0]
        self.student_age = student_info[1]
        self.student_dob = student_info[2]
        self.student_blood_group = student_info[3]
        self.student_branch = student_info[4]
    
    def print_student_details(self):
        print("---- Student Informatin is ------ ")
        print("Name :", self.student_name)
        print("Age :", self.student_age)
        print("Date of Birth is : ", self.student_dob)
        print("Blood Group is : ", self.student_blood_group)
        print("Brach is : ", self.student_branch)
    
    def set_branch_name(self, set_name_val):
        self.student_branch = set_name_val
        print("Student Brach Changed to ", self.student_branch)


if __name__ == "__main__":
    input_fields = ["name", "age", "dob", "blood_group", "branch"]
    student_info = []
    for each_field in input_fields:
        user_input = input("Enter Student {} ".format(each_field))
        student_info.append(user_input)
    student_obj = Student(*student_info)
    student_obj.print_student_details()
    student_obj.set_branch_name("Computer")
        