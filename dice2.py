from random import*
def roll():
    dice1=randint(1,6)
    dice2=randint(1,6)
    return(dice1,dice2)
sum=counter=i=0
while(i<4):
    num=0
    while(not(2<=num<=12)):
        num=int(input("please enter the number between 2 and 12 : "))
        print("sum\tdice1\tdice2\ttrail")
    while(num!=sum):
        d1,d2=roll()
        sum=d1+d2
        counter=counter+1
        print(sum,"\t",d1,"\t",d2,"\t",counter)
    print(counter)
    counter=0


