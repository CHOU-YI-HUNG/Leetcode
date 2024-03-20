# nums=[1,2,3,4,5,6,7]
# k=3
nums=[-1,-100,3,99]
k=2
nums_len=len(nums)
k=k%nums_len
tempk=nums[nums_len-k:nums_len]
nums[:]=tempk+nums[0:nums_len-k]
print(nums)


# method2
# if k>0:
#     for index in range(1,k+1):
#         nums.insert(0,nums[-1*index])
#     del nums[-k:-1]  
#     if nums_len>1:  
#         nums.pop()
# print(nums)   
#method1
# nums=[1,2,3,4,5,6,7]
# k=3
# for index in range(1,k+1):
#     nums.insert(0,nums[-1])
#     del nums[-1]    
# print(nums)    