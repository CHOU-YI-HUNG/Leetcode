


def IntToRoman(num):   
    DictRomam={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}            
    num_s=str(num)
    n=len(num_s)
    ans=""
    while num>0:
        if num>=1000:
           dig=num//1000                          
           ans+="M"*dig 
           num-=1000*dig          
        elif num>=900:
            RomanNumber="IVXLC"
            for e in RomanNumber:
                if num>=num-DictRomam[e]:
                    ans+=e 
                    num-=num-DictRomam[e] 
                    break                           
            ans+="M"  
        elif num>=400:
            if num>=500:
                ans+="D"
                num-=500                 
            else:    
                RomanNumber="IVXLC"
                for e in RomanNumber:
                    if num>=num-DictRomam[e]:
                        ans+=e 
                        num-=num-DictRomam[e] 
                        break                           
                ans+="D"  
        elif num>=90:
            if num>=100:
                ans+="C"*(num%100)
                num-=100*(num%100)
            else:
                RomanNumber="IVX"
                for e in RomanNumber:
                    if num>=num-DictRomam[e]:
                        ans+=e 
                        num-=num-DictRomam[e] 
                        break                           
                ans+="C"   
        elif num>=40:                       
            if num>=50:
                ans+="L"
                num-=50
            else:    
                RomanNumber="IVX"
                for e in RomanNumber:
                    if num>=num-DictRomam[e]:
                        ans+=e 
                        num-=num-DictRomam[e] 
                        break                           
                ans+="L"    
        else:                        
            if num>=10:                
                ans+="X"*(num%10)
                num-=10*(num%10)
            elif num>=5:
                if num==9:
                    ans+="IX"
                    num-=9
                else:   
                    ans+="V"
                    num-=5                                         
            else:
                if num==4:
                    ans+="IV"
                    num-=9
                else:                                          
                    ans+="I"*num
                    num-=num
    return ans                    
                    


# num="I"*3
# print(num)
num=3
print(IntToRoman(num))
num=58
print(IntToRoman(num))
num=1994
print(IntToRoman(num))
