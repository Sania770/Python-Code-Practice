# lists and tuples

# # list in python 
# std = [12, 13, 14]
# print(std) #[12, 13, 14]
# print(type(std)) #the type is list
# print(len(std)) #3  the lenght of the list
# std[1] = 2
# print(std) #[12, 2, 14]

# # list slicing
# std = [12, 13, 14, 23, 67, 50]
# print(std[1:4]) # As last index not include the list containes the values such as [13,14,23]
# print(std[:3]) #12,13.14
# print(std[4:]) #67,50
# #  negatve indxing also includes in slicing 
# print(std[-4:-1]) #14,23,67 last index is not includes
#list methods (methods are belongs to an object or class)
# list = [3,2,1,4]
# print(list)
# list.append(5) #adds at the end of the list suc as 3,2,1,4,5
# print(list)
# list.sort() #sort in acending order such as 1,2,3,4,5
# print(list)
# list.sort(reverse=True) #sort in decending order such as 5,4,3,2,1
# print(list)
# list = [4,5,6,7]
# list.reverse() #reverse all th list such as 7,6,5,4
# print(list)
# list = [3,2,1,4]
# list.insert(1,4) #after this insertion the list is : 3,4,2,1,4
# print(list)
# Feature	              pop()	                                      remove()
# Target Identification:  Uses the index (position) of the element.	   Uses the actual value of the element.
# Return Value:	          Returns the element that was deleted.	       Returns None
# list = [3,2,1,4,1]
# print(list) #3,2,1,4,1
# list.pop(3) #deletes on the 3rd index element
# print(list) #3,2,1,1
# list.remove(1) #removes the 1st occurance of 1 
# print(list) #3,2,1
# tup = (2,3,4)
# print(type(tup)) 
# tup1 = () #empty tuple
# print(tup1)
# print(type(tup1)) 
# tup2 = (1,) #singleton tuple
# print(tup2)
# tup3 = (1,2,3,3,3,3,3) #multi-element tuple 
# print(tup3)
# # tuple methods 

# print(tup3.index(2)) #returns the index of the element
# print(tup3.count(3)) #counts the number of the occurances in the tuple
# practice question number 1
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# f1 = input("enter your fav movie:")
# f2 = input("enter your fav movie:")
# f3 = input("enter your fav movie:")
# list = [f1,f2,f3]
# print(list)
# practice question number 2
# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# list = [1,2,2,1] #palindrom
# # list = [1,2,4,1] #not palindrom
# print(list)
# copy_list = list.copy()
# copy_list.reverse()
# if(copy_list == list):
#     print("the list is palindrom")
# else:
#     print("the list is not palindrom") 
# # practice question number 3 
# WAP to count the number of students with the “A” grade in the following tuple.
# tup = ("C", "B","A","A", "D", "D")
# cunt = tup.count("A")
# print(cunt)
# practice question number 4
# Store the values in a list & sort them from “A” to “D”
# list = ["C","B","A","A","D","D"]
# list.sort()
# print(list)