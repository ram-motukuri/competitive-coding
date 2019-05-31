str1=input("please enter the string u want : ")
str2=sorted(str1.lower())
printed=[]
for alp in str2:
    if(alp not in printed):
        print(alp,"  ",str2.count(alp))
        printed.append(alp)
