E={'java','python','javascript','c++','c#'}
F={'vb.et','java','koltin','python'}
Waleed=[]
def inter(E,F):
    for i in E:
        for j in F:
            if i==j:
                Waleed.append(i)
inter(E,F)
Waleed1=set(Waleed)
print(Waleed1)           
            
