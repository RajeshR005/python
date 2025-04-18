#practice questions 

#Store the following word and meanings in the dictionary:
#  table: "A piece of furniture", "List of facts & figures"
#  cat: "a pet and beautiful soul"

# mydict={"table":["A Piece of furniture", "List of facts & figures"], "Cat":"A pet and beautiful soul"}
# print(mydict)

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
str1=int(input("Enter how many subjects"))
dict1={}
for i in range(str1):
    subjects=input("Enter the subjects along with the marks")
    subject_name,marks=subjects.split()
    dict1[subject_name]=marks
    


    
