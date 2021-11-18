n=int(input("enter N :"))
m=int(input("enter M :"))
i=n
sum=0
print("the sum of",end=" ")
while(i<m):
    sum=sum+i
    print(i,end="+")
    i=i+1
sum=sum+m
print(m,"=",sum)




