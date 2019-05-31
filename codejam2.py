from itertools import permutations
t=int(input())
for j in range(t):
    s=int(input())
    v=input()
    u=list(v)
    if(len(u)>2):
        if(u[1]=='S'):
            m=u[2:len(u)].index('V')
        else:
            m=u[2:len(u)].index('S')
        for i in range(len(u)):
            if(i!=1 and i!=m+2):
                if(u[i]=='S'):
                           u[i]='E'
                else:
                           u[i]='S'
        print("Case #"+str(j+1)+": "+''.join(u))
    else:
         print("Case #"+str(j+1)+": "+''.join(u[::-1]))
       
                   
    
  
