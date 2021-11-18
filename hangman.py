print("welcome to hangman!")
name={'France', 'Spain', 'Lebanon', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany'}
name="waleed"
list1=["*","*","*","*","*","*"]
i=0
a=0
while a<6:
    b=input("enter a letter:")
    if b in name:
        print("correct")
        i=i+1
        w=int(name.index(str(b)))
        list1[w]=b
        print(list1)
        name.remove(str(b))
        if i==len(name):
            print("you win")
    else:
        print("incorrect")
        a=a+1    
else:
    print("game over")

