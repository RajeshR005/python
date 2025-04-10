n=int(input("Enter the number"))
temp=n
sum=0
while temp>0:
    dig=temp%10
    sum=sum+dig**3
    temp=temp//10
if sum==n:
    print("Armstrong")
else:
    print("Not a Armstrong")