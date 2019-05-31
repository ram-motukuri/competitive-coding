f1=open("sample.py")
f2=f1.read()
char=word=line=0
for i in f2:
    if(i!='\n'):
        char=char+1
    if(i==' ' or i=='\n'):
        word=word+1
    if(i=='\n'):
        line=line+1
print("no of words are : ",word)
print("no of characters are : ",char)
print("no of lines are : ",line)
