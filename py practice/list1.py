# li=[5,3,[3,4,5],1,4]
# print(li[2])


# # Practice in list qn:1

# write a program to ask the user to enter the favourite movie of 3

# fav_movie=int(input("How many movies you are going to enter: "))
# li=[]
# for i in range(fav_movie):
#     movie_list=input(f"Enter your favourite movie No:{i+1}")
#     li.append(movie_list)
# print(li)


#write a program to check th list contain elements that are in palidrome:

# method :1

# li=[1,2,2,1,2,1]
# if li==li[::-1]:
#     print("The list is palindrome")
# else:
#     print("The list is not a palindrome")

#method: 2

# li=[1,2,1,2,1]
# li1=li.copy()
# li1.reverse()
# if li==li1:
#     print("It is a Palindrome")
# else:
#     print("It is not a palindrome")

#write a program to count no of students have the 'A' grade:

# li=('A','B','C','O','B','O','A','O','O')
# print(li.count('A')) #using COunt method

# count=0
# for i in li:
#     if i=='O':       #Using the for loop
#         count+=1
# print(count)
