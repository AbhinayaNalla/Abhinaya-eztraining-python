'''import random as r
x=" i love the good fragnances"
print(r.sample(x,3))'''

'''a=[10, 20,48,67,93,]
r.shuffle(a)
print(a)

print(r.choice(a))

b="welcome home"
print(r.choice(b))

a=r.random()
print(a) #0.0 includes and 1.0 excludes
print(r.randint(40,50))

a=[10,20,40,30]
print(r.choices(a,k=10))

b="hi hello "
print(r.choices(b,k=4)
b="hi hello "
print(r.uniform(6,9))#selects flat value

a=[10,20,40,30]
print(r.choices(a,v=10))

z=dir(r)
print(z) # to find all functions '''

'''import calendar
print("full calender")
print(calendar.calendar(2022))
print("particular month")
print(calendar.month(2021,4))
print("set the first day of tne week")
calendar.setfirstweekday(calendar.TUESDAY)
print(calendar.month(2021,4))'''

'''import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
fv=a.strftime("%Y")
print("short yeasr version",sv)
print("long year version",fv)'''
# without arg and return val
'''def sample():
    print("hi")
    print("hello")
sample()
print("ho")
sample()
def multi():
    x,y,z=int(input("enter x:")),int(input("enter y:")),int(input("enter z:"))
    prod=x*y*z
    print(prod)
multi()'''
# without arg with return values
'''def multi():
    x,y,z=int(input("enter x:")),int(input("enter y:")),int(input("enter z:"))
    prod=x*y*z
    return prod
res=multi()
print(res)'''
#with arg without return val
'''def multi(x,y,z):
    prod=x*y*z
    print(prod)
multi(4,5,6)'''

'''def multi1(x,y,z):
    prod=x*y*z
    print(prod)
x,y,z=int(input("enter x:")),int(input("enter y:")),int(input("enter z:"))
multi1(x,y,z)'''

#with arg and return val
'''def multi(x,y,z):
    prod=x*y*z
    return prod
res=multi(4,2,6)
print(res)'''

'''def multi1(x,y,z):
    prod=x*y*z
    return prod
x,y,z=int(input("enter x:")),int(input("enter y:")),int(input("enter z:"))
res1=multi1(x,y,z)
print(res1)'''

# lemons using fun 1
# find factors of the given num using fun 2
# print mul table of the given num using fun type 3
# find sum of the  digits of given num using fun type 4


'''def funtion1():
    num=int(input("enter a num:"))
    for i in range (1,num+1):
        if num%i==0:
            print(i)
funtion1()'''


'''n=6
for i in range(1,11):
    print(i,"x",n,l"=",i*n)'''

'''def lemons():
    n1,n2,n3=int(input("enter n1:")),int(input("enter n2:")),int(input("enter n3:"))
    s=n1+n2+n3
    print(s)
    if (s>21):
        print("the num exceeds",s-21)
    elif(s<21):
        print("the num includes",21-s)
    else:
        print("the num is 21")
lemons()'''

'''def sumofdigits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter the num:"))
res=sumofdigits(n)
print(res)'''

# recursion
'''def display():
    n=int(input("enter the num:"))
    if n==1:
        display()
    else:
        print("over")
display()'''

'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
res=fact(6)
print(res)'''
# fabonaci series  try it with function
'''n=int(input("enter thr number:"))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum, end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b'''

# variable length method
def summ(*a):
    c=0
    for i in a:
        c=c+1
    print(c)
summ(10,2,3,1,2)




















