# Class:
# Class is the logical representation of things. It is like a blueprint or templet for the object

# Object: It is physical representation of the class and physical repesentation of things.

class Student:                      #Class creation.
    def show(self):                     #Function. In python first parameter in function is 'self'
        print("I am a show") 


#In C++: Object Creation:
# Student s;              #static object
# Student *s=new Student();       #Dynamic Object           

# In java
# Student s=new Student();
# always remember :     left side of equal to is name of object and right side is the object. 

#In Python
s=Student();
s.show();


# Constructor is used to initialise the member veriable that invoking object