class Add:
    def __init__(self, num_a, num_b):
        self.first_num = num_a
        self.secnd_num = num_b
    
    def get_add_result(self):
        add = self.first_num + self.secnd_num
        return add
    
    def print_result(self):
        print("Addition result is :", self.get_add_result())


class Sub(Add):
    def __init__(self, num_x, num_y):
        super(Sub, self).__init__(num_x, num_y)
        self.first_val = num_x
        self.secnd_val = num_y
    
    def get_sub_result(self):
        sub = self.first_val - self.secnd_val
        return sub
    
    def print_result(self): # override method of base class
        Add.print_result(self)
        print("Substraction result is : ", self.get_sub_result())

if __name__ == "__main__":
    sub_obj = Sub(30, 20)
    sub_obj.print_result()