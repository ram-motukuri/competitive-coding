class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

v=int(input())
e=int(input())
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
g=dict()
for i in range(e):
    a=input()
    s1.append(list(map(int,a.split("-"))))
for i in range(1,v+1):
    l=[]
    for j in s1:
        if(i in j):
            a=1-(j.index(i))
            l.append(j[a])
    g[str(i)]=list(map(str,l))
graph = Graph(g)
p=int(input())
for i in range(p):
    a=input()
    s3.append(a)
    s2.append(list(map(int,a.split("-"))))
for i in s2:
    i.sort()
    t=graph.find_all_paths(str(i[0]),str(i[1]))
    if(len(t)>0):
        for i in t:
            if((len(i)-1)%2!=0):
                s5.append(len(i)-1)
            else:
                s5.append(0)
    else:
        s5.append(0)
    s4.append(max(s5))
    s5=[]
if(max(s4)==0):
    print("NO",end="")
else:
    u=s4.count(max(s4))
    if(u>1):
        for i in range(u):
            if(i!=u-1):
                k=s4.index(max(s4))
                print(s3[k])
                s4[k]=0
            else:
                k=s4.index(max(s4))
                print(s3[k],end="")
                s4[k]=0
    else:
        k=s4.index(max(s4))
        print(s3[k],end="")
            
    

            
    
