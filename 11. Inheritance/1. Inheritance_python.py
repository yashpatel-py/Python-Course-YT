class teacher:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
    
    def full_name(self):
        print(self.f_name, self.l_name)

class student(teacher):
    pass

obj1 = student("Yash", "Patel")
obj1.full_name()