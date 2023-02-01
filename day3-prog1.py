"""
1* create a list with 10 items  print the ele one by one
2* create a list with  5 float  num find and display sum and avg of list
3* after creating alist with 6 ele from the user extract only even num and print
1*
l=[3,8,9,5]
for i in range(len(l)):
    print(l[i])

# using membership operator also
l=[3,4,78,9]
for j in l:
    print(j)
    print(l[j])
2*
l=[2.4,6.2,8.4,6.4,5.6]
summ=0
for i in range(len(l)):
    summ = summ+l[i]
    avg =summ/len(l)
print(summ, avg)

3*
size=int(input("size:"))
l=[]
for i in range(size):
    ele=int(input("element:"))
    l.append(ele)
print(l)
for j in l:
    if(j%2==0):
        print(j)
"""
'''4* get the nos as input , return the product if the product less than 750
else return sum'''
#jst tried
'''
size=int(input("size:"))
l=[]
for i in range(size):
    ele=int(input("element:"))
    l.append(ele)
print(l)
product=1
summ=0
for j in l:
    product(l) == product*l(i)
    if (product(l)<750):
        (product(l))
    else:
        print(summ==summ+l[i])'''
'''
n=list(map(int,input("enter").split()))
print(n)
x=1
y=0
for i in n:
    x=x*i
    y=y+i
if x<=750:
    print("prod",x)
else:
    print("sum",y)'''
'''numbers=[elements for elements in "good afternoon"]
print(numbers)'''
'''l=["rjy","araku","hyd","amirpeet"]
city=[]
for n in l:
    if "a" in n:
        city.append(n)
print(city)'''
'''l=[2**x for x in range(2,10)]
print(l)'''
'''l=[a for a in range(100,201,20)]
print(l)'''
'''L=[1,2,3,4,5,6]
L2=[i for i in L if (i<5)]
print(L2)'''
s1={1,2,34}
s2={1,4,54}
print(s1.symmetric_difference(s2))




