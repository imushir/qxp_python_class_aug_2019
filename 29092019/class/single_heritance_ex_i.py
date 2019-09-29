class Person(object):

    country = "India"  # class variable

    def __init__(self, name_val, age_val, education_val):
        self.person_name = name_val
        self.person_age = age_val
        self.person_edu = education_val

    def isPerson(self):
        return True

    def get_person_details(self):
        return "Name : {0} \nAge : {1}\nEducation : {2}".format(self.person_name,
                                              self.person_age, self.person_edu)

class Employee(Person):

    def __init__(self, name, age, edu, emp_code, emp_department):
        super(Employee, self).__init__(name, age, edu)
        self.employee_code  = emp_code
        self.employee_deparment = emp_department
        
    def get_all_details(self):
        person_details = self.get_person_details()
        print(person_details)
        print("Employee code is {}\nDepartment is {}".format(self.employee_code,
                                                            self.employee_deparment))

if __name__ == "__main__":

    emp_obj = Employee("AAA", "12", "B.E", "1234", "Fire")
    emp_obj.get_all_details()
    print("Country is ", Employee.country)
    emp_obj1 = Employee("BBB", "23", "M.E", "10101", "Accoutant")
    emp_obj1.get_all_details()
    print("Country is ", Employee.country) # accessing class attribute
