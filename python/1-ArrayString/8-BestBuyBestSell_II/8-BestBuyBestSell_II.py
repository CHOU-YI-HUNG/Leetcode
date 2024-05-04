

def maxProfit(prices):            
    i=0 #buy
    j=1 #sell    
    max_Profit=0
    while j<len(prices):
        profit=prices[j]-prices[i]        
        if profit<=0: #明天會跌不要買
            i=j
            j+=1
        else:  #這天買賺錢
            #有賺錢就賣出去
            max_Profit+=profit
            #找一天可以賣最多錢的
            i=j
            j+=1                        
    return max_Profit
        


prices=[7,1,5,3,6,4]
print(maxProfit(prices))
prices=[7,6,4,3,1]
print(maxProfit(prices))

prices=[1,4,2]
print(maxProfit(prices))
