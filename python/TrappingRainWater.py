

def TrapWatter(height):
    Start=height[0]            
    i=0
    Tw=0
    Maxheight=0   
    MaxheightIndex=0 
    ringStartflag=0    
    down=0
    up=0
    
    # for j in range(0,):    
    j=1
    while j<len(height):
        if ringStartflag==0:
            # Init raising case
            if i==0 and height[j]-Start>=0:            
                Start=height[j]
                i=j
            else:
                ringStartflag=1
                down=1
                continue                
        else:            
            if height[j]-height[j-1]<0:
                down=1
            if height[j]-height[j-1]>0:
                up=1            
        
            if j>i and height[j]>=Maxheight:
                Maxheight=height[j]
                MaxheightIndex=j
            
            if up==1 and down==1:              
                if (j-i-1)>0 and height[j]>= Start:
                    Tw+=(j-i-1)*Start-sum(height[i+1:j])
                    Maxheight=0
                    Start=height[j]
                    i=j    
                    up=0
                    down=0            
                elif j==len(height)-1:
                    Tw+=(MaxheightIndex-i-1)*MaxheightIndex-sum(height[i+1:MaxheightIndex])                

        j+=1
                                    
    return Tw
            
    
height=[0,1,0,2,1,0,1,3,2,1,2,1]
# print((3-1-1)*1-sum(height[1+1:3]))
print(TrapWatter(height))    


    
