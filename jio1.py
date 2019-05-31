t=int(input())
for i in range(t):
    a=int(input())
    l = list(map(int, input().split()))
    k= list(map(int, input().split()))
    for i in range(len(l)):
        b=sorted(k)[i]-sorted(l)[i]
        if(b<1):
            print("LOSE")
            break
    else:
        print("WIN")

