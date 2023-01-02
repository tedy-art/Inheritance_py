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

3) Multiple inheritance:
-> Python provides us a flexiblity to inherit Multiple base class in the child class

-> One child and Multiple paranets is Multiple inheritance.

e.g. 
    class p1:
        def m1(self):
            print("This is parent1 m1 method.")

    class p2:
        def m2(self):
            print("This is parnet2 m2 method.")

    class c(p1, p2):
        def m3(self):
            print("This is child m3 method.")

    jay = c()
    jay.m2()
    jay.m1()
    jay.m3()


4) Hirarchical inheritance:
-> One Parent and Multiple child is Hirarchical inheritance.

e.g.
    class p:
    def m1(self):
        print("This is parent m1 method.")

    class c1(p):
        def m2(self):
            print("This is child1 m2 method.")


    class c2(p):
        def m3(self):
            print("This is child2 m3 method.")

    jay = c1()
    jay.m2()
    jay.m1()

    viru = c2()
    viru.m1()
    viru.m3()

5) Hybrid inheritance:
-> combination of all types of inheritance is Hybrid inheritance.
-> inheritance consisting of Multiple types of inheritance is called Hybrid inheritance

e.g.
        class school:
            def func1(self):
                print("This function is in school.")

        class student1(school):
            def func2(self):
                print("This function is in student1.")

        class student2(school):
            def func3(self):
                print("This function is in student2.")

        class student3(student1, school):
            def func4(self):
                print("This function is in student3.")

        print('*'*10, "student3", '*'*10)
        o1 = student3()
        o1.func1()
        o1.func2()
        o1.func4()

        print('*'*10, "student2", '*'*10)
        o2 = student2()
        o2.func1()
        o2.func3()

        print('*'*10, "student1", '*'*10)
        o3 = student1()
        o3.func1()
        o3.func2()

        print('*'*10, "School", '*'*10)
        o4 = school()
        o4.func1()

6) Cyclic inheritance:-
Python does not support Cyclic inheritance.