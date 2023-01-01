What is inheritance??
    -> inheritance allows us to define a class that inherit all the methods and properties from another class.
    

    \\Parent class:
    It is the class being inherited from, also called base class.

    \\Child class:
    It is the class that inherit from, another class also called drived class.

    Parent class syntax:
        class class_name1:
                class_body
    
    e.g.
        class Person:
            def __init__(self, fname, lname):
                self.firstname = fname
                self.lastname = lname

            def print_name(self):
                print(self.firstname, self.lastname)

        x = Person('Jay','Doe')
        x.print_name()

    Child class syntax:

        class class_name(class_name1):
                body_of_child_class

    e.g.
        class Person:
            def __init__(self, fname, lname):
                self.firstname = fname
                self.lastname = lname

            def print_name(self):
                print(self.firstname, self.lastname)
        
        class student(Person):
            pass


        x = student('Jay','Doe')
        x.print_name()


***Types of inheritance:-
    1) Sample/single inheritance
    2) Multi-level inheritance
    3) Multiple inheritance
    4) Hirarchical inheritance
    5) Hybrid inheritance
    6) Cyclic inheritance


1) Sample/single inheritance
-> single Parent and single Child relation is called Sample/ single inheritance.

e.g.
        class P:
            def m1(self):
                print("This is parent m1 method")

        class c(P):
            def m2(self):
                print("This is child m2 method")

        jay = c()
        jay.m2()
        jay.m1()

2) Multi-level inheritance
-> Multi-level inheritance is archived when a drived class inherit another  class, there is no limit the number of levels up to which, the Multi-level inheritance is archived in python.
-> relation between GP, P and child is Multi-level inheritance.

e.g.
    class GP:
        def m3(self):
            print("This is Grand parent m3 method.")

    class P(GP):
        def m1(self):
            print("This is paranet m1 method.")

    class c(P):
        def m2(self):
            print("This is child m2 method")


    jay = c()
    jay.m2()
    jay.m1()
    jay.m3()