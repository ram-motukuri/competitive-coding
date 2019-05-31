#SMALLEST MULTIPLE IN PERMUTED DIGITS!!!

def small():
    #please enter the first integer N
    N=int(input(""))
    #please enter the number(d) that have to divide N
    d=int(input(""))
    #checking the range of N and r
    if(N in range(1,1000000000001) and d in range(1,1000001) and N>d):
        #importing the respective library functions 
        from itertools import permutations
        #converting the number N into a list and sorting it
        l=sorted([int(x) for x in str(N)])
        #getting all the wanted permutations of number N 
        k=[a for a in permutations(l)]
        #looping all the permutes by converting each permute back into integer and performing the logic of dividing N by the smallest multiple of d has leading zeros eliminated
        for i in range(0,len(k)):
            v=int(''.join(map(str,k[i])))
            if(v%d==0):
                print(v)
                break
            #breaking when the required answer is got
        else:
            #else when no permuted number of N is divided by least multiple of d then printing the output as -1
            print(-1)
    #if N and d are out of range we have to re-enter the values of r
    else:
        print("integer values are out of range!!\nRe-enter your numbers\n")
        small()
small()


