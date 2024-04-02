def isAnagram(s,t):

    if len(s)!=len(t):return False
    s_table={}
    t_table={}    
    for se, ts in zip(s,t):
        if se not in s_table:
            s_table[se]=1
        else:
            s_table[se]+=1     
        if ts not in t_table:
            t_table[ts]=1
        else:
            t_table[ts]+=1     
    
    for ta in t_table:
        if ta in s_table:
            if t_table[ta]!=s_table[ta]:
                return False
        else:
            return False    
    return True
    
    
    





s="anagram"
t="nagaram"
print(isAnagram(s,t))

s="rat"
t="car"
print(isAnagram(s,t))














