# oops 
# classes and objects 
##creating a class
# class Student:
#     name = "sania"
# #creating an object of the class    
# s1 = Student()
# print(s1.name)

# ##constructor are called when an object is being initiated
# class Student:
#    def __init__(this,name):  #we dont need to call it
#      this.name = name
#      print(name)
# s1 = Student("SANA")

# # methods in oop methods>>are the function in the oop

# class Subject:
#     def print(self,sub):
#        self.sub = sub
#        print(sub)

# s1 = Subject()
# s1.print("Physics")
# s1.print("Chemistry")
# s1.print("Maths")

# # Let‘s Practice
# # Create student class that takes name & marks of 3 subjects as arguments in constructor.
# # Then create a method to print the average.
# class student:
#    def __init__(self,marks):
#       self.marks = marks
#       print(marks)
#    def  avg(self):
#       sum = 0
#       for el in self.marks:
#          sum = el +sum
#       print(sum/3)
         
# s1 = student([1,2,3])   
# s1.avg()   


# # Staticmethod used when we dont passed any argument in the function
# # @staticmethod
# class student:
#    @staticmethod
#    def __init__():
#       print("hi Im a satic method") 
# s1 = student()
# # Fir pillers of oop
# # 1-Abstraction[hiding the implementation of class only showing essential information] 
# # 2-Encapsulation[Wrapping data and function into a single unit (object)] 
# # 3-Inheritance[one class inherit the properties of another class like a child inherit the properties from his parent]
# # 4-Polymorphism[poly-> many & morphism-> forms so polymorphism means many forms]

# # Create Account class with 2 attributes - balance & account no.
# class Account:
#    def __init__(self,bal,acc_no):
#       self.bal = bal
#       self.acc_no = acc_no
#       print(bal, end=" ")
#       print(acc_no)
      
# # Create methods for debit, credit & printing the balance.
#    def debit(self,deb):
#       self.deb = deb
#       t_amt = self.bal - self.deb
#       print("Total amont after debit",t_amt)

#    def credit(self, crd):
#       self.crd = crd
#       t_amt = self.bal + self.crd
#       print("Total amount after credit",t_amt)

      
# a1 = Account(2300, 3456) 
# a1.credit(1000)    
# 

# =====method overloading===== & ====method overriding =======
# metod overloading same function different parameters
 
class Addition():
    def add(sellf, a ,b):
        print(a + b)
    def add(self,a,b,c = 0): #incase we dont passed a value to c 
        print(a + b + c)
    def add(self,a,b,c = 0 , d = 0): #incase we dont passed a value to c and d
        print(a + b + c + d)
a1 = Addition()
a1.add(1,2) #3
a1.add(1,2,4) #7
a1.add(1,2,4,9) #16
print(end="\n")
# ===========individual Character ================
class Characters():
    # def prints(self,a, c ="" , d = ""): #incase we dont passed a value to c and d
    #     print(a , c , d)
    # def prints(self,a,c = ""): #incase we dont passed a value to c 
    #     print(a , c)
    def prints(self, *args):
        print(args)
   

a1 = Characters()
a1.prints('H') #H
a1.prints('E','L') #E,L
a1.prints('L','O','S') #L,O,S
print(end="\n")
# ===========Strings================
class Strings():
    def prints(sellf, a):
        print(a)
    def prints(self,a,c = ""): #incase we dont passed a value to c 
        print(a , c)
    def prints(self,a, c ="" , d = ""): #incase we dont passed a value to c and d
        print(a , c , d)
a1 = Strings()
a1.prints("Hello") #Hello
a1.prints("I'm","Sania") #I'm, Sania
a1.prints("I'm","Learn","Python") #I'm, Learn, Python

# # Definition: Method overriding ka matlab hai child class mein parent class ke method ko same name aur compatible 
# # parameters ke sath dobara define karna, taake uska behavior change ho jaye.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# # obj = Dog()
# obj = Animal()
# obj.sound()
# # # Inheritance
# # ================single inheritance===========
# class Animal:
#    def eat(self):
#       print("animal eat") 
# class Dog(Animal):
#    def bark(self):
#       print("dog bark") 
# d1 = Dog()
# d1.eat()
# d1.bark()  
# # ================multi-level inheritance===========
# class Uni:
#    def un_name(self,name):
#       self.name = name
#       print("Your University Name is:", name)
# class Student(Uni):
#    def info(self,name,roll_no):
#       self.name = name
#       self.roll_no = roll_no
#       print("your name is:",name)
#       print("your Roll Number is:",roll_no)
# class Marks(Student):
#    def print_marks(self,marks):
#       self.marks = marks
#       print("your marks list is:",marks) 
# s1 = Marks()
# s1.un_name("BZU")   
# s1.info("Sania", 1234)        
# s1.print_marks({"phy":77, "maths":89})
# # ================Multiple inheritance===========

# class Father:
#    def __init__(self):
#       print("Father Earn")
#       super().__init__()

# class Mother:
#    def __init__(self):
#       print("Mother cook")
#       super().__init__() 

# class Child(Father,Mother):
#    def __init__(self):
#       print("child eat") 
#       super().__init__()

# c1 = Child()              