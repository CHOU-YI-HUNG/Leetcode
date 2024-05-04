

def maxProfit(prices):            
    i=0 #buy
    j=1 #sell    
    max_Profit=0
    while j<len(prices):
        profit=prices[j]-prices[i]        
        if profit<0: #現在買不賺錢            
            i=j
            j+=1
        else:  #這天買賺錢
            #看賺多少錢，如果比之前都還要多，就換這天賣
            if profit>max_Profit: 
                max_Profit=profit
            #找一天可以賣最多錢的
            j+=1                        
    return max_Profit
        


prices=[7,1,5,3,6,4]
print(maxProfit(prices))
prices=[7,6,4,3,1]
print(maxProfit(prices))

prices=[1,4,2]
print(maxProfit(prices))

prices=[3,2,6,5,0,3]
print(maxProfit(prices))

prices=[1]
print(maxProfit(prices))
