num=int(input("please enter a valid number : "))
n=num
cube=0
while(num!=0):
    rem=num%10
    cube=cube+(rem**3)
    num=num//10
if(n==cube):
    print(n,"is a amstrong number")
else:
    print(n,"is a not amstrong number")
