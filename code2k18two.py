import math
from decimal import Decimal, ROUND_HALF_UP
v1=int(input())
r1=int(input())
v2=int(input())
r2=int(input())
N=float(input())
if(0<v1<=360 and 0<v2<=360 and 0<r1<r2<=100 and 0<N<=100):
    deg1=v1*N
    deg2=v2*N
    x1=r1*math.cos(math.radians(deg1))
    y1=r1*math.sin(math.radians(deg1))
    x2=r2*math.cos(math.radians(deg2))
    y2=r2*math.sin(math.radians(deg2))
    dist=math.sqrt((pow((x1-x2),2))+(pow((y1-y2),2)))
    dis=Decimal(dist).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    print(dis,end="")
