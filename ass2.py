def ascending(data):
    if(tuple(data)==tuple(sorted(list(data)))):
        return True
    else:
        return False
def valley(data):
    k=sorted(data)
    if(k.count(k[0])==1 and len(k)>2):
        v=[]
        s=[]
        for i in range(len(data)):
            if(data[i]==k[0]):
                break 
        for p in range(i):
            v.append(data[p])
        for q in range(len(data)-i-1):
            s.append(data[len(data)-q-1])
        b=sorted(list(set(v)))
        d=sorted(list(set(s)))
        b.reverse()
        d.reverse()
        if(v==b and s==d):
                     return True
        else:
            return False
    else:
        return False
def transpose(data):
    return([[data[i][j] for i in range(len(data))] for j in range(len(data[0]))])
def table():
	inputt=tuple(["Test Case " + str(i) for i in range(1,21)])
	outt=('ascending([7])','ascending([37,37,42,43,43])','ascending([9,23,27,26,39])','valley([2])','valley([13,12,14,14])','valley([5,4,3,2,1,2])','valley([17,1,2,3,4,5])','transpose([[19,14]])','transpose([[21,33,11],[42,64,16]])','transpose([[16,31,42],[26,82,73],[84,53,38]])','ascending([7])','ascending([7,7,7,7])','ascending([1,2,3,3,4,3])','valley([5,4,3,2,1,2,3,4,5,4,3,2,1])','valley([5,5,3,2,3,4,5])','valley([5,4,3,2,1,1,2,3,4,5])','valley([2,1,2])','transpose([[1,2,3,4,5]])','transpose([[17,23,4,44],[11,12,17,18],[19,27,12,88]])','transpose([[1],[2],[3],[4]])')
	out=(ascending([7]),ascending([37,37,42,43,43]),ascending([9,23,27,26,39]),valley([2]),valley([13,12,14,14]),valley([5,4,3,2,1,2]),valley([17,1,2,3,4,5]),transpose([[19,14]]),transpose([[21,33,11],[42,64,16]]),transpose([[16,31,42],[26,82,73],[84,53,38]]),ascending([7]),ascending([7,7,7,7]),ascending([1,2,3,3,4,3]),valley([5,4,3,2,1,2,3,4,5,4,3,2,1]),valley([5,5,3,2,3,4,5]),valley([5,4,3,2,1,1,2,3,4,5]),valley([2,1,2]),transpose([[1,2,3,4,5]]),transpose([[17,23,4,44],[11,12,17,18],[19,27,12,88]]),transpose([[1],[2],[3],[4]]))
	print('{:{align}{width}}'.format('',align='<', width='11'),'{:{align}{width}}'.format('INPUT', align='<', width='52'),'{:{align}{width}}'.format('OUTPUT\n', align='<', width='60'))
	for m in range(20):
		print('{:{align}{width}}'.format(inputt[m], align='<', width='11'),'{:{align}{width}}'.format(outt[m], align='<', width='52'),'{:{align}{width}}'.format(str(out[m]), align='<', width='60'))
table()

    
    
    
        
        
        
