t=int(input())
buildings=[]
s=0
for i in range(t):
    k=input()
    buildings.append(tuple(map(int,k.split("#"))))
buildings.sort()
edges = []
edges.extend([building[0],building[2]] for building in buildings)
edges = sorted(sum(edges,[]))
edges=list(set(edges))
edges.sort()
current = 0
points = [(edges[0],0)]
for i in edges:
  active = []
  active.extend(building for building in buildings if (building[0] <= i and building[2] > i))
  if not active:
    current = 0
    points.append((i,0))
    continue
  max_h = max(building[1] for building in active)
  if max_h != current:
    current = max_h
    points.append((i,max_h))
for i in points:
    s=s+1
    if(s==len(points)):
        print('#'.join(list(map(str,i))),end="")
    else:
        print('#'.join(list(map(str,i))))

    
