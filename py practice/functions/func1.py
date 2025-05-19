# def msg():
#     return "Hello world"
# print(msg())

# Write a program to print the len of the list in parameter:

# def li():
#     li=[1,2,3,4,5,6,7]
#     print(len(li))
# li()5
# n=int(input("Enter the number"))
# def factorial():
#     global n
#     fact=1
#     while n>0:
#         fact=n*fact
#         n-=1
#     return fact


# op=factorial()
# print(op)

 #Write a function to calculate the 1 usd to inr
# n=int(input("Enter the value in USD"))
# inr=85.38
# def usdtoinr():
#     global n
#     value=n*inr
#     return value
# op=usdtoinr()
# print(op)

#write a program to check the given num is even or odd:

# def oddeven(number):
#     if n%2==0:
#         return "Even"
#     else:
#         return "ODD"
# n=int(input("Enter the number to check"))
# op=oddeven(n)
# print(op)

#write a recursive function to write the n natural numbers
# n=int(input("Enter the number"))
# def nat(n):
#     if n==0:
#         return 0
#     return nat(n-1)+n
    
# print(nat(n))
# n=int(input("Enter the number"))
# def nat(n):
#     if n==0:
#         return
    
#     nat(n-1)
#     print(n)
    
# nat(n)

# write a factorial in recursive function
# n=int(input("Enter the number"))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return fact(n-1)*n
# print(fact(n))

#write a recursive function to print all the elements in the list
# li = [1, 3, 5, 7, 9]

# def list1(li, index=0):
#     if index == len(li):
#         return
#     print(li[index])
#     list1(li, index + 1)

# list1(li)
