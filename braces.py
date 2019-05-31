def braces(str):
    open=0
    error=0
    for x in str:
        if(x=='('):
            open=open+1
        if(x==')'):
            if(open>0):
                open-=1
            else:
                error+=1
        else:
            continue
    k=open+error
    return k 
print("Invalid string")

