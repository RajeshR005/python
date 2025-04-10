n=int(input("Enter the number"))
temp=n
count=0
while temp>0:

    temp=temp//10
    count=count+1
print(count)