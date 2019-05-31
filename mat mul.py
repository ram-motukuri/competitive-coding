matrix1=[]
matrix2=[]
result=[]
print("9 Elements of matrix 1 are :")
for row in range(3):
    matrix1.append([])
    for col in range(3):
        element=int(input())
        matrix1[row].append(element)
print("\n9 Elements of matrix 2 are :")
for row in range(3):
    matrix2.append([])
    for col in range(3):
        element=int(input())
        matrix2[row].append(element)
print(matrix2,matrix2[0])
for row in range(len(matrix1)):
    result.append([])
    for col in range(len(matrix2[0])):
        res=0
        for k in range(len(matrix2)):
            res+=matrix1[row][k]*matrix2[k][col]
        result[row].append(res)
print("\nresult is :",result)


        
        
    
