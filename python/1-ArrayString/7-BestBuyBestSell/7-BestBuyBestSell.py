

def maxProfit(prices):            
    i=len(prices)-2 #buy
    max_price=prices[len(prices)-1]
    max_Profit=0
    while i>-1:
        profit=max_price-prices[i]
        max_price=max(max_price,prices[i])        
        max_Profit=max(max_Profit,profit)        
        i-=1
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


# def maxProfit(prices):        
#     i=0
#     j=1
#     max_profit=0
#     while j<len(prices):           
#         currentprofit=prices[j]-prices[i]
#         if currentprofit>0:
#             max_profit=max(currentprofit,max_profit)
#         else:
#             i=j
#         j+=1
#     return max_profit






# list=[1, 2, 3]


# print(max(list[0:2]))
# prices_len=len(prices)
# Max_price=max(prices)
# Min_price=min(prices)
# if prices.index(Max_price)>prices.index(Min_price):
#     print(Max_price-Min_price) 


##method 3
# prices=[2,4,1,7]
# prices_len=len(prices)
# Max_profit=-1
# Min_prices=prices[0]
# for index in range(0,prices_len):
#     # For accerate
#     if index>1 and prices[index]>Min_prices:        
#         continue        
#     if Min_prices>prices[index]:
#         Min_prices=prices[index]    
        
#     # For solve problem
#     profit=max(prices[index:prices_len])-prices[index]
#     if Max_profit<profit:
#         Max_profit=profit
# if Max_profit<0:
#     print(0)
# else:
#     print(Max_profit)   


## method2
# prices_len=len(prices)
# Max_profit=-1
# for i in range(0,prices_len):
#     for j in range(i+1,prices_len):
#         profit=prices[j]-prices[i]
#         if Max_profit<profit:
#             Max_profit=profit
# print(Max_profit)





# prices=[7,6,4,3,1]
# prices_len=len(prices)
# Max_profit=-1
# for index in range(0,prices_len-1):
#     profit=max(prices[index:prices_len])-prices[index]
#     if profit<0:
#         continue          
#     if Max_profit<profit:
#         Max_profit=profit
# if Max_profit<0:
#     print(0)
# else:
#     print(Max_profit)    


#method 1
# prices=[7,1,5,3,6,4]
# prices_len=len(prices)
# Max_profit=-1
# for index in range(0,prices_len-1):
#     profit=max(prices[index:prices_len])-prices[index]
#     if Max_profit<profit:
#         Max_profit=profit
# if Max_profit<0:
#     print(0)
# else:
#     print(Max_profit)    

