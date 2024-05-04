

def twoSum(nums:list,target):    
    indexed_list = list(enumerate(nums))
    sorted_list = sorted(indexed_list, key=lambda x: x[1])
    i=0
    j=len(nums)-1
    while i<j:
        Sum=sorted_list[i][1]+sorted_list[j][1]
        if Sum==target:
            return [sorted_list[i][0],sorted_list[j][0]]
        elif Sum<target:
            i+=1
        else:
            j-=1
    
    return -1



nums=[2,7,11,15]
target=9
print(twoSum(nums,target))


nums=[3,2,4]
target=6
print(twoSum(nums,target))

nums=[3,3]
target=6
print(twoSum(nums,target))

    
        
    
    