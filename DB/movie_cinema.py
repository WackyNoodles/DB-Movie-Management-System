import random
import numpy

cinema=[]
with open('n_cinema.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        cinema.append(eval(line))

cinema = [item[0] for item in cinema]
c=[]
for i, x in enumerate(cinema):
    c.append([i+1,x[0], x[1], x[2], x[3]])
cinema=c

movie=[]
with open('result.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=list(eval(line))
        movie.append(x)





def day():
    x=random.randint(1, 28)
    return x

def month():
    x=random.randint(1, 12)
    return x

def ind(n):
    x=random.randint(0, n-1)
    return x

def choice():
    x = numpy.random.choice(numpy.arange(1, 4), p=[0.75, 0.175, 0.075])
    return x



for i in movie:
    x=choice()
    i.append(x)
    i.append(0)

for i in cinema:
    x=choice()
    i.append(x)
    i.append(0)


mov_cin=[]
for x, i in enumerate(movie):
    while i[9] != i[10]:
        cin=ind(len(cinema))
        c=cinema[cin]
        data=(c[0], i[0])
        if data not in mov_cin:
            date=str(i[2])+'-'+str(month())+'-'+str(day())
            mov_cin.append((c[0], i[0], date))
            cinema[cin][6]=cinema[cin][6]+1
            i[10]=i[10]+1
            if cinema[cin][5]==cinema[cin][6]:
                cinema.remove(c)


print(len(mov_cin))

with open('movie_cinema.txt', 'w+', encoding='utf-8') as file:
    for line in mov_cin:
        file.write(str(line)+','+'\n')
