# f= open("D:\Git-Repo\python\py practice\(input-output)file\sample.txt","w+")
# write1=f.write(" At Maestreo Technologies")
# read=f.read()


# print(read)
# f.close()

# #write on a file :
# # f= open("D:\Git-Repo\python\py practice\(input-output)file\sample.txt","a")
# # write1=f.write("\n With Around 5+ Years of Experience")
# # f.close()


#Create a file  practice.txt using python and add the following data
# Hi everyone
# we are learning File I/0
# using Java.
# I like programming in Java.

# with open ("Sample1.txt","a+") as f:
#     f.write("Hi everyone")
#     f.write("\nwe are learning file I/O")
#     f.write("\nUsing Java")
#     f.write("\nI like Programming in Java")
#     f.seek(0)
#     hello=f.read()
#     print(hello)


#Replace the java with python

# with open ("Sample1.txt","r") as f:
#     hello=f.read()
# updated=hello.replace("Java","Python")
# print(updated)


 #Check if the word learning is in the file or not
# with open ("Sample1.txt","r") as f:
#     data=f.read()
#     if "learning" in data:
#         print("Found")
#     else:
#         print("Not found")

# with open("sample1.txt","r") as f:
#     data=f.read()
#     count=0
#     li=list(data.split(","))
#     for i in li:
#         if int(i)%2==0:
#             count+=1
#     print(count) 

# WAF to find in which line of the file does the word "learning"occur first.
# Print -1 if word not found.

# with open("sample1.txt", "r") as f:
#     count_line=1
#     word="xlearning"
#     hello=True
#     for i in f:
#         if word in i:
#             print(count_line)
#             hello=False
       
#         count_line+=1
#     if hello:
#              print("The given word is not in the file")

# with open("num.txt","w") as f:
#     n=int(input("no of numbers"))
#     li=[]
#     for i in range(n):
#         number=(input("Enter the number"))
#         f.write(number+',')
#         if int(number)%2==0:
#             li.append(number)
#     print(li)

# Task 1: Write Even Numbers to a File
# Objective:

# Ask the user how many numbers they want to input.

# Write only the even numbers to a file called even.txt, separated by commas.

# with open("even.txt","w+") as f:
#     n=int(input("How many number you want to print"))
#     for i in range(n):
#         number=(input("Enter the number:"))
#         if int(number)%2==0:
#             f.write(number+',')
#     f.seek(0)
#     print(f.read())

#  Task 2: Count Words in a File
# Objective:

# Create a file message.txt (either manually or using your code).

# Write a few sentences into it.

# Then, write a Python program to read the file and count how many words are in the file.


# with open("Message.txt","w+") as f:
#     f.write("Hello this is the new file \n It can hold multiple words")
#     # f.write("Hello this is the new file")
#     # f.write("\nIt can hold multiple words at one time")
#     # f.write("\nAnd we are going to count the words in this file")
#     # f.write("\nusing python program")
#     f.seek(0)
#     count=0
#     for i in f:
#         for word in i.split():
#             count+=1
#     print(count)
        


# Task 3: Line Number Where a Word Appears
# Objective:

# Ask the user for a word to search (case-insensitive).

# Read a file story.txt.

# Print all the line numbers where that word appears.

# with open("message.txt","r") as f:
#     with open("newfile.txt","w") as j:
#         write1=j.write(f.read())
#     # word="thinking"
    # count_line=1
    # for i in f:
    #     if word in i.lower():
    #         print(f"The given word is in the line:{count_line}")
    #     count_line+=1

# Task 4: Store Student Names and Marks
# Objective:

# Ask the user how many students.

# For each student, input their name and mark (e.g., Rajesh 89).

# Write this data into a file students.txt, with each student on a new line.

# Then, read the file and print the name of students who scored above 80.







    
       
    
    
    
        
        
    




 


