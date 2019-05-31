t=int(input())
for i in range(t):
    num=int(input())
    num1=str(num)
    l=len(num1)
    v=0
    while('4' in set(num1)):
        k=num1.find('4')
        p=l-1-k
        v=v+(10**p)
        s=num-(10**p)
        num1=str(s)
        num2=str(v)
        num=s
    print("Case #"+str(i+1)+": "+num1+" "+num2)
    

