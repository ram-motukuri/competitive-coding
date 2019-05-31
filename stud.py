num=int(input("please enter a number : "))
if num in range(1,21):
    print("Name   : pragati",num)
    print("age    : 20 years")
    if(num>10):
        print("gender : male")
    else:
        print("gender : female")
    if(num%2==0):
        print("marks  : 90%")
    else:
        print("marks  : 95%")
    print("roll number : ",num+100)
else:
    print("given number is not in range")
