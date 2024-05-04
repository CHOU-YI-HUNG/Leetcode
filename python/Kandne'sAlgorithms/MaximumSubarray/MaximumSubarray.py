
def maxSubArray(nums):
    Summation=max_value=nums[0]    
    for i in range(1,len(nums)):
        Summation=max(nums[i],Summation+nums[i])
        max_value=max(max_value,Summation)
    return max_value

        
    
    
    


nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))    







