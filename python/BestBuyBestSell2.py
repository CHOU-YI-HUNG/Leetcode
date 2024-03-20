# prices=[7,1,5,3,6,4]
prices=[7,6,4,3,1]
left=0
right=1
prices_len=len(prices)
MaxProfit=0
while right<prices_len:    
    profit=prices[right]-prices[left]
    if profit>0:
        MaxProfit=MaxProfit+profit
        left=right 
    else:   
        left=right
        
    right=right+1    
         
print(MaxProfit)
# return MaxProfit