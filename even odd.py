min=int(input("enter the minimum number : "))
max=int(input("enter the maximum number : "))
print("even numbers in given range are :")
for num in range(min,max+1):    
    if(num%2==0):
        print(num)
print("odd numbers in given range are :")
for num in range(min,max+1):    
    if(num%2!=0):
        print(num)
