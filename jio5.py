def minMoves(arr, n): 
    expectedItem = n 
    for i in range(n - 1, -1, -1): 
        if (arr[i] == expectedItem): 
            expectedItem -= 1
    return expectedItem
t=int(input())
l=[]
for i in range(t):
    k=int(input())
    l.append(k)
s=sorted(l)
if(s==l):
    print(minMoves(l,t)-1,end="")
else:
    print(minMoves(l,t),end="")
