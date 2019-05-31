ran=int(input("please enter the range of fibnicco series : "))
num1,num2=0,1
fib=[]
sum=0
print("fibinicco series is : ",end=" ")
while(ran>0):
    fib.append(num1)
    temp=num1+num2
    num1=num2
    num2=temp
    ran=ran-1
    
print(fib.reverse())
for i in range(0,len(fib),2):
    sum=sum+fib[i]
print(sum)
