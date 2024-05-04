# method 1 fail
# def candy(ratings):
#     candys=0
#     n=len(ratings)
#     if n<1:        
#         return 1
#     if ratings[0]>ratings[1]:
#         preP=2
#         candys+=preP
#     else:    
#         preP=1
#         candys+=preP
    
#     for i in range(1,n-1):
#         if ratings[i]<ratings[i-1] or ratings[i]<ratings[i+1]:            
#             if preP-1>0:
#                 preP-=1      
#         elif ratings[i]==ratings[i-1] and ratings[i]==ratings[i+1]:
#             preP=1
#         else:            
#             preP+=1                        
#         candys+=preP    
    
#     if ratings[n-2]<ratings[n-1]:
#         preP+=1
#     elif ratings[n-2]==ratings[n-1]:
#         preP=1
#     else:            
#         if preP-1>0:
#             preP-=1
#     candys+=preP                
#     return candys    
def checkState(a,b):
    if a<b: #upward                      
        return 'up'                
    elif a>b: #downward
        return 'down'
        
    else: #flat     
        return 'flat'        
    
    

def candy(ratings):
    n=len(ratings)
    if n<1:
        return 1
    preup=0
    predown=0
    up=0
    down=0
    flat=0
    candys=0
    prestate=checkState(ratings[0],ratings[1])
    state=prestate
            
    for i in range(0,n-1):
        prestate=state
        if ratings[i]<ratings[i+1]: #upward                      
            state='up'
            if prestate=='down':
                
                
            elif prestate=='flat':
            
            else:                        
                preup+=1
                up+=preup            
        elif ratings[i]>ratings[i+1]: #downward
            state='down'
            if prestate=='up':
                tempup=up
                
                predown+=1
                down+=predown                
                if down>up:
                    candys+=down
                else:    
                    candys+=up
                
            elif prestate=='flat':
            
            else:
                predown+=1
                down+=predown
        else: #flat     
            state='flat'
                    
        if prestate=='up' and state=='down':
                       
            
    
ratings=[1,0,2] #5
print(candy(ratings))
ratings=[1,2,2] #4
print(candy(ratings))
ratings=[1,3,2,2,1] #7
print(candy(ratings))
ratings=[1,2,87,87,87,2,1] #13
print(candy(ratings))

