def sorting(s):
    u=[]
    for i in s:
        u.append(i)
    w=[]
    for x in u:
        if x not in w:
            w.append(x)
    a=''.join(sorted(w))
    return(a)
string=input()
v=len(sorting(string))
str1=sorting(string)
for j in range(len(string)):
    for i in range(len(string)-v+1-j):
        x=sorting(string[i:v+i+j])
        if(x==str1):
            print(string[i:v+i+j])
            break
    else:
        continue
    break

    


