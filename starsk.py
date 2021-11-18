#variable=int(input("enter n:"))
#for i in range (1,variable+1):
  #  name=input("enter name"+str(i))

n=int(input("enter n"))
names=" "
for i in range (1,n+1):
    name=input("enter a name")
    names=names+name+"\n"
print(names)