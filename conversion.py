def dec_to_bin():
    num=int(input("enter a decimal number : "))
    bin=[]
    while(num!=0):
            d=num%2
            num=num//2
            bin.append(d)
    print("binary number = ",end=" ")
    print(*bin[::-1],sep="")
dec_to_bin()
def dec_to_oct():
    num=int(input("\nenter a decimal number : "))
    oct=[]
    while(num!=0):
            d=num%8
            num=num//8
            oct.append(d)
    print("octal number = ",end=" ")
    print(*oct[::-1],sep="")
dec_to_oct()
def dec_to_hex():
    num=int(input("\nenter a decimal number : "))
    hex=[]
    str="0123456789ABCDEF"
    while(num!=0):
            d=num%16
            num=num//16
            hex.append(str[d])
    print("hexa number = ",end=" ")
    print(*hex[::-1],sep="")
dec_to_hex()
