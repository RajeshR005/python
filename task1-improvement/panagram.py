str1="abcdefghijklmnopqrstuvwxyz"
str2=input("Enter the string").strip().lower()
for i in str2:
    if i in str1:
        print("panagram")
    else:
        print("not a Panagram")

