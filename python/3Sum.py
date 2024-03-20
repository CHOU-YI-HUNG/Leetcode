

def threeSum(nums:list):    
    nums.sort()
    ans=[]  
    i=0    
    j=len(nums)-1
    k=i
    while j-i>1 and k<j: # step 3        
        if k-i==1 and j-k==1:
            if nums[i]+nums[j]+nums[k]==0 and ([nums[i],nums[k],nums[j]] not in ans):
                ans.append([nums[i],nums[k],nums[j]])
                i+=1
                break
            # if nums[k]==0 and ([nums[i],nums[k],nums[j]] not in ans):
            #     ans.append([nums[i],nums[k],nums[j]]) 
            # if nums[k+1]>0:
            #     j-=1

            # else:
            #     i+=1    
            continue  # back to step 3                  
        elif abs(nums[i])>=abs(nums[j]):             
            k=j-1
            # flag=True
            while k>i: # step (i)                
                if abs(nums[i])>nums[k]+nums[j]:
                    i+=1
                    # flag=False
                    break # back to step 3
                else: # merge < and ==
                    if nums[i]+nums[j]+nums[k]==0 and ([nums[i],nums[k],nums[j]] not in ans):
                        ans.append([nums[i],nums[k],nums[j]])
                        i+=1
                        break
                    k-=1 
            # if flag:
            #     i+=1                                                                                   
        else: #abs(nums[i])<abs(nums[j])
            k=i+1
            # flag=True
            while k<j:
                if abs(nums[i]+nums[k])>nums[j]:
                    j-=1
                    flag=False
                    break
                else:
                    if nums[i]+nums[j]+nums[k]==0 and ([nums[i],nums[k],nums[j]] not in ans):
                        ans.append([nums[i],nums[k],nums[j]])                        
                        j-=1 
                        break                  
                    k+=1
            # if flag:
            #     j-=1                            
    return ans
                                        
    
    
nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))

nums=[0,1,1]
print(threeSum(nums))
nums=[0,0,0]
print(threeSum(nums))
nums=[0,0,0,0]
print(threeSum(nums))
# nums=[-2,0,1,1,2]
# print(threeSum(nums))
# nums=[3,0,-2,-1,1,2]
# print(threeSum(nums))
   
    # ans=[]    
    # i=0
    # if nums[i]>0:
    #     return ans   
    # while i<len(nums)-2:
    #     j=i+1   
    #     while j<len(nums)-1:            
    #         k=j+1           
    #         y=nums[j]+nums[k]
    #         if y>abs(nums[i]):
    #             break
    #         while k<len(nums):
    #             x=nums[i]+nums[j]
    #             if x>0 or abs(x)<nums[k]:
    #                 break
                
    #             if x+nums[k]==0:
    #                 ans.append([nums[i],nums[j],nums[k]])      
                
    #             k+=1    
    #         j+=1                        
    #     i+=1
    # return ans



