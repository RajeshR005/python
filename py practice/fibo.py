num=int(input("Enter the number"))
a=0
b=1
li=[]

while num > b:
    a, b = b, a + b
    li.append(a)
print(li)


