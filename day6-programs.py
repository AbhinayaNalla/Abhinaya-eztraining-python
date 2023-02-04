# exception handling
'''a=20
b=0
try:
    print(a/b)
except Exception as e:
    print("num can't divided by zero",e)
finally:
    print("end")'''

'''a=10
try:
    b=int(input("enter the input : "))
    print(a/b)
except ZeroDivisionError as e:
    print("can't be divisible",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error",e)
finally:
    print("end")'''

# raise
'''x=10
if x%2!=0:
    raise Exception (" x should be even num")
else:
    print("x is even num")'''
#oops
'''class computer:
    def config(self):
        print("yes")
asus=computer()#obj1
asus.config()

lenovo=computer() #obj2
lenovo.config()'''
#constructor
'''class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("name:%s\n ID:%d" %(self.name,self.id))
emp1=Employee("abhi",17)
emp2=Employee("sasu",12)
emp1.display()
emp2.display()'''

# variable accesing
class computer():
    a=10
    b=20
    print("class variable inside the clss",a)
    def config(self):
        c=100
        print("yes")
        print("instanceor clss variable access inside the fun",self.b)
asus=computer()
print(asus.a)
print(asus.a+asus.b)
asus.config()
lenovo=computer()
print("lenovo",lenovo.a)
lenovo.config()

        

