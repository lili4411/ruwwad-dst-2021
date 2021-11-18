#write a python program that requires the user
#to login to his mobile ,if the pincode is in correct 
#let him repeat entering it till he eneters the correct code

code=int(input("give me the pincode"))
pincode=123
while (code!=pincode):
    print("the pincode is incorrect")
    code=int(input("give me the pincode"))
else:
    print("the pincode is correct")
