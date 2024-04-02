nums=[3,2,3]
n = len(nums)
count_map = {}

for num in nums:
    count_map[num] = count_map.get(num, 0) + 1
    if count_map[num] > n / 2:
        print(num)
       
# nums.sort()
# max_time=-1
# times=0
# nums_len=len(nums)
# i=0
# while i<nums_len:            
#     k=1
#     while i+k<nums_len and nums[i]==nums[i+k]:
#         k=k+1
#     if max_time<k:
#         max_time=k
#         max_number=nums[i]
#     i=i+k
# print(max_number)