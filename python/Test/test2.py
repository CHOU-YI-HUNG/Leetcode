nums=[1,2,2,2]
nums_len=len(nums)
i=0
while i<nums_len:        
    k=1
    while (i+k)<nums_len and nums[i]==nums[i+k]:
        k=k+1            
    if k==1:        
        i=i+1
    elif k==2:
        i=i+2 
        pass
    else:
        del nums[i+1:i+k-1]
        nums_len=len(nums)
        i=i+2
        
           
print(nums)