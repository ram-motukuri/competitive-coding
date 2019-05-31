plys=int(input("enter the number of players : "))
import itertools,random
deck=list(itertools.product(['A','2','3','4','5','6','7','8','9','10','J','K','Q'],['Spades','Hearts','Diamonds','Clubs']))
for x in range(plys):
    print("cards randomly distibuted to player",x+1,"are : ")
    random.shuffle(deck)
    for i in range(13):
        print(deck[i][0],"of",deck[i][1])

