birthdays={}
ans="y"
while ans=="y":
    name=input("enter a name :")
    bday=input("enter a birthday :")

    #if the name does not exist,add it.
    if name not in birthdays:
        birthdays[name]=bday
    else:
        print("that entry lready exists.")
    print("\nThe birthdays dictionry contains :",birthdays)
    ans=input("\nAdd another entry?(y for yes)")
print("\nName \t\t birthdays")
print("----------------------------")
for name in birthdays:
    print(name,"\t\t" , birthdays[name])
    
deleted_name=input("enter a name to delete")
del birthdays[deleted_name]
print(birthdays)

