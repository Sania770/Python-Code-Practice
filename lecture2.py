# String and conditional statements # what is string # string concatination
# str1 = "hello"
# str2 = "world"
# print(str2)
# con = str1 + " " + str2
# print("The concatinaton of the string is:", con)
# # The length of the string 
# print(len(con))
# # indexing in python 
# print(con[1]) #e
# print(con[2]) #l
# What is string slicing
# print(con[1:4]) #ell
# print(con[:7]) #hell w
# print(con[3:]) #lo world
# negative indexing is only available in slicing of the string and also negative indexing start from the right suc as -4,-3,-2 ,-1etc
# print(con[-5:-1]) #worl
# functions in the string 
# str1 = "hello my name is Sania. I'm a cyber developer."
# print(str1)
# #endswith retura true if exists.
# print(str1.endswith("developer")) #False
# print(str1.endswith("developer.")) #True
# print(str1.capitalize()) #Hello capital and all the remains are in the smallcase
# print(str1.replace("developer", "attacker")) #Hello
# print(str1.find("hello")) #return index 0 its because the first word of the hello is h->on 1st index means[0]
# print(str1.find("Sania")) #return index 17
# str1 = "hello my name is Sania. I'm a cyber developer. Sania Sania Sania"
# print(str1.count("Sania")) #4 times
# practice question1
# WAP to input user’s first name & print its length
# user = input("Enter user's first Name:")  
# print("the length of the user name is:",len(user))
# # practice question2
# # WAP to find the occurrence of ‘$’ in a String.
# str = input("Please enter something I can find the Occurances of the '$':")
# print("The occurance of the $ is:",str.count("$"))

# ====================Conditional Statements=============================
# if_elif_else syntax
# find the grade of the student based on their numbers
# num = int(input("enter the number of the student:"))
# if(num > 100):
#     num = int(input("Inperopriate marks! Please enter the marks between 0 to 100:"))
#     if(num >= 90 and num <= 100):
#      print("Your grade is A")
#     elif(num >= 80): 
#      print("Your grade is B")  
#     elif(num >= 70):
#      print("your grade is C")
#     elif(num >= 60):
#      print("your grade is D")
# else:
#     print("Your marks are less the 60 You are fail") 
# if_else statement in python 
# if(num > 50):
#   print("You are passed ") 
# else:
#   print("you failed")
#ternery operator
# age = 20
# s = "Adult" if age >= 18 else "Minor"
# print(s)  
# Practice Question1
# WAP to check if a number entered by the user is odd or even 
# num = int(input("enter a number:"))
# if((num%2) == 0):
#     print("you entered an even number")
# else:
#     print("you entered an odd number")
# WAP to find the greatest of 3 numbers entered by the user.
# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))
# num3 = int(input("Enter num3:"))
# if(num1 > num2 and num1 > num3):
#     print("num1 is greater then num2 and num3. The number is:",num1)
# elif(num2 > num1 and num2 > num3):
#     print("num2 is greater then num1 and num3. The number is:",num2)
# else:
#     print("num3 is greater then num1 and num2. The number is:",num3)
# Practice Question Number3
# WAP to check if a number is a multiple of 7 or not.
# num = int(input("Enter a Number:"))
# if((num%7) == 0):
#     print("The number is multiple of 7")
# else:
#     print("the number is not the multiple of 7")

""" 
MATCH STATEMENT
Instead of a long chain of if-elif-else statements, you pass an expression to match 
and define possible matches with case blocks. Unlike languages like C or c++, Python does not
require a break statement; only the first matching block executes.
"""
# Basic value matching 
# number = 2
# match number:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")
# multiple vales matching
# status = 201
# match status:
#     case 200 | 201 | 204:
#         print("HTTP Success")
#     case 400 | 401 | 404:
#         print("HTTP Client Error")
# the values of the
# num = int(input("enter the number we find what the number is > = < 50 or > = < 100 or other::"))
# match num:
#   case n if(n%2 == 0 and n >= 100):
#     case n if(n > 100):
#         print("number greater then hundred")
#     case n if(n == 100):
#         print("the number is hundred")
#     case n if(n > 50 and n < 100):
#         print("number is greater then 50 and less then 100")
#     case n if(n == 50 ):
#         print("the number is 50") 
#     case n if(n < 50 ):
#         print("the number is less then 50") 
#     case _ :
#         print("inparopriate number")          