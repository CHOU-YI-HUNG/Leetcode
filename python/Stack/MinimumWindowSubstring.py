
def minWindow(s,t):
    dictionary=dict()
    for i in t:
        dictionary[i]=0
    dictionary["other"]=0        
    count=pow(10,6)
    
    ans=""          
    # need to reset these parameter  
    temp=""
    windowSize=0
    # CheckDictionaryIsFull=0
    # CheckDictionaryIsNoEmpty=False
    for i in range(len(s)):
        if s[i] in t:                                   
            dictionary[s[i]]+=1
            if len(temp)<1:
                start=i   
            if s[i] not in temp:
                temp+=s[i]                                                             
            if len(temp)==len(t):
                if count>sum(dictionary.values()):
                    count=sum(dictionary.values())
                    ans=s[start:i+1]
                # reset
                start=i-windowSize
                temp=s[i-windowSize:i+1]    
                dictionary=dict.fromkeys(dictionary,0)                            
                for j in range(len(temp)):
                    dictionary[temp[j]]+=1                        
            windowSize+=1
        else:            
            dictionary["other"]+=1
            windowSize=0
                
    return ans

s="ADOBECODEBANC"
t="ABC"
print(minWindow(s,t))

s="a"
t="a"
print(minWindow(s,t))

s="a"
t="aa"
print(minWindow(s,t))

s="bdab"
t="ab"
print(minWindow(s,t))

s="aa"
t="aa"
print(minWindow(s,t))