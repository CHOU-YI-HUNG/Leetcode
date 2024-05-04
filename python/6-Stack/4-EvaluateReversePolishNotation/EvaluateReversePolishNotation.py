def evalRPN(tokens):
    # 遇到數字push
    # 遇到+,-,*,/ pop
    def sign(num):
        return -1 if num<0 else 1
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def mutilply(x,y):
        return x*y
    def divition(x,y):        
        return (abs(x)//abs(y))*sign(y)*sign(x)
    dictionary={"+":add,"-":subtract,"*":mutilply,"/":divition}
    stack=[]
    for token in tokens:
        if token in "+-*/":
            operation=dictionary[token]
            a=stack.pop()
            b=stack.pop()
            c=operation(b,a)
            stack.append(c)
        else:
            stack.append(int(token))    
    return stack.pop()



tokens=["2","1","+","3","*"]
print(evalRPN(tokens))


tokens=["4","13","5","/","+"]
print(evalRPN(tokens))

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))






