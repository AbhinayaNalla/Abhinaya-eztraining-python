#anonymous function
'''l=[1,2,3]
r=map(lambda x:x+1,l)
print(list(r))
res=map(lambda n:pow(n,2),l)
print(list(res))
name='abhi'
(lambda name:print(name)) (name)'''
# write a program after creating a list with even num with in the range 1 to 15 now apply lambda fun and create a new list which should have sqrts of the elements
'''import math
l=[2,4,6,8,10,12,14]
r=map(lambda x:math.sqrt(x),l)
print(list(r))'''
#abstraction
'''class abstractdemo(ABC):
    @abstractmethod #called decorator to make the method abstact one
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
#changing abtract to concrete
class demo(abstractdemo):
    def display(self):
        print("abstraction method")
    def show(self):
        print("show")
obj=demo()
obj.display()
obj.show()'''
#inheritence
'''class parent:
    def display(self):
        print("parent")
class child(parent):
    def show(self):
        print("show")
obj=child()
obj.display()
obj.show()'''
#example program
'''class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
obj=B()
obj.calc()'''
#multiple inheritence
'''class dad:
    def display(self):
        print("disp")
class mom:
    def show(self):
        print("shown")
class child(dad,mom):
    def ask(self):
        print("asken")
obj=child()
obj.display()
obj.show()
obj.ask()'''
#multilevel inheritence
'''class grandpa:
    def display(self):
        print("iam biggest of family")
class father(grandpa):
    def show(self):
        print("middle man of family")
class son(father):
    def ask(self):
        print("asken")
obj=son()
obj.display()
obj.show()
obj.ask()'''
# Hierarchical inheritance
'''class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()'''
# hybrid inheritance
'''class School:
	def func1(self):
		print("This function is in school.")
class Student1(School):
	def func2(self):
		print("This function is in student 1. ")
class Student2(School):
	def func3(self):
		print("This function is in student 2.")
class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")
obj= Student3()
obj.func1()
obj.func2()'''
#happy number program
'''def happy(n):
  s=r=0
  while(n>=0):
    for i in range(0,len(str(n))+1):
        r=n%10
        s=s+r**2
        n=n//10
    return s
n=int(input("enter the number :"))
res=n
while(res!=1 and res!=4):
  res=happy(res)
if res==1:
    print("happy number")
else:
    print("not a happy num")'''
'''Short_list =[5,7,3,2,8,1,0,10,9,4,6]
def sort_list(my_list):
  even_list = []
  odd_list = []
  for i in my_list:
      if i % 2 == 0:
          even_list.append(i)
      else:
          odd_list.append(i)
  even_list.sort(),odd_list.sort()
  even_list.extend(odd_list)
  return even_list

print(sort_list(Short_list))'''









