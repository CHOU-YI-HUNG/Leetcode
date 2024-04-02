

def twoSum(numbers,target):            
    i=0
    while i <len(numbers): 
        j=i+1
        while j<len(numbers):                     
            if numbers[i]==numbers[j]:
                jump=j
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]            
            j+=1                    
        i+=1
        if jump>i:
            i=jump
    
    
    
    


numbers=[2,7,11,15]
target=9

print(twoSum(numbers,target))
numbers=[2,3,4]
target=6

print(twoSum(numbers,target))
    
    
numbers=[-1,0]
target=-1

print(twoSum(numbers,target))
    


