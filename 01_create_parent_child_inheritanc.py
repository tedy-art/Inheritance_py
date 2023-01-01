
# Creating a parent class Person
class person:
    def __init__(self, nm, age):
        self.name = nm
        self.age = age

class student(person):
    def __init__(self, nm, age, std, roll, mks):
        super().__init__(nm, age)
        self.standard = std
        self.roll = roll
        self.marks = mks

    def print_detials(self):
        print(f"student name is {self.name},\nage is {self.age},\nstandard is {self.standard},\nroll number is {self.roll},\nmarks are {self.marks}")

s1 = student('jay', 25, 12, 1, 85)
s1.print_detials()