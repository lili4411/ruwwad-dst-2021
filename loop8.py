
even=0
odd=0
i=0
while(i<5):
    n=int(input("enter your numbers"))
    i=i+1
    print(i)
    if(n%2==0):
         even=even+1
    else:
         odd=odd+1

print("the even numbers is:",even)
print("the odd numbers is:",odd)