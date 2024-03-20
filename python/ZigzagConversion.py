

def convert(s,numRows):
    if numRows==1:
        return s
    ans=[[] for i in range(numRows)]
    
    if numRows==2:
        for j in range(len(s)):
            ans[j%numRows].append(s[j])
        pass        
    else:
        P=0
        for j in range(len(s)):        
            if P<numRows:                        
                ans[P].append(s[j])  
                P+=1          
            else:                        
                aa=(numRows-1)-(j%(numRows-1))            
                ans[aa].append(s[j])                 
                aaaa=2*numRows-3      
                if P==aaaa:
                    P=0
                else:    
                    P+=1  
    t=""
    for i in range(numRows):
        t=t+"".join(ans[i][:])                   
    return t
                    
s="PAYPALISHIRING";numRows=3
print(convert(s,numRows))

s="PAYPALISHIRING";numRows=4
print(convert(s,numRows))

s="A";numRows=1
print(convert(s,numRows))
