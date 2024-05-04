def calculate(s:str):   
    def split_with_symbols(text):
        split_result = []
        i = 0
        while i < len(text):
            if text[i] in "+-":
                split_result.append(text[i])
                i += 1
            else:
                start_index = i
                while i < len(text) and text[i] not in "+-":
                    i += 1
                split_result.append(text[start_index:i])
        return split_result
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y    
    dictionary={"+":add,"-":subtract}
    s=split_with_symbols(s)
    
    
    
        
    stacks=[]
    stacksSize=-1
    for e in s:
        if e==" ": #空白建
            continue        
        if e==")": #右括弧             
            n=len(stacks[stacksSize])
            if n<3: return int(stacks[stacksSize][1])         
            i=0
            while n>0:
                if stacks[stacksSize][i] in "+-":
                    operation=dictionary[stacks[stacksSize][i]]
                    a=int(stacks[stacksSize][i-1])
                    b=int(stacks[stacksSize][i+1])
                    c=operation(a,b)
                    stacks[stacksSize][:]=stacks[stacksSize][4:]
                    stacks[stacksSize].insert(0,str(c))                
                    i=0
                    n-=4
                i+=1                 
            if stacksSize>0:    
                stacks[stacksSize-1].append(stacks[stacksSize].pop())                    
                stacks.pop()
                stacksSize-=1                                
        
        elif e=="(":#左括弧                        
            stacks.append([e])
            stacksSize+=1
        else:#數字
            if stacks:# stacks非空的
                stacks[stacksSize].append(e)    
            else: #stacks是空的                                
                stacks.append([e])
                stacksSize+=1
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

s="1+1"
print(calculate(s))


s=" 2-1+2"
print(calculate(s))


s="(1+(4+5+2)-3)+(6+8)"
print(calculate(s))

s="0"
print(calculate(s))
s="(0)"
print(calculate(s))