#Fibonacci Right Triangles

#importing the library function 
from math import sqrt
#declaring consecutive terms of a fibnicco series
#next is sum of those consecutive terms
t1,t2,next=0,1,0;
#entering the positive integer for FART 
n=int(input(""))
#creating a empty list 
lt=[]
#appending values of t1,t2 in list lt
lt.append(t1)
lt.append(t2)
next = t1 + t2
#repeating the loop until recent next is less than or equal to number n 
while(next <= n):
    lt.append(next)
    t1 = t2
    t2 = next
    next = t1 + t2
lt.append(next)
#checking whether least number in list is even or odd
if((len(lt)-1) % 2 == 0):
    t1 = t2
    t2 = next
    next = t1 + t2
    lt.append(next)
#repeating the loop until the required element is odd
while(lt[len(lt)-1] % 2 ==0 or (len(lt)-1) % 2 == 0):
    t1 = t2
    t2 = next
    next = t1 + t2
    lt.append(next)
#getting the hypotenuse 
hyp=lt[len(lt)-1]
#getting the longest side
long_sd=int(hyp*(2/sqrt(5)))
#getting the shortest side
short_sd=int(sqrt(hyp**2 - long_sd**2))
#checking the required FART conditions
if((short_sd**2) + (long_sd**2) != hyp**2):
    long_sd = long_sd + 1
    short_sd=int(sqrt(hyp**2 - long_sd**2))
if(long_sd % 2 == 0):
    fact = long_sd
elif(short_sd % 2 == 0):
    fact = short_sd
lt2=list()
#printing the no of factors for the highest even number other than hypotenuse
for i in range(1,fact+1):
    if(fact % i == 0):
        lt2.append(i)
print(len(lt2))
