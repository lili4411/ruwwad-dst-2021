


# class Employee:
#     def __init__(self,fname,lname,salary=1000):
#      self.fname=fname
#      self.lname=lname
#      self.salary=salary;;;
#     def print_emp(self):
#         print("firstname:"+self.fname+"lastname:"+self.lname+"sal:"+str(self.salary))

# emp1=Employee("hassan","dib",2000)
# #emp1.print_emp()
# emp2=Employee("hassan","ibrahim","1400")
# #emp2.print_emp()

# list1=[]
# list1.append(emp1)
# list1.append(emp2)
# for x in list1:
#     x.print_emp()



    #xxxxxxxxxxxxxxxxxxxxxxxxxxdef create_dic_person(self):
   #return{"name":self.}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx





from _typeshed import Self
class BankAccount:
  def __init__(self,accountNumber,name,balance):
    self.accountNumber=accountNumber
    self.name=name
    self.balance=balance
  def print_acc(self):
   print("numeric type:"+self.accountNumber+"name of the account owner:"+self.name+"balance:"+self.balance)
