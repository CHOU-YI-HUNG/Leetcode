# s=chr(ord('a')+1)
# print(s)


def lengthOfLongestSubstring(s):
    n=len(s)    
    if n ==0: return 0
    if n ==1: return 1    
    length=0
    temp=""    
    for i in range(n+1):
        if i<n and s[i] not in temp:
            temp+=s[i]            
        else:
            length=max(len(temp),length)   
            if i<n:                
                temp=temp[temp.index(s[i])+1:]+s[i]

    return length
    


s="abcabcbb"
print(lengthOfLongestSubstring(s))
s="bbbbb"
print(lengthOfLongestSubstring(s))
s="pwwkew"
print(lengthOfLongestSubstring(s))

s="au"
print(lengthOfLongestSubstring(s))

s="dvdf"
print(lengthOfLongestSubstring(s))
# ord(s[i])+1==ord(s[i+1])

s="aabaab!bb"
print(lengthOfLongestSubstring(s))