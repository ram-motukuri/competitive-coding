def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def merge(l):
    k="".join(list(map(str,l)))
    return int(k)
t=int(input())
star=[0]
adj=[]
graph={}
node=0
path=[]
s=-1
r=[]
w=[]
for i in range(t):
    k=int(input())
    star.append(k)
m=int(input())
n=int(input())
for i in range(m):
    k=input()
    adj.append(list(map(int,k.split(" "))))
for i in adj:
    node=node+1
    k=[]
    for j in range(len(i)):
        if(i[j]==1):
            k.append(j+1)
    graph[node]=k
v=find_all_paths(graph,1,4,path)
v.sort()
for p in v:
    s=s+1
    for q in range(len(p)):
        v[s][q]=star[v[s][q]]
r=list(tuple(v))
for i in range(len(v)):
    for j in v[i]:
        if(merge(v[i])%j!=0):
            r.remove(v[i])
            break
if(len(r)==0):
    print(-1,end="")
else:
    for i in r:
        w.append(sum(i))
    print(min(w),end="")
        

        
    
    
    
    
