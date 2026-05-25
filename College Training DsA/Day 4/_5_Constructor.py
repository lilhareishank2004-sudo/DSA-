class Student:
    def __init__(self):             #in python ' __init__ ' is the constructor. in python constructor does not have same name as class.
        print("default constructor")
    def show(self):
        print("I am in show")
s=Student();
s.show();