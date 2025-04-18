import json
# student={
#     'name':'Prince',
#     'age':22,
#     'loc':'kvp'

# }


# with open("student.json",'w') as f:
#     json.dump(student,f)

# with open("student.json",'r') as j:
#     data=json.load(j)
#     # print(data)
# student=[
#     {'name':'prince','age':23,'loc':'kvp'},
#     {'name':'Rajesh','age':25,'loc':'Swiss'}
# ]

# with open("student.json",'w') as f:
#     data=json.dump(student,f)
# with open("student.json",'r') as k:
#     hello=json.load(k)
#     print(hello[0]["name"])
#     print(hello[1]["name"])
# # Append a new student to the list without replacing the existing data in the JSON file.

# # Print the updated student list!

# ✅ Important:

# You always load first (r mode).

# Then append in Python (data.append()).

# Then save full updated list back (w mode).

# ✨✨
# Simple words: JSON is like a notebook 📒 —
# if you want to add a line,
# you have to read the notebook, add the new line inside, and save the whole notebook again.
# You can't just throw random papers into it.



# with open('student.json','r') as f:
#     data=json.load(f)
# data.extend([{'name':'Mai','loc':'firenation'},{'name':'Katara','loc':'water nation'}])


# with open('student.json','w') as j:
#     json.dump(data,j,indent=4)

# Task:
# ✅ Read your student.json.
# ✅ Ask the user to input a location (e.g., "firenation" or "water nation").
# ✅ Then print all the student names whose loc matches the input (case-insensitive)

# with open ("student.json") as f:
#     data1=json.load(f)
#     n=input("Enter the starting letter").lower()
#     count=0
#     for i in data1:
#         if n in i["name"]:
#             if count==0:
#                 print("Student found")
#             print(i["name"])
#             count+=1
#     if count==0:
#         print("Student not found")

# Task: Update Student Information in JSON

# You have a JSON file with student details, including name, age, and location.

# Your task is to create a program where the user can update the student information (e.g., update the name, age, or location of a student) by specifying the student’s name.

# After the update, save the new information back into the JSON file.

# Steps:

# Load the JSON data from the file.

# Ask the user to input the student's name whose details they want to update.

# Allow the user to choose which detail they want to update (name, age, or location).

# Update the chosen detail with the new value.

# Save the updated data back to the JSON file.

# with open('student.json') as f:
#     data1=json.load(f)
#     n=input("Enter the student name: ")
#     for i in data1:
#         if n==i["name"]:
#             new_name=input("Enter the new name")
#             i["name"]=new_name
# with open('student.json','w') as f:
#     json.dump(data1,f,indent=2)
#     print(data1)

# Task: Remove a student from the JSON file.
# Objective: Write a program that allows a user to remove a student from the student.
# json file by their name. If the student exists, remove them and update the JSON file.
# If the student is not found, display a message indicating that the student could not be found.

with open('student.json') as f:
    data1=json.load(f)
    n=input("Enter the user name").lower()
    flag=False
    for i in data1:
        if n==i["name"].lower():
            data1.remove(i)
            flag=True
    if not flag:
        print("Student not found")
    else:
        with open('student.json','w') as f:
            json.dump(data1,f,indent=3)
            print(data1)


    

   