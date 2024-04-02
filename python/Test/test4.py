

desserts = {'Muffin':(39,28), 'Scone':(39,28), 'Biscuit':(39,20)}
print(21 in desserts['Muffin'])
print(desserts['Muffin']==desserts['Biscuit'])
# if 'Muffin' in desserts:    
#     desserts['Muffin']=desserts['Muffin']+(8)
# else:    
#     desserts['Muffin']=(8)
# print(desserts)

# Add element into tuple
t1 = (2,)
t=t1+(8,)
print(t)


# citations = [3,6,0,1,5]
# citations_length = len(citations)
# papers = [0]*(citations_length+1)

# for citation in citations:
#     index = min(citations_length, citation)
#     papers[index] += 1

# k, s = citations_length, papers[citations_length]
# while k > s:
#     k -= 1
#     s += papers[k]
    
# print(k)    