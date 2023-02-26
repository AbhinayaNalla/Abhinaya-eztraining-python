#encaps protected
'''class encap:
  _a=10
  c=20
  def encapfunction(self):
    _b=20
    print("encap accessing protected")
    print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)'''
#private
'''class encap:
  __a=10
  print(__a)
  def encapfunction(self):
    print("encap function")
    print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)'''
#method overloading
'''class moverloading:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverloading()
print("without arguments")
obj.display()
print("with arguments")
obj.display(10,20)
print("with one arguments")
obj.display(10)'''
#polymorphism
'''class rjy:
    def placename(self):
        print("rjy place name is humkumpeta")
    def student(self):
        print("yes rjy")
    def year(self):
        print("3rd")
class kkd:
    def placename(self):
        print("kkd place name is  surampalem")
    def student(self):
        print("yes kkd")
    def year(self):
        print("3rd")
obj_rjy=rjy()
obj_kkd=kkd()
for details in (obj_rjy,obj_kkd):
    details.placename()
    details.student()
    details.year()'''
# linked list
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #first node
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()'''
#example
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #first node
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node("w")
obj.head=n
n1=node("i")
obj.head.next=n1
n2=node("n")
n1.next=n2
n3=node("n")
n2.next=n3
n4=node("e")
n3.next=n4
n5=node("r")
n4.next=n5
obj.display()'''
# insertion at beginning
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #first node
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
print("before inserting")
obj.display()
obj.insert_beginning(50)
print("\nafter the inserting")
obj.display()'''
#inserting at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        ne=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #first node
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
print("before inserting")
obj.display()
obj.insert_end(50)
print("\nafter the inserting")
obj.display()'''
#insert at desired position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #first node
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
print("before inserting")
obj.display()
obj.insert_position(3,50)
print("\nafter the inserting")
obj.display()'''
#single linked list creation using user input
class Node:
    def _init_(self,data):
        self.data = data
        self.next= None
class LinkedList:
    def _init_(self):
        self.head = None
        self.last_node = None
    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
a_llist = LinkedList()
n = int(input('how many elements would you like to enter:'))
for i in range(n):
    data = int(input("enter data item:"))
    a_llist.append(data)
print('the linked list:',end = ' ')
a_llist.display()



    
