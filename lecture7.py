# file I/O 
# f = open("python.txt", "w")
# data = f.read() #read all the lines
# print(data)
# data = f.readline() #read line by line for one line reading
# print(data)
# data = f.readlines()  # list of the lines
# print(data)
# data = f.readable() #returns true if file is readable
# print(data)
# data = f.write("Im a student at BZU University")
# print(data)
# f.close()

# f = open("write.txt", "a+")
# # data = f.write("hello in the writtng and reading mode")
# data = f.write("next line")
# print(data)
# data = f.read()
# print(data)
# f.close()

# f = open("overWrite.txt", "w+")
# # data = f.write("hello in the writtng and reading mode")
# data = f.write("next line")
# print(data)
# data = f.read()
# print(data)
# f.close()

# with open("write.txt","r") as f:
#     data = f.read()
#     print(data)
# import os 
# os.remove("overWrite.txt") 

# # Let‘s Practice
# #question number 1
# # Create a new file “practice.txt” using python. Add the following data in it:
# # Hi everyone
# # we are learning File I/O
# # using Java.
# # I like programming in Java.

# with open("new.txt","w") as f:
#     str = f.write("Hi everyone \nwe are learnig File I/O \nusing java.\nI like programming in java.")
# f.close()
  
# #question number 2
# # WAF that replace all occurrences of “java” with “python” in above file.

# with open("new.txt","r") as f:
#     data = f.read()
#     print(data)
#     new_data = data.replace("java", "python")
#     print(new_data)
# with open("write.txt","w") as f:    
#     f.write(new_data)   


# #question number 3
# # Search if the word “learning” exists in the file or not.
# with open("new.txt","r") as f:
#     str = f.read()   
#     str_len = str.find("learning")
#     if(str_len):
#         print(len(str_len))
#     else:
#         print(-1) 

# # From a file containing numbers separated by comma, print the count of even numbers.
# count = 0
# with open("write.txt","r") as f:
#     data = f.read()
#     print(data)
#     num = data.split(",")
#     for el in num:
#         if(int(el) % 2 == 0):
#             count = count + 1
# print(count)            
    
        






