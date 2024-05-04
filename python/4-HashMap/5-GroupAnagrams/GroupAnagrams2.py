def hash(string):
    ans=sorted(string)
    ans = ''.join(ans)
    return ans
6
def groupAnagrams(strs:list[list]):
    ans=[]
    start=0
    mapping={}
    for string in strs:        
        token=hash(string)
        if token not in mapping:                        
            mapping[token]=start            
            ans.append([])
            start+=1                            
        ans[mapping[token]].append(string)
    return ans
        
        
                
        
        
        

strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
strs=[""]
print(groupAnagrams(strs))
strs=["a"]
print(groupAnagrams(strs))



