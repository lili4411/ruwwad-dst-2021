n=int(input("enter the first number:"))
m=int(input("enter the last number"))
s=0
print("the sum of",end="")
for a in range (n,m+1):
    s=s+a
    print(a,"+",end="")
print("=",s)

