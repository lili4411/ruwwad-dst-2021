# for a in range(1,6):
#     print("*")
# print("* * * * * * *")

#name=input("enter a name:")
# print(name.find("ane",2,4))
# name=name.replace("ane","one")
#print(name)
#print(name.isalnum())

# for i in range (1,5):
#     for k in range(1,6):
#         print(" ",end=" ")
#     print("***")

for i in range(1,5):
    for sp in range(1,5-i):
        print("-",end="")
    for pls in range(1,i):
        print("+",end=" ")
    for st in range(1,4):
        print("*",end=" ")
    print()    