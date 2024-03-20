# citations = [0,1]
# citations = [1,3,1]
citations = [3,6,0,1,5]
# citations = [4,4,0,0]
# citations = [1,7,9,4]

# # Sorted
# citations.sort(reverse=True)
# ans=0
# for index in range(0,len(citations)):
#     if citations[index]>=index+1:
#         ans+=1            
# print(ans)

# # UnSorted
ans=0
for index in range(0,len(citations)):
    if citations[index]>=ans+1:       
        ans+=1                
        if citations[index-1]<ans and citations[index-1]!=0:
            ans-=1                
print(ans)
# 參考別人的
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




