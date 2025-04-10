str1=input("Enter the number")
str2=str1.split()
freq={}
for i in str2:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)
