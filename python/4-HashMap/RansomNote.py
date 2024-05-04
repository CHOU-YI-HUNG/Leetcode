
def serch(e,magazine):
    for i in range(len(magazine)):
        if magazine[i]==e:
            return True, i
    return False, 0
        
def canConstruct(ransomNote,magazine):
    
    for i in range(len(ransomNote)):
        Exists, Index=serch(ransomNote[i],magazine)
        if Exists:
            magazine=magazine[:Index]+magazine[Index+1:]
        else:
            return False
    return True
    
    
    


ransomNote="a"
magazine="b"

print(canConstruct(ransomNote,magazine))

ransomNote="aa"
magazine="ab"
print(canConstruct(ransomNote,magazine))

ransomNote="aa"
magazine="aab"
print(canConstruct(ransomNote,magazine))
