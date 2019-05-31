def prime():
    ran=int(input("please enter the range :"))
    if(ran<2):
        print("prime numbers doesnot exist!!")
        prime()
    else:
        print("prime numbers upto ",ran," are : ",end=" ")
        for num in range(2,ran+1):
            if(num>1):
                for x in range(2,num):
                    if(num%x==0):
                        break
                else:
                    print(num,end=" ")
prime()
