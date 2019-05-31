str='+','-','*','**','/','//','%'
for sym in str:
    x=int(input("please  enter the first numbers : "))
    y=int(input("please  enter the second numbers : "))
    sym=input("please enter the symbol : ")
    if(sym=='+'):
        print(x,sym,y,"=",x+y)
    elif(sym=='-'):
        print(x,sym,y,"=",x-y)
    elif(sym=='*'):
        print(x,sym,y,"=",x*y)    
    elif(sym=='**'):
        print(x,sym,y,"=",x**y)
    elif(sym=='/'):
        print(x,sym,y,"=",x/y)
    elif(sym=='%'):
        print(x,sym,y,"=",x%y)
    elif(sym=='//'):
        print(x,sym,y,"=",x//y)
    else:
        print("wrong symbol")
        break
