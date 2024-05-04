nums=[1,1,1,1,1,2,2,2,2,3,3,]
nums_len=len(nums)
i=0
DelCount=0
while i<nums_len:        
    k=1
    while (i+k)<nums_len and nums[i]==nums[i+k]:
        k=k+1        
    kk=1
    while (i+kk)<nums_len and nums[i+k]==nums[i+k+kk]:
        kk=kk+1
    
    if k==1:
        i=i+1                
    elif k==2:
        i=i+2        
    else :                
        DelCount+=k-2        
        i=i+k                
del nums[nums_len-1-DelCount:nums_len-1]        
print(nums)