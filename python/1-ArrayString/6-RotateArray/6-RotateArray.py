def rotate(nums,k):    
    nums_len=len(nums)
    k=k%nums_len
    nums[:]=nums[nums_len-k:nums_len]+nums[0:nums_len-k]
    

nums=[-1,-100,3,99]
k=2
rotate(nums,k)
print(nums)


# nums=[1,2,3,4,5,6,7]
# k=3

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