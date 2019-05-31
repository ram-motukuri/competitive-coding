t=int(input())
for i in range(t):
    r,c=map(int,input().split())
    row=list(map(int,input().split()))
    col=list(map(int,input().split()))
    if(sum(row)!=sum(col)):
        print("NO",end="")
    elif(max(row)==c and min(col)==0):
        print("NO",end="")
    else:
        row.sort(reverse=True)
        col.sort(reverse=True)
        k=0
        p=0
        l = [[0] * c for p in range(r)]
        for i in row:
            if(i==0):
                break
            else:
                for j in range(i):
                    l[k][j]=1
            k=k+1
        l=list(zip(*l))
        for i in range(c):
            if(l[i].count(1)+p<col[i]):
                print("NO",end="")
                break
            elif(l[i].count(1)+p>=col[i]):
                p=abs(l[i].count(1)-col[i]+p)
        else:
            print("YES",end="")
    print("")
            
