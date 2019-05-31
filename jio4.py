t=int(input())
a=3
b=c=0
l=[]
if(t>0):
    for i in range(t+1):
        c=c+(a*a-b*b)
        b=a
        a=a+2
    print(c)
else:
    print(str(8))
