class NameFirst:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
           
    def get_full_name(self):
        print(self.first_name + self.last_name)
    
        
class  NameLast(NameFirst):
    def __init__(self, age, first_name, last_name):
        super().__init__(first_name, last_name)
        self.age = age
    
    def getAge(self):
        print(self.age)
        
nm = NameLast(20, "John", "Doe")
nm.get_full_name()
nm.getAge()      
    