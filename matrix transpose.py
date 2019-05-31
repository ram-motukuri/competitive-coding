matrix1=[]
matrix2=[]
result=[]
print("Elements of matrix 1 are :")
for row in range(3):
    matrix1.append([])
    for col in range(3):
        element=int(input("enter an element : "))
        matrix1[row].append(element)
print("\nElements of matrix 2 are :")
for row in range(3):
    matrix2.append([])
    for col in range(3):
        element=int(input("enter an element : "))
        matrix2[row].append(element)
for row in range(3):
    result.append([])
    for col in range(3):
        result[row].append(matrix1[row][col]+matrix2[row][col])
print("\nresult is :",result)


        
        
    
