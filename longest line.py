longest=''
filename=open("alp.py")
for line in filename:
    if(len(line)>len(longest)):
          longest=line
print("longest line is : ",longest,"\nand the length is : ",len(longest))
    
