director = []

with open('directors.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        director.append(eval(line))

director = [item[0] for item in director]
d=[]
for i, x in enumerate(director):
    d.append([i+1, x[0]+' '+x[1]])
director=d


movie=[]
with open('data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=list(eval(line))
        movie.append(x)
m=[]
for i in movie:
    for j in director:
        if i[7]==j[1]:
            i[7]=j[0]
    x=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
    m.append(x)


with open('Movie_Data_collect.txt', 'w+', encoding='utf-8') as file:
    for line in m:
        file.write(str(line)+','+'\n')