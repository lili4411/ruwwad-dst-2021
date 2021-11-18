i=0
positivenumber=0
negativenumber=0
while(i<5):
     n=int(input("enter five numbers:"))
     if(n>=0):
        positivenumber=positivenumber+1
     elif(n<=0):
        negativenumber=negativenumber+1
     i=i+1
     
print("the nb of negative numbers:",negativenumber)
print("the nb of positive numbers:",positivenumber)
    







