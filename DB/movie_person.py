import random
import numpy


persons = []

with open('nn_persons.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        persons.append(eval(line))

persons = [item[0] for item in persons]

p=[]
for i in persons:
    p.append(list(i))
# print(p)
persons=p


movie=[]
with open('result.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=list(eval(line))
        movie.append(x)


def choice():
    x = numpy.random.choice(numpy.arange(1, 11), p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05])
    return x
def day():
    x=random.randint(1, 28)
    return x

def month():
    x=random.randint(1, 12)
    return x

def year(n):
    x=random.randint(n, 2023)
    return x

def ind(n):
    x=random.randint(0, n-1)
    return x

def rat(x,y):
    r=random.uniform(x,y)
    r=round(r,1)
    return r

for i in movie:
    x=choice()
    i.append(x)
    i.append(0)

for i in persons:
    x=choice()
    i.append(x)
    i.append(0)


mov_rat=[]
mov_pur=[]
check=[]
for x, i in enumerate(movie):
    while i[9] != i[10]:
        cin=ind(len(persons))
        c=persons[cin]
        data=(c[0], i[0])
        if data not in check:
            check.append(data)


            y1=persons[cin][5]+13
            y2=i[2]
            if y1>y2:
                y=y1
            else:
                y=y2
            ye=year(y)
            date=str(ye)+'-'+str(month())+'-'+str(day())
            mov_pur.append((i[0], c[0], date))


            r1=i[3]
            r2=r1-1.5
            if r2<0:
                r2=0
            r3=r1+1.5
            if r3>10.0:
                r3=10
            r=rat(r2, r3)

            mov_rat.append((i[0], c[0], r))



            persons[cin][7]=persons[cin][7]+1
            i[10]=i[10]+1

            if persons[cin][6]==persons[cin][7]:
                persons.remove(c)


print(len(mov_rat))
print(len(mov_pur))


with open('movie_purchase.txt', 'w+', encoding='utf-8') as file:
    for line in mov_pur:
        file.write(str(line)+','+'\n')

with open('movie_rating.txt', 'w+', encoding='utf-8') as file:
    for line in mov_rat:
        file.write(str(line)+','+'\n')