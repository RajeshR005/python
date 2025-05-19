# 🛠️ Your Task:

# Write a recursive function to find the sum of digits of a given number.

# Example:

# Input: 1234

# ➔ 1 + 2 + 3 + 4 = 10

n=int(input("Enter the number"))
def sumof(n):
    
    
    if n==0:
        return 0
    
    
    dig=n%10
       
    n=n//10
        
        
    return (dig)+sumof(n)
    
                                            
print(sumof(n))
        
