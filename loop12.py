#write a program that ask the user 
#to enter a number then output the table
#of multiplication for this number using for loop
#ex:enter a number :4
#4*1=4
#4*2=8
#4*3=12
#......
#4*10=40


nb=int(input("enter your numbers"))
s=0
for a in range (1,11):
    mult=a*nb
    print(nb,"*",a,"=",mult)

