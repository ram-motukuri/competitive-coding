p=int(input())
a=[]
b=[]
for i in range(p):
    det = list(map(str,input().rstrip().split()))
    a.append(det)
    det=[]
fin=list(map(int,input().rstrip().split()))
for i in range(fin[1]):
    ids= list(map(str,input().rstrip().split()))
    b.append(ids)
    ids=[]
print(a,b)
    
    
