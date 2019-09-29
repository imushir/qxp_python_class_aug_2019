class Addition:
    def __init__(self, frts_nm, scnd_num):
        self.x_num = frts_nm
        self.y_num = scnd_num
    
    def add_result(self):
        return self.x_num + self.y_num

class Multiplication:
    def set_num(self, a_num, b_num):
        self.p_num = a_num
        self.q_num = b_num
    
    def mul_result(self):
        return self.p_num * self.q_num

class Calculator(Addition, Multiplication):
    def __init__(self, f_num, s_num):
        super(Calculator, self).__init__(f_num, s_num)
        self.set_num(f_num, s_num)
    
    def get_add_result(self):
        add_rslt = self.add_result()
        return add_rslt

    def get_mul_result(self):
        mul_rslt =self.mul_result()
        return mul_rslt

if __name__ == "__main__":

    user_input_one = int(input("Enter the first value :"))
    user_input_two = int(input("Enter the second value :"))
    cal_obj = Calculator(user_input_one, user_input_two)
    print("Method Resolution Order is ", Calculator.__mro__)  # to check method accessing order
    print("Addtion is ", cal_obj.get_add_result())
    print("Multiplication is ", cal_obj.get_mul_result())