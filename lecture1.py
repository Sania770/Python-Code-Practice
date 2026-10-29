# Variables and data type 

# print statemnet
# print("hello", end=" ")
# print("World")
#input statement
# name = input("enter Your name:")
# print("Your name is:", name)
# age = 19
# marks = 99.9
# print("Your age is:", age)
# print("Your marks are:", marks)
# print("type of name is",type(name))
# how to find the type of a variable
# print(type(age))
# print(type(marks))
# char = '123'
# print("The type of 'A' is:",type(char)) #string
# char = 123
# print("The type of '123' is:",type(char)) #integer
# char = 22.2
# print("The type of '22.2' is:",type(char)) #float
# char = False
# print("The type of 'False' is:", type(char)) #boolen
# char = None
# print("The type of empty space is:", type(char)) #nonetype
#Print Sum
# a = 12
# b = 10
# print(a+b)
# sum = a + b
# print("sum of two numbers a and b is :",sum)
# comment in python single comment 
""" 
multi line comment
""" 
# operator in python 
# Arithmetic operator 
# a = 12
# b = 10
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(int(12/12))
# print(a%b) # the remainder of a/b 
# print(a**b) # the b is the power of a means a
# Relational/comparison  operator 
# a = 12
# b = 10
# print(a==b) # False
# print(a!=b) # True
# print(a>=b) #True
# print(a<=b) #False
# print(a<b)  #False
# print(a>b)  #True
# Assignment operator
# a = 11
# a += 1 # 11+1 = 12
# print(a) #12
# a -= 1 # 12-1 = 11
# print(a) #11
# a *= 1 # a=a*1 or 11*1=11
# print(a) #11
# a /= 1 # a=a/1 or 11/1=11
# print(a) #11
# a = 13
# a **= 2 # a=a^2 or 13^2=13
# print(a) #169
#logical operator
# a = True
# b = False
# print(a != b ) # True
# print(a and b) # False
# b = True
# print(a and b) # True
# print(a or b ) # True
"""the type conversion is not allow in python such as if a = 1 integer and b = "2" 
basically it is a integer but the compiler understand it as a string so we cannot calculate the sum of a & b.
such as sum = a + b # throug an error
 """
# a = 1
# b = "2" 
# sum = a + b
# print(sum) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

""" for handling these type of situation we used type casting
if we summarize the above example the solution with type casting is as follows.
"""
# a = 12
# b = "22"
# c = int(b) #type casting
# sum = a+c
# print(sum) # 12+22 = 34
#input statement always takes a string so before taking a input we convert its typee through type casting
# num = input("enter a number:")
# print("before type conversion: ",num,type(num))#string
# num = int(input("enter a number:"))
# print("after type conversion in integer: ",num,type(num))#this time the type is integer
# num = float(input("enter a number:"))
# print("after type conversion in float: ",num,type(num))#this time the type is float
# practice question1
# Write a Program to input 2 numbers & print their sum.
# num1 =int( input("enter a number:"))
# num2 =int( input("enter a number:"))
# sum = num1 + num2
# print("sum of num1 and num2 is:", sum)
# practice question2
# WAP to input side of a square & print its area. 
# side =float( input("enter a side of square:"))
# area = side * side 
# print("area of square is:", area)
# practice question3
# WAP to input 2 floating point numbers & print their average.
# num1 = float(input("enter a number:"))
# num2 = float(input("enter a number:"))
# avg = (num1 + num2) / 2
# print(avg)
# practice question4
# WAP to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False.
# n1 =int( input("enter a number:"))
# n2 =int( input("enter a number:"))
# print(n1 >= n2)