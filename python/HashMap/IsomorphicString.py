


def isIsomorphic(s,t):
    histroy_s=dict()
    histroy_t=dict()
    for i in range(len(s)):                
        if s[i] not in histroy_s:
            histroy_s[s[i]]=t[i]
        else:
            if histroy_s[s[i]]!=t[i]:
                return False
        if t[i] not in histroy_t:
            histroy_t[t[i]]=s[i]
        else:
            if histroy_t[t[i]]!=s[i]:
                return False
    return True            
            
            
            
s="egg"
t= "add"           
print(isIsomorphic(s,t))
            
s="foo"
t= "bar"           
print(isIsomorphic(s,t))
            
s="paper"
t= "title"           
print(isIsomorphic(s,t))
            
            
            
            
            
            
            
            
            