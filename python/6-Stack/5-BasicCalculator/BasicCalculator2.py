def calculate(s:str):   
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y    
    dictionary={"+":add,"-":subtract}                        
    stacks=[]
    stacksSize=-1
    i=0
    while i<len(s):
        if s[i]==" ": #空白建
            i+=1
            continue        
        if s[i]==")": #右括弧             
            n=len(stacks[stacksSize])
            if n<3: return int(stacks[stacksSize][1])         
            j=0
            while n>0:
                if stacks[stacksSize][j] in "+-":
                    operation=dictionary[stacks[stacksSize][j]]
                    a=int(stacks[stacksSize][j-1])
                    b=int(stacks[stacksSize][j+1])
                    c=operation(a,b)
                    stacks[stacksSize][:]=stacks[stacksSize][4:]
                    stacks[stacksSize].insert(0,str(c))                
                    j=0
                    n-=4
                j+=1                 
            if stacksSize>0:    
                stacks[stacksSize-1].append(stacks[stacksSize].pop())                    
                stacks.pop()
                stacksSize-=1                                
        
        elif s[i]=="(":#左括弧                        
            stacks.append([s[i]])
            stacksSize+=1
        elif s[i] in "+-":
            stacks[stacksSize].append(s[i])    
        else:#數字
            digit=0
            while i<len(s) and s[i] not in"+-() ":
                digit=digit*10+int(s[i])
                i+=1                
            if stacks:# stacks非空的                
                stacks[stacksSize].append(str(digit))    
            else: #stacks是空的                                
                stacks.append([str(digit)])
                stacksSize+=1
            continue
        i+=1
    n=len(stacks[stacksSize])
    
    if n<3: return int(stacks[stacksSize][0])         
    i=0
    while n>0:
        if stacks[stacksSize][i] in "+-":
            operation=dictionary[stacks[stacksSize][i]]
            a=int(stacks[stacksSize][i-1])
            b=int(stacks[stacksSize][i+1])
            c=operation(a,b)
            stacks[stacksSize][:]=stacks[stacksSize][3:]
            stacks[stacksSize].insert(0,c)                
            i=0
            n-=3
        i+=1

    return stacks[stacksSize].pop()

s="11+1"
print(calculate(s))
s="1-(     -2)"
print(calculate(s))
s=" 2-1+2"
print(calculate(s))


s="(1+(4+5+12)-3)+(6+8)"
print(calculate(s))

s="0"
print(calculate(s))
s="(0)"
print(calculate(s))