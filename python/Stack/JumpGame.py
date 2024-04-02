# nums=[3,2,1,0,4]
nums=[2,0,2,1,4]
# nums=[2,5,0,0]
# nums=[1,1,0,1]
#參考自己的解答:
ans = 0
end = 0
farthest = 0

# Implicit BFS
for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])
    if farthest >= len(nums) - 1:
        ans += 1
        break
    if i == end:      # Visited all the items on the current level
        ans += 1        # Increment the level
        end = farthest  # Make the queue size for the next level
print(ans)
























# def JumpGame(nums,index,DeadIndex,Route,Routes):
#     nums_len=len(nums)
        
#     if nums_len<=1:
#         value=Route[:]        
#         Routes.append(value)        
#         Route.pop()
#         DeadIndex.append(index)
#         return True
#     if nums_len>1 and nums[0]==0:
#         DeadIndex.append(index)
#         Route.pop()
#         return False
#     for inner in range(nums[0],0,-1):
            
#         if (index+inner) in DeadIndex:
#             if index not in DeadIndex:
#                 DeadIndex.append(index)                
#             pass
#         else:
#             Route.append(index+inner)
#             JumpGame(nums[inner:nums_len],index+inner,DeadIndex,Route,Routes)
            
#     Route.pop()
#     return 0

# # main
# index=0
# DeadIndex=[]
# Route=[0]
# Routes=[]
# JumpGame(nums,index,DeadIndex,Route,Routes)
# if len(Routes)>0:
#     print(True)
#     minouput=len(Routes[0][:])
#     for item in Routes:
#         if minouput>len(item):
#             minouput=len(item)
#     print(minouput)
# else:
#     print(False)
#     print(0)
















# 
# last_position = len(nums)-1
# for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
#     if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
#         last_position = i # Since we just need to reach to this new index
# # return last_position == 0	
# print(last_position == 0) 






# initial
# Curindex=0 
# DeadIndex=[]
# RouteIndex=[Curindex] 
# step=nums[Curindex]
# innerStep=0
# Start decide
# nums_len=len(nums)        
# if nums_len==1:
#     print(True) 
# while Curindex<nums_len-1:          
#     Nextindex=Curindex+step      
#     if step<=0:
#         if Curindex==0:
#             print(False)
#             break
#         DeadIndex.append(Curindex)
#         RouteIndex.pop()
#         Curindex=RouteIndex[-1]
#         innerStep=innerStep+1
#         if innerStep==nums[Curindex]:
#             if Curindex==0:
#                 print(False)
#                 break
#             DeadIndex.append(Curindex)
#             RouteIndex.pop()
#             Curindex=RouteIndex[-1]
#             innerStep=1

                                      
#     if Nextindex not in DeadIndex:
#         if Nextindex>nums_len-1:
#             break         
#         RouteIndex.append(Nextindex)
#         step=nums[Nextindex]
#         Curindex=Nextindex
#     else:                
#         step=nums[Curindex]-innerStep                               
# print(True)
