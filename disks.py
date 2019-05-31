amount=int(input("please enter the amount you have : Rs."))
num=amount//500
rem=amount%500
print("no of disks you can buy is ",num)
if(rem!=0):
    bal=500-rem
    print("remaining amount you want to buy another disk is : Rs.",bal)
