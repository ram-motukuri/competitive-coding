def birday():
    year=month=day=0
    while(not(year>0)):
        year=int(input("Enter the year you were born : "))
    while(not(0<month<13)):
          month=int(input("Enter the month you were born : "))
    import calendar
    v=(calendar.monthrange(year,month)[1])
    print("no of days in ",calendar.month_name[month],"th month are : ",v)
    while(not(0<day<v+1)):
        day=int(input("Enter the day you were born : "))
    import datetime
    today=datetime.date.today()
    birthday=datetime.date(year,month,day)
    if(birthday>today):
        print("human from future !!!\nnever possible")
        birday()
    else:
        diff=today-birthday
        a=diff.days
        print("you have lived ",a,"days!!!")
birday()








        
