

def happy(n):
    ans=0
    while n>0:        
        ans+= pow((n%10),2) 
        n=(n//10)
    return ans

def isHappy(n):
    slow=n
    fast=n    
    while True:
        slow=happy(slow)
        fast=happy(happy(fast))        
        if slow==1: return True
        if slow==fast: return False
        

    
    



n=19
print(isHappy(n))

n=2
print(isHappy(n))
