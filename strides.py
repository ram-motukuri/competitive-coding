arr = list(map(str,input().rstrip().split()))
print(arr)
k=[]
l=arr
p=arr
for i in arr:
    if(1<=i<=10**9):
        k.append(sum(arr)-i)
print(min(k)," ",max(k))
    
