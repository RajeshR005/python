#method 1
li=[5,8,10]
print(max(li))
#method 2
li = [5, 8, 10]
largest = li[0]

for num in li:
    if num > largest:
        largest = num

print(largest)
