#dict comprehension
'''d={n:n*n for n in range(2,6)}
print(d)

old={"rice":50,"oil":90,"sugar":120}
new={product:price*5 for (product,price) in old.items()}
print(new)'''

'''real={"ali":20,"ajith":15,"abhi":25}
now={name:age for (name,age)in real.items() if age>20}
print(now)'''

'''create a list with 8 customers names display a dict which has customers
names along with discounts for them from a particular shop'''

'''import random
lst=['avi','raj','ram','abhi','ashi','sam','nitya','sahiti']
d={names:random.randint(1,100) for names in lst}
print(d)

l1=['a','b','c']
l2=[1,2,3]
d={a:b for (a,b) in zip(l1,l2)}
print(d)

stu=['abhi','nani','vinnu','akhi','vinni']
marks=[86,76,85,95,73]
n=150
d={a:(b/n)*100 for (a,b) in zip(stu,marks)}
print(d)'''
'''import random
stu_names=list(map(str,input("enter names:").split()))
marks=[]
for i in range(len(stu_names)):
    a = (random.randint(300,500)/500)*100
    marks.append(a)

di={a:b for (a,b) in zip(stu_names,marks)}
print(di



x="hi i'am "abhi""
#it throws error so use opposite opposite
x="hi i'am"
print(x)
or use back ward slash "hi i\am'abhi'"

print('a'>'b)
get one string  as input along with a charachter
find out and display whether that particular char is present or not
check whetherc the given string as palindrome or not
after getting one string as input check ur string contains spaces or not
if yes print the no of spaces in it
st=input("enter a str:")
char =input("enter a char:")
if char in st:
    print("character is present")
else:
    print("char is not present")
st=input("enter a str:")
char =input("enter a char:")
for i in st:
    if i==char:
        flag=1
    else:
        flag=0
if flag==1:
    print('present')
else:
    print('not present')
st=input("enter a string:")
space=" "
if space in st:
    print("space is their")
else:
    print("spaces are not thier")
st=input("enter a string:")
n=0
for i in st:
    if i==" ":
        n+=1
print(n)
create a list with vowels get one string as input count vowels from the string
l=['a','e','i','o','u' 'A','E','I','O','U']
st=input("enter a string:")
n=0
for i in st:
     if i in l:
         n+=1
print(n)'''
#math module
import math
print("ceil 25.6 :",math.ceil(25.6))
print("floor 25.6 :",math.floor(25.6))
print("sqrt 5 :",math.sqrt(5))
print("factorial 6 :",math.factorial(6))
print("power (5,2) :",math.pow(5,2))
print("remainder 25,6 :",math.fmod(25,6))
a,b=divmod(5,3)
print(a,b)

        





