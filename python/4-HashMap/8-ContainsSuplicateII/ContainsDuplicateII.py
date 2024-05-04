def containsNearbyDuplicate(nums,k):    
    history={}    
    for i in range(len(nums)):
        if nums[i] not in history:
            # 第一次出現
            history[nums[i]]=i
        else:
            # 發生Duplicate
            if i-history[nums[i]]<=k:
                return True
            # update history
            history[nums[i]]=i    
    return False
            
            
    
nums=[1,2,3,1]
k=3
print(containsNearbyDuplicate(nums,k))
nums=[1,0,1,1]
k=1
print(containsNearbyDuplicate(nums,k))
nums=[1,2,3,1,2,3]
k=2
print(containsNearbyDuplicate(nums,k))


