
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """ 
    nums.sort()
    nums_len=len(nums)
    max_time=-1        
    i=0
    while i<nums_len:            
        k=1
        while i+k<nums_len and nums[i]==nums[i+k]:
            k=k+1                
        if max_time<k:
            max_time=k
            max_number=nums[i]
        if max_time>nums_len/2 or max_time>(nums_len-i):
            break    
        i=i+k
    return max_number
    







            