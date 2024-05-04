
def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    k=0
    for index in range(0,len(nums)):                        
        if nums[index] == val:                                
            nums[index]=-1
            k=k+1
    nums.sort() 
    del nums[0:k]
    print(k)
    print(nums)
       
