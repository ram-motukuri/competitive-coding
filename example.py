'''print("Let's see some examples.\n\nDid you notice the empty lines?")
print("Do you notice\t the tab space?\nDid you see that I have moved to next line?")
print("Do you want a \" in your text?")
print("Are you going to store more info about escape sequence in Z:\\\\user\\escape_sequence.txt??")
#Every print starts with a new line, end can change that behavior by specifying your own character
print("Did you see I start here", end=" ")
print("and I end in the same line although from a different print?")
print("As observed escape sequences help you to format your output.")
q=sum(list(map(lambda x:pow(x,3),list(map(int,str(a))))))
import math
n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
         print(i)
         print(n)
     i = i + 1
print (n)
def is_prime(a):
    return all(a % i for i in range(2,int(math.sqrt(int(a))+1)))
print(is_prime(int(9)))
empName = ['Jhon', 'Emma', 'Kelly', 'Jason']
empSalary = [7000, 6500, 9000, 10000]
print("Print Lists Before Shuffling")
print("List Employee Names: ", empName)
print("List Employee Salary: ", empSalary)
mapIndexPosition = list(zip(empName, empSalary))
random.shuffle(mapIndexPosition)
empName, empSalary = zip(*mapIndexPosition)
print("\nPrint Lists after Shuffling")
print("List Employee Names: ", empName)
print("List Employee Salary: ", empSalary)
import re
k="  abc de fgh"
print(re.search("Abc",k))'''
def func(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("T")
    finally:
        print("IF")
    print("XX")
func(3,0)
