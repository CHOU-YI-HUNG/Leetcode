
def minSubArrayLen(target,nums:list):    
    ans=len(nums)+1
    left=0
    right=len(nums)
    while left<=right and right>0:                
        ws=(right+left)//2    
        if ws==0: ws=1       
        start=0
        end=ws        
        SumA=sum(nums[start:end])
        flag=True
        while end <len(nums)+1:                        
            if SumA>=target:                            
                flag=False                                        
                right=ws-1
                ans=min(ans,ws)
                
                break
            else: 
                SumA-=nums[start]                   
                if end<len(nums):            
                    SumA+=nums[end] 
                start+=1                              
                end+=1
                
        if flag==True:                               
            left=ws+1 
    if ans== len(nums)+1:
        return 0                   
    return ans
        
    
    
target=7
nums=[2,3,1,2,4,3]
print(minSubArrayLen(target,nums))


target=4
nums=[1,4,4]
print(minSubArrayLen(target,nums))
target=11
nums=[1,1,1,1,1,1,1,1,1]
print(minSubArrayLen(target,nums))

target=7
nums=[1,1,1,1,7]
print(minSubArrayLen(target,nums))
# target=213
# nums=[12,28,83,4,25,26,25,2,25,25,25,12]
# print(minSubArrayLen(target,nums))
# target=15
# nums=[1,2,3,4,5]
# print(minSubArrayLen(target,nums))

# target=396893380
# nums=[3571]
# print(minSubArrayLen(target,nums))


# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         ws=1
#         while ws<len(nums)+1:
#             start=0
#             end=ws 
#             while end <len(nums)+1:
#                 SumA=sum(nums[start:end])
#                 if SumA>=target:
#                     return ws
#                 else:
#                     start+=1
#                     end+=1
#             ws+=1                                
#         return 0