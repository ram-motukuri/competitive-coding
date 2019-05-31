L1=[]
for x in range(0,26):
    k=chr(ord('a')+x)
    L1.append(k)
print(L1)
L2=['apple','ball','cat','dog','egg','fan','gun','hat','ink','jug','kid','lion','man','nun','ox','pen','quick','rat','star','tax','unicorn','van','water','xerox','yak','zebra']
for y in range(0,26):
    print(L1[y],"for",L2[y])
