def wordPattern(pattern,s):
    s_splited=s.split(" ")
    if len(s_splited)!=len(pattern):
        return False
    histroy_p=dict()
    histroy_s=dict()
    
    for i in range(len(pattern)):                
        if pattern[i] not in histroy_p:
            histroy_p[pattern[i]]=s_splited[i]
        else:
            if histroy_p[pattern[i]]!=s_splited[i]:
                return False
        if s_splited[i] not in histroy_s:
            histroy_s[s_splited[i]]=pattern[i]
        else:
            if histroy_s[s_splited[i]]!=pattern[i]:
                return False
    return True      




pattern="abba"
s="dog cat cat dog"
print(wordPattern(pattern,s))
pattern="abba"
s="dog cat cat fish"
print(wordPattern(pattern,s))
pattern="aaaa"
s="dog cat cat dog"
print(wordPattern(pattern,s))