gas=[1,2,4,3,5,1,100]
cost=[3,4,1,5,2,10,0]
# gas=[2,3,4]
# cost=[3,4,3]
# Reference method
trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
for i in range(n):
    trip_tank += gas[i] - cost[i]
    curr_tank += gas[i] - cost[i]
    if curr_tank < 0:
        start = i + 1
        curr_tank = 0 
print(start if trip_tank >= 0 else -1) 
# return start if trip_tank >= 0 else -1


# # mehtod 3     Time limite
# n=len(gas)
# h={}
# for i in range(0,n):
#     if gas[i]-cost[i]>=0:
#         start=i
#         step=i
#         a=gas[start]
#         if step in h:
#             if a in h[step]:
#                 continue
#             else:
#                 h[step]=h[step]+(a,)
#         else:       
#             h[step]=(a,)         
        
#         while True:
#             if a-cost[step]>=0:
#                 a=a-cost[step]
#                 step=(step+1)%n
#                 if step in h:
#                     if a in h[step]:
#                         break
#                     else:
#                         h[step]=h[step]+(a,)
#                 else:       
#                     h[step]=(a,)                         
#                 a=a+gas[step]
#                 if step==start:
#                     print(step) 
#                     break
#                     # return start            
#             else:            
#                 break
# print(-1)


# mehtod 2 Time limite
# n=len(gas)
# for i in range(0,n):
#     if gas[i]-cost[i]>=0:
#         start=i
#         step=i
#         a=gas[start]
#         while True:
#             if a-cost[step]>=0:
#                 a=a-cost[step]
#                 step=(step+1)%n
#                 a=a+gas[step%n]
#                 if step==start:
#                     print(step) 
#                     break
#                     # return start            
#             else:            
#                 break
# print(-1)

# method1 Time limite
# sp=[]
# n=len(gas)
# for i in range(0,n):
#     if gas[i]-cost[i]>=0:
#         sp.append(i)
# for start in sp:
#     a=gas[start]
#     i=start
#     while True:
#         if a-cost[i]>=0:
#             a=a-cost[i]
#             i=(i+1)%n
#             a=a+gas[i%n]
#             if i==start:
#                 print(start) 
#                 break
#                 # return start            
#         else:            
#             break
# print(-1)