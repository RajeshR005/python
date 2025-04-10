n=int(input("Enter the number"))
for i in range(1,n+1):
    for k in range(1,i):

        print(" ",end="")
    for j in range(n,i,-1):
        print("*",end=" ")
    print()