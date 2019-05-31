#python program for perfect number
def perfect(n):
    factor=[i for i in range(1,n) if n%i==0]
    if(sum(factor)==n):
        return True
    else:
        return False

#python program for depth of a given string
def depth(s):
        open=0
        error=0
        for x in s:
            if(x=='('):
                open=open+1
            if(x==')'):
                if(open>0):
                    open-=1
                else:
                    error+=1
            else:
                continue
        k=open+error
        if(k>0):
            print("invalid string ")
        else:
            count=0
            k=[]
            for i in s:
                if(i=='('):
                    count=count+1
                elif(i==')'):
                    k.append(count)
                    count=0
                else:
                    k.append(0)
            return(max(k))
            

#python program for sum of perfect squares in a given list
def sumsquares(l):
    sum=0
    for i in l:
        if((i**0.5)-int(i**0.5)==0):
            sum=sum+i
    return(sum)


def table():
	innput=tuple(["Test Case " + str(i) for i in range(1,19)])
	output=('perfect(6)','perfect(12)','perfect(8128)','depth("33")','depth("(a+b)(c-d)(e+f)")','depth("sqrt((2(b*b-4ac)+33)-64)")','sumsquares([3,9,12,16])','sumsquares([5,6,7,8])','sumsquares([64,676,1024])','perfect(28)','perfect(77)','perfect(33550336)','depth("a3f7+ag343")','depth("()((((()))))")','depth("()()(())(())((()))(((())))")','sumsquares([625,676,729])','sumsquares([23,31,47,55,77])','sumsquares([1048576, 145924, 5184])')
	output1=(perfect(6),perfect(12),perfect(8128),depth("33"),depth("(a+b)(c-d)(e+f)"),depth("sqrt((2(b*b-4ac)+33)-64)"),sumsquares([3,9,12,16]),sumsquares([5,6,7,8]),sumsquares([64,676,1024]),perfect(28),perfect(77),perfect(33550336),depth("a3f7+ag343"),depth("()((((()))))"),depth("()()(())(())((()))(((())))"),sumsquares([625,676,729]),sumsquares([23,31,47,55,77]),sumsquares([1048576, 145924, 5184]))
	print('{:{align}{width}}'.format('TESTCASE', align='<', width='13'),'{:{align}{width}}'.format('TESTCASE INPUT', align='<', width='40'),'{:{align}{width}}'.format('OUTPUT\n', align='<', width='30'))
	for v in range(18):
		print('{:{align}{width}}'.format(innput[v], align='<', width='13'),'{:{align}{width}}'.format(output[v], align='<', width='40'),'{:{align}{width}}'.format(str(output1[v]), align='<', width='30'))
table()

    
    
            


