

def maxArea(height):
    left=0
    right=len(height)-1
    maxWater=-1
    while left<right:        
        if height[left]<height[right]:
            water=(right-left)*height[left]
            if water>maxWater:
                maxWater=water            
            left+=1
        else:
            water=(right-left)*height[right]
            if water>maxWater:
                maxWater=water
            right-=1
    
    return maxWater


height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))

height=[1,1]
print(maxArea(height))
height=[1,2,1]
print(maxArea(height))

height=[0,2]
print(maxArea(height))

height=[1,2,4,3]
print(maxArea(height))



    # n=len(height)    
    # #find max left  
    # maxWater=0   
    # maxLeft_h=0  
    # maxLeft_p=-1     
    # for i in range(0,n):        
    #     if (n-i-1)*height[i]>=maxWater:
    #         maxWater=(n-i)*height[i]
    #         maxLeft_h=height[i]
    #         maxLeft_p=i
    # #find max Right 
    # maxWater=0
    # maxRight_h=0  
    # maxRight_p=-1                  
    # for i in range(n-1,0,-1):
    #     if i*height[i]>maxWater:
    #         maxWater=i*height[i]
    #         maxRight_h=height[i]
    #         maxRight_p=i
    # if maxRight_h==-1 or maxLeft_p==-1:
    #     return 0

    # water=(maxRight_p-maxLeft_p)*min(maxRight_h,maxLeft_h)
