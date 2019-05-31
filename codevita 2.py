def urns():
    N,p=map(float,input("").split(","))
    if(2<N<=20000 and 0<p<=1):
        count=0
        for j in range(2,int(N)+1):
            for k in range(2,int(N)+1):
                if(k>=j):
                    v=((j/k)*(j-1)/(k-1))
                    if(v==p):
                        print(v,j)
                        count=count+1
        print(count)
    else:
        urns()
urns()
    
    
    


