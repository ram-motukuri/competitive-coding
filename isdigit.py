t=input()
v=[]
for i in t:
    if(i.isdigit()==1):
        v.append(i)
if(t[0]=='-'):
    v.reverse()
    v.append('-')
    v.reverse()
    k="".join(v)
    print(k,end="")
else:
    k="".join(v)
    print(k,end="")
