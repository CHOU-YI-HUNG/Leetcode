nums=[0,0,1,1,1,2,2,3,3,4]

n=len(nums)
i=0
while i<n-1:                  
    while i<n-1 and nums[i]==nums[i+1]: #當他們兩相同的時候        
        n-=1
        del nums[i:i+1]
    i+=1    
print(nums)