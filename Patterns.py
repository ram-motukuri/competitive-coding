t=int(input())
l=[]
for i in range(t):
    l.append(t)
for i in range(t+1):
    if(i==0):
        print((" ")*(t-i+8),"  *"," ".join(list(map(str,l[0:i]))))
    else:
        print(("  ")*(t-i),"  *  ","  ".join(list(map(str,l[0:i]))),"  *")
    
    
