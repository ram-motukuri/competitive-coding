n=int(input(" no of people "))
l=[]
m=[]
print("enter names")
for i in range(n):
    k=input()
    l.append(k)
for row in range(n):
    m.append([])
    for col in range(n):
        m[row].append(0)
print("1\n2\n3")
s=int(input())
while(s!=3):
    if(s==1):
        b=input("name ")
        a=int(input("money "))
        c=round(a/n,3)
        for i in range(n):
            if(l[i]==b):
                for j in range(n):
                    m[i][j]=m[i][j]+c
        print(m)
        print("1\n2\n3")
        s=int(input())
    if(s==2):
        for i in range(n):
            for j in range(n):
                if(i==j):
                    m[i][j]=0
                    print
                elif(i<j):
                    if(m[i][j]<m[j][i]):
                        m[j][i]=m[j][i]-m[i][j]
                        m[i][j]=0
                    elif(m[i][j]==m[j][i]):
                        m[i][j]=0
                        m[j][i]=0
                    else:
                        m[i][j]=m[i][j]-m[j][i]
                        m[j][i]=0
        print("\t","\t".join(l),"\n")
        for i in range(n):
            print(l[i],end="\t")
            for j in range(n):
                print(m[i][j],end="\t")
            print("\n")
        print("1\n2\n3")
        s=int(input())
if(s==3):
    exit(0)
                    
        
    
