# students=["tahani","manaser","jinan","rana","rima"]

# grades=[20,80,70,80,90]

# for i in range (len(students)):
#     print(students[i]+"\t",grades[i])



# students_count=input("how many students are these in the class?\n")
# while(not students_count.isdigit()) : students_count=input("please enter a valid positive numbfruita

# fruits=["banana","strawberry","wtermelon","apple"]
# newlist=["hello"for x in fruits]
# print(newlist)
# newlist1=[x if x !="banana" else "orange" for x in fruits]
# print(newlist1)

a=[1,2,3,4,5]
b=[10,9,8,7,5]
c=[]

for i in range (5):
    sum=a[i]+b[-i-1]
    c.append(sum)
print(c)