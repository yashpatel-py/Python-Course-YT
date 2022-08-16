class my_class:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def my_func(self):
        print('My name is ' + self.name)
    
    def my_age(self):
        print('My age is ', self.age)

# Creating object of a class
obj1 = my_class("yash patel", 23)

obj1.name = "Manav"
obj1.age = 21

del obj1

obj1.my_func()
obj1.my_age()



# print(obj1.name)
# print(obj1.age)