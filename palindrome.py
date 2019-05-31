num=int(input("please enter a number : "))
str=input("please enter a string : ")
reverse=0
n=num
while(num!=0):
    r=num%10
    reverse=reverse*10+r
    num=num//10
if(reverse==n and str==str[::-1]):
    print(n,"and",str,"are palindrome")
else:
    print(n,"and",str,"are not palindrome")

