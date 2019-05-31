def emi(amt,rate,yr):
    EMI = amt * (rate/12.0) /( 1 -( 1 / ((1 + (rate/12.0))**(yr * 12))))
    return EMI
l1=[]
l2=[]
P=int(input())
T=int(input())
if(1 <= P <= 1000000 and 1 <=T <= 50):
    N1=int(input())
    if(1<= N1 <= 30):
        for i in range(N1):
            year,rate=input().split()
            year=int(year)
            rate=float(rate)
            k=emi(P,rate,year)*year
            l1.append(k)
        sumA=sum(l1)
        N2=int(input())
        if(1<= N2 <= 30):
            for i in range(N2):
                year,rate=input().split()
                year=int(year)
                rate=float(rate)
                k=emi(P,rate,year)*year
                l2.append(k)
            sumB=sum(l2)
    if(sumA<sumB):
        print("Bank A",end="")
    else:
        print("Bank B",end="")
            
