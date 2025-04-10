n=int(input("Enter the numbers"))
temp=n
num=0
while temp>0:
    sum=temp%10
    num=num*10+sum
    temp=temp//10
if num==n:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
