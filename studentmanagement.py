# Task:
# 👉 Design a mini student management system using only JSON file operations.

# It should support:

# Add new student (ask name, age, loc)

# View all students

# Search student by name (partial match allowed)

# Update student name/location

# Delete student by name

# ⚡ Important:
# You must build a menu-driven program where user can select:

# markdown
# Copy
# Edit
# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit
# Each choice should call the correct function.

# ✅ Rules:

# Use only one JSON file (student.json).

# Handle if the file is empty.

# Always save after changes.
import json

student=list()

with open('studentmanagement.json','r') as f:
    data1=json.load(f)
    print("\nAdd Student=1 \nView student=2 \nSearch student=3 \nUpdate student=4 \nDelete student=5 \nExit=6")
p_operations=int(input("Enter what operation you are going to perform(in Num):  "))
if p_operations==1:
    name=input("Enter the name of the student: ")
    Age=int(input("Enter the Age of the student: "))
    location=input("Enter the location of the student: ")
    data1.extend([{'name':name,'Age':Age,'location':location}])
    print("Data Saved Sucessfully")
    
    
elif p_operations==2:
    count=0
    for i in data1:
        count+=1
        print(i)
    if count==0:
        print("There is no Student Record")
elif p_operations==3:
    student_name=input("Enter the student Name: ").lower()
    count=0
    for i in data1:
        if student_name in i["name"].lower():
            count+=1
            print(i)
    if count==0:
        print("No Data found with this Student Name")
elif p_operations==4:
    update_stu=input("Enter the student name: ").lower()
    count=0
    for i in data1:
        if update_stu==i["name"].lower():
            count+=1
            print("The fields you can update \n Name = 1 \n Age = 2 \n location = 3")
            field_name=int(input("Enter the field number you want to update: "))
            if field_name==1:
                stu_name=input("Enter the New student Name: ")
                i["name"]=stu_name
            elif field_name==2:
                stu_age=int(input("Enter the New Age: "))
                i["Age"]=stu_age
            elif field_name==3:
                stu_location=input("Enter the New location")
                i["location"]=stu_location
            else:
                print("Enter the valid field number")
    if count==0:
        print("No Data Found with this Student Name")
elif p_operations==5:
    del_stu=input("Enter the name of the student want to delete: ").lower()
    count=0
    for i in data1:
        if del_stu==i["name"].lower():
           count+=1
           data1.remove(i)
    if count==0:
        print("NO Data Found with this Student Name")
elif p_operations==6:
    exit
else:
    print("Enter the Valid Operation")
        
with open('studentmanagement.json','w') as f:
    json.dump(data1,f,indent=3)
    

    





    



