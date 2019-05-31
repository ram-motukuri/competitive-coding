num=int(input(""))
l=[]
m=[]
for i in range(100,num+1):
    l.append(i)
l.reverse()
for j in range(0,len(l)):
    x=[int(v) for v in str(l[j])]
    p=len(x)-2
    for k in range(0,p):
        if((x[k]>x[k+1]<x[k+2] or x[k]<x[k+1]>x[k+2]) and ((x[0]%2==0 or x[len(x)-1]%2==0) or (len(x)%2==0))):
            m.append(x)
k=int(''.join(str(digit) for digit in m[0]))
print(k)
          


        
       
        
