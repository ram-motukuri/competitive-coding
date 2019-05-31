from random import*
def roll():
    dice1=randint(1,6)
    dice2=randint(1,6)
    return(dice1,dice2)
sum=num=counter=0
amount=int(input("enter the amount you wanna keep in cassino = "))
while amount!=0:
        num=int(input("please enter the number between 2 and 12 : "))
        if(2<=num<=12):
            print("sum\tdice1\tdice2\ttrail")
            while(num!=sum):
                d1,d2=roll()
                sum=d1+d2
                counter=counter+1
                print(sum,"\t",d1,"\t",d2,"\t",counter)
            if(counter<=5):
                amount=amount+100
                print("amount : ",amount)
                counter=0
                if(amount<=0):
                    print("cannot continue due to insufficient amount!!! = ",amount)
                else:
                    print("1.quit\n2.continue")
                    choice=int(input("please enter your choice : "))
                    if(choice==1):
                        print("you have quited\nyour final amount remained is : ",amount)
                        break
                    else:
                        print("current amount is : ",amount,"\nyou can continue")
            elif(6<=counter<=10):
                amount=amount+50
                print("amount : ",amount)
                counter=0
                if(amount<=0):
                    print("cannot continue due to insufficient amount!!! = ",amount)
                else:
                    print("1.quit\n2.continue")
                    choice=int(input("please enter your choice : "))
                    if(choice==1):
                        print("you have quited\nyour final amount remained is : ",amount)
                        break
                    else:
                        print("current amount is : ",amount)
            else:
                amount=amount-50
                print("amount : ",amount)
                counter=0
                if(amount<=0):
                    print("cannot continue due to insufficient amount!!! = ",amount)
                else:
                    print("1.quit\n2.continue")
                    choice=int(input("please enter your choice : "))
                    if(choice==1):
                        print("you have quited\nyour final amount remained is : ",amount)
                        break
                    else:
                        print("current amount is : ",amount)
        else:
            print("should enter a number between 2 and 12!!")
                                        

    
