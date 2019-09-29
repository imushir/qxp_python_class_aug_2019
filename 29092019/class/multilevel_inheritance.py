class Animal():
    def __init__(self):
        self.animal_class = "Animal Base"

    def walking(self):
        print("I am Animal Base class I can walk")
    
    def color(self):
        print("I am Animal Base class I have color")

class Horse_Male(Animal):
    def __init__(self):
        super(Horse_Male, self).__init__()
    
    def type_of_hrse_one(self):
        print("I am Male Horse")
    
    def horse_male_name(self):
        print("I am Bunty")
    
    def horse_male_color(self):
        print("Male Horse Colour is Black")

class Horse_Female(Horse_Male):
    def __init__(self):
        super(Horse_Female, self).__init__()

    def horse_female_name(self):
        print("I am Sweety")
    
    def type_of_hrse_two(self):
        print("I am Female Horse")
    
    def horse_female_color(self):
        print("Female Hourse Colour is White")


if __name__ == "__main__":

    fmle_hrse_obj = Horse_Female()
    print("My class is ", fmle_hrse_obj.animal_class)
    fmle_hrse_obj.horse_male_color()
    fmle_hrse_obj.horse_female_color()
    fmle_hrse_obj.color()
    fmle_hrse_obj.horse_female_name()
    fmle_hrse_obj.horse_male_name()