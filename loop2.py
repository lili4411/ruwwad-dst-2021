mult=1
nb=10 #init
while(nb<20): #condition
    mult=mult*nb
    nb=nb+1  #increment
print("the mult of the numbers:",mult)

name=input("enter a string of seven caracters")
nb=0
letter=0
digit=0
while(nb<len(name)):
    if(name[nb].isalpha()):
     letter=letter+1
    elif(name[nb].isdigit()):
        digit=digit+1
    nb=nb+1
print("the number of letters",letter)
print("the number of digits:",digit)


