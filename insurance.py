income=int(input("annual income of the person : "))
if(income<=400000):
    print("no tax for this person : ")
else:
    gender=input("gender : ")
    age=int(input("age of the person is : "))
    if(gender=='M'):
        if(age<60):
            print("Income tax is : ",(income-250000)*0.1)
        else:
            print("income tax is : ",(income-300000)*0.1)
    elif(gender=='F'):
        if(age<60):
            print("income tax is : ",(income-300000)*0.1)
        else:
            print("income tax is : ",(income-350000)*0.1)
    else:
        print("no proper gender ")
