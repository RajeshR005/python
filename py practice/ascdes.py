# li=input("Enter the string")
# print(sorted(li))
# print(sorted (li, reverse=True))

# n=int(input("Enter the number"))
# a=0
# b=1
# li=[]
# while n+1>0:
#     li.append(a)
#     a,b=b+a,a
#     n=n-1
# print(li)
    

# n=int(input("Enter the number"))
# is_prime=True
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
# if is_prime:
#     print(f"{n}is a prime number")
# else:
#     print(f"{n}is not a prime number")
    
# n=int(input("Enter the number"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)

# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# operations=input("add,sub,mul,div")
# if operations=="add":
#     print(a+b)
# elif operations=="sub":
#     print(a-b)
# elif operations=="mul":
#     print(a*b)
# elif operations=="div":
#     print(a/b)
# else:
#     print("invalid operations")/

# n=input("Enter the string")
# num=len(n)
# if num>3:
#     print(f"{n}is a valid name")
# else:
#     print(f"{n}is a invalid string")

# n=input("Enter the string")

# if n.islower():
#     print(f"{n}is in lowercase")
# elif n.isupper():
#     print(f"{n}is in Upper case")
# else:
#     print(f"{n}it contains mixed letters")

# n=int(input("Enter the number"))
# sum1=0
# for i in range(1,n):
#     if n%i==0:
#         sum1=sum1+i
# if sum1==n:
#     print(f"{n}perfect number")
# else:
#     print(f"{n}imperfect number")
    

# n=int(input("Enter the number"))
# sum1=0
# temp=n
# while temp>0:
#     dig=temp%10
#     sum1=sum1+dig**3
#     temp=temp//10
# if sum1==n:
#     print(f"{n}is a Armstrong number")
# else:
#     print(f"{n}is not a Armstrong number")

# n=int(input("Enter the number"))
# li=[]
# for i in range(1,n+1):
#     if n%i==0:
#         li.append(i)
# print(li)

# n=input("Enter the number or string")
# if n==n[::-1]:
#     print(f"{n} is palindrome")
# else:
#     print(f"{n} is not a palindrome")

# n=int(input("Enter the number to sum"))
# sum1=0
# while n>0:
#     dig=n%10
#     sum1=sum1+dig
#     n=n//10
# print(sum1)

# a=10
# b=5
# print(divmod(a,b))

# n=int(input("Enter the year"))
# if (n%400==0) or (n%4==0 and n%100!=0):
#     print(f"{n}is a leap year")
# else:
#     print(f"{n}is not a leap year")