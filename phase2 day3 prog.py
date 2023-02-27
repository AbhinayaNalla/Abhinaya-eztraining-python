#linked list operations and insertion in ascending order
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        if not temp:
            print('list is empty')
            return
        else:
            print('start:',end=' ')
        while temp:
            print(temp.data, end=' -> ')
            temp=temp.next
        print('end')
    def insert(self,data):
        new_node=node(data)
        #if the linked list is empty
        if self.head is None:
            self.head=new_node
        #if the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            #locate the node before insertion point
            t=self.head
            while t.next and new_node.data > t.next.data:
                t=t.next
            #insertion
            new_node.next=t.next
            t.next=new_node
    def delete(self,key):
        #if the list is empty
        if self.head is None:
            print("deletion error: the list is empty")
            return
        # if the key is in head
        if self.head.data == key:
            self.head=self.head.next
            return
        # find the position of the 1st occurence of the
        t=self.head
        while t:
            if t.data == key:
                break
            previous=t
            t=t.next
        #if the key was  not found
        if t is None:
            print("deletion error: key is not found")
        else:
            previous.next=t.next
# __name is python special variable
if __name__== '__main__':
    #create an obj
    ll=linkedlist()
    print('')
    
    #insert some nodes
    ll.insert(10)
    ll.insert(12)
    ll.insert(7)
    ll.insert(17)
    ll.insert(5)
    ll.printlist()
    
    ll.delete(12)
    ll.delete(7)
    ll.delete(5)
    ll.printlist()'''
#creating own module
'''import fn
fn.printing()
print(__name__)'''
#let say u have lot of functions in ur project
#u can give all  definitions at one place
#and give all function calls inside the main then their will be a format
#easy to read,especially for others
'''print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__== '__main__':
    f1()
    f2()
    f3()
print("name:",__name__)'''
#double linked list
'''class node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class doublelinkedlist:
    def __init__(self):
        self.head=None
    def insert_start(self):
       new_node=node(5)
       temp=self.head
       temp.previous=new_node
       new_node.next=temp
       self.head=new_node
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head #first node
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
obj=doublelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
n1.previous=n
n.next=n1
n2=node(30)
n2.previous=n1
n1.next=n2
print("before inserting")
obj.display()
obj.insert_start()
print("\nafter the inserting")
obj.display()'''

#insertion at start dll
'''def insert_start(self):
    n=node(5)
    temp=self.head
    temp.prev=n
    self.head=n'''
#insertion at position
'''def insert_position(self,pos):
    ne=node(25)
    temp=self.head
    for i in range(1,pos-1):
        temp=temp.next
    ne.previous=temp
    ne.next=temp.next
    temp.next.previous=ne
    temp.next=ne'''
#insertion at end
'''def insert_end(self):
    ne=node(40)
    temp=self.head
    while temp.next is not None:
        temp=temp.next
    temp.next=ne
    ne.previous=temp'''
#delete at beginning
'''def delete_beginning(self):
    temp=self.head
    self.head=temp.next
    temp.next=None'''
#delete at end
'''def delete_end(self):
    temp=self.head.next
    previous=self.head
    while temp.next is not None:
        temp=temp.next
        previous=previous.next
    previous.next=None'''
#delete at position
'''def delete_position(self,pos):
    temp=self.head.next
    previous=self.head
    for i in range(1,pos-1):
        temp=temp.next
        previous=previous.next
    previous.next=temp.next
    temp.next=None'''
#circular linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class createlist:
    def __init__(self):
        self.head=node(None)
        self.tail=node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    #adding node at the end of ll
    def add(self,data):
        newnode=node(data)
        #is empty
        if self.head.data is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            #it is cll so tail will point to head
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("list is empty")
            return
        else:
            print("nodes of the cll :")
            print(current.data, "-->")
class circularlinkedlist:
    c1=createlist()
    c1.add("s")
    c1.add("m")
    c1.add("i")
    c1.add("l")
    c1.add("e")
    c1.display()
    
