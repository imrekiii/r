class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def print_info(self):
        if self.name:
            print("Name:", self.name)
        if self.age:
            print("Age:", self.age)