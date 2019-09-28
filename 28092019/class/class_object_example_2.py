class Lion:
    def __init__(self, name, color, age):
        print("Init is called")
        self.name = name
        self.color = color
        self.age = age
    
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
    
    def set_lion_name(self, changed_name):
        self.name = changed_name

if __name__ == "__main__":

    lion_obj = Lion("BBB", 34, "White" )
    lion_obj.get_lion_name()
    lion_obj.get_lion_age()
    lion_obj.get_lion_color()
    lion_obj.set_lion_name("ZZZZ")
    lion_obj.get_lion_name()