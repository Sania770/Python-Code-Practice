# loops
# loops in the python 
# # 1st while loop ==> while condition : some work
# a = 0
# while (a <=5 ):
#     print("hello")
#     a = a+1
# # practice question 1    
# # Print numbers from 1 to 100  
# num = 1
# while (num <= 100):
#     print(num)
#     num += 1  
# # Print numbers from 100 to 1  
# num = 100
# while (num >= 1):
#     print(num)
#     num -= 1 
# # Print the multiplication table of a number n.
# num = 3
# n = 1
# while (n <= 10):
#     print(num,"*",n,"=",num*n)
#     n += 1
# # Print the elements of the following list using a loop:
# # [1, 4, 9, 16, 25, 36, 49, 64, 81,100]  
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
# indx = 0
# while (indx <= (len(list)-1)):
#     print(list[indx], end=" ")
#     indx += 1
# # Search for a number x in this tuple using loop:
# # [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# indx = 0
# search = 16
# while (indx <= (len(list)-1)):
#     if(search == list[indx]):
#         print("\nsearched at indx:[",indx,"]")
#         break
#     indx += 1
# # for loop in python 
# list = [1,2,3,4]
# for el in list:
#     print(el) 
# # for else in python 
# for el in list:
#     print(el)
# else:
#     print("all list is printed")
#practice question using using for loop  
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for el in list :
#     print(el)
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# indx = 0
# search = 1
# for el in list:
#     if(search == el):
#         print("number is founded in the list at the index:[",indx,"]" )
#         indx += 1
#         break
#     else:
#         print("not founded")       
#  # diff bw continue and break 
# # for i in range(1, 6):
# #     if i == 3:
# #         break
# #     print(i)

# # Output:
# # 1
# # 2

# # for i in range(1, 6):
# #     if i == 3:
# #         continue
# #     print(i)

# # Output:
# # 1
# # 2
# # 4
# # 5

# # Range function in the for loop range(start,stop, step) =>stop is not included
# for el in range(5):  # 0 to 4
#     print(el)
# for el in range(1,5):  # 1 to 4
#     print(el)
# for el in range(2,5,2):  # 2,4 (with the increasing step by 2)
#     print(el)

# # Let‘s Practice
# #using range functions
# # Print numbers from 1 to 100.
# for el in range(1,101):
#     print(el)
# # Print numbers from 100 to 1.
# for el in range(100,0,-1):
#     print(el)
# # Print the multiplication table of a number n
# num = 3
# for el in range(1,11):
#     print(num,"*",el,"=",num*el)
# Pass statement in the python 
# num = 3
# for el in range(1,11):
#     pass    
# while(num >= 0):
#     pass
# if(num >= 3):
# #    pass
# for el in range(1,11):
#     print(el)
# # Let‘s Practice    
# # WAP to find the sum of first n numbers. (using while)
# n = int(input("enter the number:"))
# # n = 5
# sum = 0
# i = 1
# while (i <= n):
#     sum = sum + i
#     i = i + 1
# print(sum)    
# # WAP to find the factorial of first n numbers. (using for)
# num = 3
# fact = 1
# i = 1
# for el in range(1,num+1):
#     fact = fact * i
#     i = i + 1
# print(fact)
