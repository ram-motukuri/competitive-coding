cityno=[1,2,3,4,5,6,7,8,9,10]
hopform=[('HYD','DEL'),('DEL','HYD'),('DEL','GAU'),('GAU','DEL'),('HYD','RJY'),('RJY','HYD'),('HYD','CCU'),('CCU','HYD'),('HYD','BOM'),('HYD','PNQ'),('HYD','VTZ'),('HYD','DEL'),('HYD','BLR'),('HYD','BOM'),('HYD','CCU')]
destination=['Hyderabad','Delhi','Bangalore','Guwahiti','Rajahmundry','Mumbai','Ahemedabad','Visakhapatnam','Kolkata','Pune']
flightcode=['FW1','FW2','FW3','FW4','FW5','FW6','FW7','FW8','FW9','FWA','FWB','FWC','FWD','FWE','FWF']
flighthop=[(1,2),(2,1),(2,4),(4,2),(1,5),(5,1),(1,9),(9,1),(1,6),(1,10),(1,8),(1,2),(1,3),(1,6),(1,9)]
fare=[5670,5670,6000,6000,4000,4000,6000,6000,5500,4500,4500,5670,4000,4500,6000]
timings=[('07:00','09:30'),('10:40','13:00'),('10:40','12:40'),('14:00','16:00'),('14:00','15:00'),('16:00','17:00'),('18:15','20:45'),('03:30','06:00'),('16:30','18:00'),('08:00','09:00'),('09:00','10:30'),('18:30','20:00'),('18:30','19:45'),('18:30','20:00'),('19:30','22:00')]
timediff=['02:30','02:20','02:00','02:00','01:00','01:00','02:30','02:30','01:30','01:00','01:30','01:30','01:15','01:30','02:30']
k=[]
hop=[]
finalhop=[]
finalfare=[]
def FROMCITY(): 
    fromcity=input("Please enter the city you want to start from : ")
    if(fromcity in destination):
        def TOCITY():
            tocity=input("Please enter the city you want to go : ")
            if(tocity in destination and fromcity!=tocity):
                for city in range(len(destination)):
                    if(destination[city]==fromcity):
                        fromcitynum=city+1
                    if(destination[city]==tocity):
                        tocitynum=city+1
                for numhop in range(len(flighthop)):
                    if(flighthop[numhop][0]==fromcitynum or flighthop[numhop][1]==tocitynum):
                        hop.append(flighthop[numhop])
                for hop1 in range(len(hop)):
                    for hop2 in range(len(hop)):
                        if(hop[hop1][1]==hop[hop2][0]):
                            if hop[hop1] not in finalhop or hop[hop2] not in finalhop:
                                finalhop.append(hop[hop1])
                                finalhop.append(hop[hop2])
                if(len(finalhop)==0):
                    print("There is no journey")
                else:
                    for j in range(len(flighthop)):
                        for i in finalhop:
                            if i not in k:
                                if(flighthop[j]==i):
                                    k.append(flighthop[j])
                                    finalfare.append(fare[j])
                    if(fromcity!=tocity):
                        waittimehrs=int(input("please enter the no of hrs : "))
                        waittimemin=int(input("please enter the minutes : "))
                        waittimeinhrs=waittimehrs+(waittimemin/60)
                        if(waittimeinhrs<=1 or waittimeinhrs>=5):
                            print("no count")
                        if(waittimeinhrs>1 and waittimeinhrs<=2):
                            total=0.9*sum(finalfare)
                            print(total)
                        if(waittimeinhrs>2 and waittimeinhrs<=4):
                            total=0.7*sum(finalfare)
                            print(total)
                        if(waittimeinhrs>4 and waittimeinhrs<5):
                            total=0.6*sum(finalfare)
                            print(total)
                        for i in range(len(flighthop)):
                            if(flighthop[i]==finalhop[0]):
                                a=timings[i][1].split(":")
                                print(a)
                                break
                        for i in range(len(flighthop)):
                            if(flighthop[i]==finalhop[1]):
                                b=timediff[i].split(":")
                                print(b)
                                break
                        hrs=int(a[0])+int(b[0])+waittimehrs
                        print(hrs)
                        minutes=int(a[1])+int(b[1])+waittimemin
                        print(minutes)
                        if(minutes>=60):
                                hrs=hrs+minutes//60
                                minutes=minutes%60
                        if(hrs>23):
                                hrs=hrs-24
                        print("total time for journey is : ",hrs,":",minutes) 
            else:
                print("you have to enter the correct destination")
                TOCITY()
        TOCITY()
    else:
        print("You have to enter the correct city u want to traval from ")
        FROMCITY()
FROMCITY()


                    

            

