student = {
    "name": "Rajesh",
    "course": {
        "name": "Python",
        "topics": ["Basics", "OOP", {"advanced": ["FastAPI", "Decorators"]}]
    },
    "location": {
        "city": "Coimbatore",
        "pincode": 641035
    }
}
#  What You Need to Do:
# Print the student's name

# Print the course name

# Loop through the topics list

# If it's a simple topic like "Basics" or "OOP" → print as basic topic

# If it's a dictionary → print the advanced topics separately

# Print the pincode of the student

# print(student["name"])
# print(student["course"])
# for i in student["course"]["topics"]:
#     if isinstance(i,dict):
#         print(f"This is advanced topic {i['advanced']}")
#     else:
#         print(f"This is a basic topic {i}")
# print(student["location"]["pincode"])

students = {
    "batch": "MCA 2025",
    "students": [
        {
            "name": "abc",
            "location": {"city": "Coimbatore", "pincode": 641035},
            "skills": ["Python", "Git", {"advanced": ["FastAPI", "Pandas"]}],
            "projects": [
                {
                    "title": "Healthcare Assistant",
                    "tech_stack": ["Python", "NLP", {"extras": ["Speech Recognition", "TTS"]}],
                    "role": "Lead Developer",
                    "contributions": {
                        "backend": True,
                        "frontend": False,
                        "api_integration": True
                    }
                }
            ]
        },
        {
            "name": "xyz",
            "location": {"city": "Chennai", "pincode": 600028},
            "skills": ["HTML", "CSS", {"advanced": ["JavaScript", "ReactJS"]}],
            "projects": [
                {
                    "title": "E-Commerce Website",
                    "tech_stack": ["JavaScript", "MongoDB", {"extras": ["JWT Auth", "Stripe Payment"]}],
                    "role": "Frontend Dev",
                    "contributions": {
                        "backend": False,
                        "frontend": True,
                        "api_integration": True
                    }
                }
            ]
        }
    ]
}

# Write code to:

# Print the batch name.

# For each student:

# Print name and pincode

# Loop through skills:

# If basic, print it

# If advanced, print separately

# Loop through projects:

# Print title and role

# Print basic tech stack

# If any extras, print those too

# Print what contributions they made (True fields only)
u=int(input("Enter the id"))
print("Batch: ",students["batch"])
print("Name:  ",students["students"][u-1]["name"])
print("Pincode: ",students["students"][u-1]["location"]["pincode"])
for i in students["students"][u-1]["skills"]:
    if isinstance(i,dict):
        print("Advanced skills:",i["advanced"])
    else:
        print("The Basic skills: ",i)
for i in students["students"][u-1]["projects"]:
    print("Title:",i["title"])
    print("Role: ",i["role"])
    for j in i["tech_stack"]:
        if isinstance(j,dict):
           print("Extras skills are: ",j["extras"])
        else:
           print("The Basic skill are: ",j)
    for key ,value in i["contributions"].items():
        if value is True:
            print("Their Contributions is in: ",key)


        

    