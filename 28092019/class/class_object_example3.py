class Employee:
    def __init__(self):

        self.employee_code = "QXP123"
        self.employee_name = "ABCD"
        self.employee_dept = "Account"
    
    def get_employee_code(self):
        return self.employee_code
    
    def get_employee_name(self):
        return self.employee_name
    
    def get_employee_dept(self):
        return self.employee_dept
    
    def set_employee_code(self, emp_cd_val):
        self.employee_code = emp_cd_val
    
    def set_employee_name(self, emp_name_val):
        self.employee_name = emp_name_val
    
    def set_employee_dept(self, emp_dept_val):
        self.employee_dept = emp_dept_val

if __name__ == "__main__":

    employee_obj = Employee()
    employee_name = employee_obj.get_employee_name()
    employee_code = employee_obj.get_employee_code()
    employee_dept = employee_obj.get_employee_dept()
    print("Employee name ", employee_name)
    print("Employee code ", employee_code)
    print("Employee Department", employee_dept)


