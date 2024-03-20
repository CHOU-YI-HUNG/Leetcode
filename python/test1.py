
nums=[0,0,1,1,1,2,2,3,3,4]
#nums=[0]
nums_len=len(nums)
duplicate_nums=0
i=0
ii=0
while i<nums_len-1:        
    k=1
    while (i+k)<nums_len-1 and nums[i]==nums[i+k]: #當他們兩相同的時候
        k=k+1
    nums[ii+1]=nums[i+k] #當他們兩不相同的時候
    i=i+k
    ii=ii+1
    duplicate_nums=duplicate_nums+k-1
del nums[nums_len-1-duplicate_nums:nums_len-1]

if nums_len>1 and nums[nums_len-2]==nums[nums_len-1]:
    del nums[nums_len-1]
print(nums)