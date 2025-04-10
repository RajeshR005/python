n=int(input("Enter the number"))
sum1=0
for i in range(1,n):

    if n % i == 0:
        sum1 = sum1 + i
if sum1==n:
    print("It is a perfect Number")
else:
    print("Not a perfect Number")

