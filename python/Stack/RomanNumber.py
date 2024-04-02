
def RomanNumber(s):
    DictRomam={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}       
    n=len(s)
    number=0    
    i=0
    flag=0
    while i<n-1:  
        if DictRomam[s[i]]<DictRomam[s[i+1]]:
            number+=DictRomam[s[i+1]]-DictRomam[s[i]]            
            if i==n-2:
                flag=1
            i+=2
        else:
            number+=DictRomam[s[i]]    
            i+=1
    if flag!=1:        
        number+=DictRomam[s[i]]
        
                
    return number
    
s="CCCIC"    
print(RomanNumber(s))
# s="LVIII"
# print(RomanNumber(s))
# s="MCMXCIV"
# print(RomanNumber(s))
