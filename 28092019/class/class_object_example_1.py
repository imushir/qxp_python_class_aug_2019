class Lion:
    def __init__(self):
        self.name = "Lion"
        self.color = "Brown"
        self.age = 12
    
    def walking(self):
        print("Lion is Walking")
    
    def eating(self):
        print("Lion is Eating")
    
    def get_lion_name(self):
        print("Lion Name is ", self.name)
    
    def get_lion_color(self):
        print("Lion color is ", self.color)
    
    def get_lion_age(self):
        print("Lion age is ", self.age)
    

if __name__ == "__main__":

    lion_obj = Lion()
    lion_obj.get_lion_name()
    lion_obj.get_lion_age()
    lion_obj.get_lion_color()
    lion_obj.walking()
    lion_obj.eating()