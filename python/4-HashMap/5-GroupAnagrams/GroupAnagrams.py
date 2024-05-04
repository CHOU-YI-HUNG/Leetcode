def hash(string):
    ans=1
    for char in string:
        ans*=ord(char)
    for char in string:
        ans+=ord(char)
    return ans

def groupAnagrams(strs:list[list]):
    ans=[]
    start=0
    mapping={}
    for string in strs:        
        number=hash(string)
        if number not in mapping:                        
            mapping[number]=start            
            ans.append([])
            start+=1                            
        ans[mapping[number]].append(string)
    return ans
        
        
                
        
        
        

strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
strs=[""]
print(groupAnagrams(strs))
strs=["a"]
print(groupAnagrams(strs))




