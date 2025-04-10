n=int(input("Enter the number"))
temp=n
sum=0
while temp>0:
    dig=temp%10
    sum=sum+dig
    temp=temp//10
print(sum)
