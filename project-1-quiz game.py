q1='''who is  the most familiar cricketer in indian team
a.sachin
b.sehwag
c.dhoni
d.virat'''
q2='''who is  the first pm of india
a.nehru
b.gandhi
c.subhash
d.patel'''
q3=''' who is most popular in insta
a.virat
b.modi
c.ronaldo
d.rohit'''
q4=''' what the capital of andhra pradesh
a.amaravati
b.hyderabad
c.vizag
d.none of the above'''
q5=''' which film received the golden globe 2023 award
a.rrr
b.vikram
c.akanda
d.18 pages'''
questions={q1:"b",q2:"a",q3:"a",q4:"d",q5:"a"}
name=input("hi what is your name :")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do u want to skip this ques (yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter ur answer")
    if ans==questions[i]:
        print("wow u got one point")
        score=score+1
        print("ur current score is:",score)
    else:
        print("wrong answer ,u lost 1 mark")
        score=score-1
        print("ur current score is:",score)
    flag2=input("do u want to quit? type (yes/no)")
    if flag2=="yes":
        break
print("ur total score is :",score)
        
