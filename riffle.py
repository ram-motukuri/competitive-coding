ran=int(input(""))
ll = list(range(1,ran+1))
mid = len(ll)//2   
it1 = iter(ll[:mid])
it2 = iter(ll[mid:])
riff = sum(zip(it1,it2), ()) + tuple(it2)
print(riff)
