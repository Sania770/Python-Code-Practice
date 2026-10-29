# # Dictionary and set
# # dictinaries are the key:value pairs -> it can be mutable, ->unorderd
# std = {
#     "name" : "Sania",
#     "class": "VOIP lab",
#     "cgpa" : 3.90,
#     "age"  : 19,
# }

# print(std)
# print(type(std))

# print(std["name"]) #Sania
# std["name"] = "Sadia" #mutable
# print(std)
# print(std["name"]) #Sadia

# marks = {
#     "chem" : 59,
#     "phy"  : 58,
#     "maths": 60,
# }
# print(marks)

# # nested  dictionaries 
# std = {
#     "name" : "Sara",
#     "class": "VOIP Lab",
#     "age"  : 19,
#     "marks" : {
#         "phy" : 49,
#         "che" : 50,
#         "fav_colors" : {
#             "color1" : "red",
#             "color2" : "green"
#         }
#     }
# }
# # Acces values of nested dictionaries
# marks = std["marks"] # phy: 59 , che:50, fav_colos :{'color1': 'red', 'color2': 'green'}
# print(marks)
# color = std["marks"]["fav_colors"]["color1"] # red
# print(color)

#  #dictinaries methods
# std = {
#     "name" : "Sania",
#     "class": "VOIP lab",
#     "cgpa" : 3.90,
#     "age"  : 19,
# }
#  #std.keys() :returns the all keys in the dictionaries
# print(std.keys()) #name, class, agpa, age
#  #std.values() :returns all the values in the dictionary
# print(std.values()) #sania, VOIP lab, 3.90, 19
#  #std.items() :returns the dict_items same as simple print(std) return the dict
# print(std)
# print(type(std))
# # print(std.items())
# print(type(std.items()))
# #  #std.get("key")  returns the specific value of the key
# print(std.get("name")) #Sania
# # #std.update()
# std.update(
#    {
#         "name" : "saba"

#    }
# )
# print(std.get("name")) #$saba


# =============== Sets in the python ===================
# set1 = {1,2,1,1,1}  ## ! is appars only once, no duplicated itmes are in sets
# print(set1) #{1,2}
# print(type(set1))
# set1.add(3)
# print(set1)
# set1.remove(1)
# print(set1)
# set1.clear()
# print(set1)
# set1.add(3)
# print(set1)
# #empty set
# # #how to create an empty set 
# empty_set = set() #syntax ep = set()
# print(empty_set)
# print(type(empty_set))

# num = {1,2,3,4}
# num.pop()
# print(num)
# num.pop()
# print(num)
# num.pop()
# print(num)

# # methods
# set1 = {1,2,3}
# set2 = {3,4,5}

# print(set1.union(set2)) # 1,2,3,4,5
# print(set1.intersection(set2)) #3

# practice question number 1
# Store following word meanings in a python dictionary :
# table : “a piece of furniture”, “list of facts & figures” 
# cat : “a small animal”
# dict = {
#     "table" : ["a piece of furniture", "List of facts and figure"],
#      "cat"  : "A small animal"
# }
# # #another way of writting instead of combinig
# table = {
#     "table1" : "A small piece of furniture",
#     "table2" : "List of facts and figure"
# }
# cat = {
#     "cat" : "A small animal"
# }
# print(dict)
# print(table)
# print(cat)

# """
#practice quesyion number 2
# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
# """
# set = {"python","java","c++","js","java","python","java","c++","c"}
# print(len(set))
# """
#practice quesyion number 3
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
# """
# dict = {}
# sub1 = int(input("enter the marks of first subject:"))
# sub2 = int(input("enter the marks of second subject:"))
# sub3 = int(input("enter the marks of third subject:"))
# # dict.add(sub1) this is the mistake
# dict.update({
#     "sub1":sub1,
# })
# dict.update({
#     "sub2":sub2,
# })
# dict.update({
#     "sub3":sub3,
# })
# print(dict)
# """
# # practice quesyion number 3
# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
# """
# set = {
#     ("int",9),
#     ("float",9.0), ## in set we use tuples 
# }
# print(set)