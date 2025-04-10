# # 1. Write a program that takes a list of integers and prints the sum, max, min, and average.

# li=[1,2,3,4,5]
# print(sum(li))
# print(max(li))
# print(min(li))
# len1=len(li)

# Average=sum(li)/len1
# print(Average)

#  Write a program that checks if a given number is a perfect number.
# n=int(input("Enter the number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")

# Write a Python program to check whether a given number is a prime number or not.
# n=int(input("Enter a number"))
# if n>1:
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

# Check whether the given string or number is palindrome or not

# n=input("Enter the number or string")
# if n==n[::-1]:
#     print("it is palindrome")
# else:
#     print("It is not a palindrome")


# Factorial of a number
# n=int(input("Enter the number"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)

# Fibonacci series5

# n=int(input("Enter the number: "))
# a=0
# b=1
# li=[]
# for i in range(1,n+1):
#     li.append(a)
#     a,b=b+a,a
# print(li)

#  Find the Armstrong Number
n=int(input("Enter the number"))
temp=n
sum1=0
while temp>0:
    dig=temp%10
    sum1=sum1+dig**3
    temp=temp//10
if sum1==n:
    print(f"{n}is a Armstrong number")
else:
    print(f"{n}is not a Armstrong number")



