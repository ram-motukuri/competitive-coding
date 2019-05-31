while(1):
    t=int(input())
    while(t!=int(str(t)[::-1])):
        t=t+int(str(t)[::-1])
    print(t)
