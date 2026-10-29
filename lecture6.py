# function and recursion 
# function block of statement perform a specific task 
# def sum(a,b): #function defination ==> here a & b passed as the argument in the function
#     sum = a+b
#     return sum
# print(sum(1,2))  # function call ==> here 1&2 passed as argument in the function calling 

# ##default function ==> no passed any argument to the function
# def sum():
#     print( 1 + 4) 
# sum()
# Let‘s Practice
# WAF to print the elements of a list in a single line. ( list is the parameter)
# def list_print(lst):
#     idx = 0
#     while(idx <= len(lst)-1):
#         print(lst[idx], end=" ")
#         idx = idx + 1
# list = [1,2,3,4,5]
# list_print(list)        

# # WAF to find the factorial of n. (n is the parameter)
# def fact(num):
#     f = 1
#     for el in range(f, num + 1):
#         f = f*el
#     print(f)  
# fact(2)      
# fact(3)  #6    
# fact(4)  #24  

# # WAF to print the length of a list. ( list is the parameter)
# def length(list):
#     print(len(list))
# lst = [1,1,2,2,3,4,5,5,6,77] 
# length(lst)   
# # WAF to convert USD to PKR.
# def convert(usd):
#     PKR = 200
#     total = usd * PKR
#     print(total)
# usd = int(input("enter the usd:"))
# convert(usd) 
# 
# ====================== Recursion ====================
# A function that calls itself is called recursion
# # prints the n to 1 backword 
# def prints(n):
#     if(n == 0): #base case when to exists from the function
#         return   
#     print(n, end=" ")
#     prints(n-1) #function calls itselfs
# prints(5)

# #returns n!
# def fact(n):

#     if( n == 0 or n == 1):
#         return 1
#     else:
#        return n * fact(n-1)
# print(fact(4))


# Let‘s Practice
# Write a recursive function to calculate the sum of first n natural numbers.
# def sum_fun(n):
#        if(n == 0):
#          return 0
#        else:
#         return n + sum_fun(n-1)
# s = sum_fun(4)
# print(s) 
 
       

# n = [1,2,3,4,5,66,7]
# sum = 0
# for el in n:
#     sum = sum + el
# print(sum)

# # Write a recursive function to print all elements in a list.
# # Hint : use list & index as parameters.
# list = [1,2,3,4,4,5]
# def prints(lst,idx):
#    if(idx == len(lst)):
#       return
#    else:
#       print(lst[idx], end = " ")
#       prints(lst, idx+1)
     
# prints(list,0)   


    
    
