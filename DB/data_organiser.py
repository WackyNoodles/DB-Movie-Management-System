count=1
language = []
genre = []
production=[]
movie=[]
actor=[]
m_actor=[]


with open('n_production.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        production.append(eval(line))

pro=[]

for i in range(len(production)):
    pro.append((i+1,production[i]))

production=pro

with open('n_language.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        language.append(eval(line))
lan=[]


for i in range(len(language)):
    lan.append((i+1,language[i]))

language=lan


with open('n_genre.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        genre.append(eval(line))
ge=[]

for i in range(len(genre)):
    ge.append((i+1,genre[i]))

genre=ge

ac=[]
with open('nnn_actors.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        ac.append(eval(line))


a_count=len(ac)+1

for i in range(len(ac)):
    actor.append((i+1,ac[i]))


# um=[]
# r=[]
# for i in ac:
#     x=i[0]+ ' '+ i[1]
#     if x not in um:
#         um.append (x)
#     else:
#         r.append(i)
# print(len(um))
# print(r)
# print(len(ac))


with open('movie_actor.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        m_actor.append(eval(line))


with open('Movie_Data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=list(eval(line))
        movie.append(x)
um=[]
r=[]
unique=['Little Women', 'Elephant' ,'Home' ]
for i in movie:
    if i[1] not in um:
        um.append (i[1])
    elif i[1] in unique:
        pass
    else:
        if i[1] not in r:
            r.append(i[1])
# print(len(um))

# print(r)

# u=[]
# for i in movie:
#     x=(i[7])
#     if x not in u:
#         u.append(x)

# print(len(u))

mov=[]
n_genre=[]
n_production=[]
n_language=[]
n_actor=[]
nm_actor=[]
for i in movie:
    a_check=0
    i[0]=count
    for j in language:
        if i[5] == j[1]:
            i[5]=j[0]
            break
    if type (i[5])==str:
        num=language[-1][0]
        language.append((num, i[5]))
        n_language.append((i[5]))
        i[5]=num

    for j in genre:
        if i[6] == j[1]:
            i[6]=j[0]+1
            break
    if type (i[6])==str:
        num=genre[-1][0]
        genre.append((num, i[6]))
        n_genre.append((i[6]))
        i[6]=num

    for j in production:
        if i[8] == j[1]:
            i[8]=j[0]
            break
    if type (i[8])==str:
        num=production[-1][0]+1
        production.append((num, i[8]))
        n_production.append((i[8]))
        i[8]=num
    data=0
    for j in actor:
        x=j[1][0]+ ' ' + j[1][1]
        y=i[9] +' '+ i[10]
        if x==y:
            a_check=1
            data=j[0]
            break
    if a_check==0:
        a=(i[9], i[10], i[11])
        actor.append((a_count, a))
        n_actor.append(a)
        data=a_count
        a_count+=1


    m_ac=(data, count)
    if m_ac not in m_actor:
        m_actor.append(m_ac)
        nm_actor.append(m_ac)
    count+=1



    mov.append((i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))




with open('result.txt', 'w+', encoding='utf-8') as file:
    for line in mov:
        file.write(str(line)+','+'\n')

if len(n_genre)!=0:
    with open('new_genre.txt', 'a', encoding='utf-8') as file:
        for line in n_genre:
            file.write("('"+str(line)+"')"+','+'\n')
    with open('n_genre.txt', 'a', encoding='utf-8') as file:
        for line in n_genre:
            file.write("('"+str(line)+"')"+','+'\n')

if len(n_language)!=0:
    with open('new_language.txt', 'a', encoding='utf-8') as file:
        for line in n_language:
            file.write("('"+str(line)+"')"+','+'\n')
    with open('n_language.txt', 'a', encoding='utf-8') as file:
        for line in n_language:
            file.write("('"+str(line)+"')"+','+'\n')

if len(n_production)!=0:
    with open('new_production.txt', 'a', encoding='utf-8') as file:
        for line in n_production:
            file.write("('"+str(line)+"')"+','+'\n')
    with open('n_production.txt', 'a', encoding='utf-8') as file:
        for line in n_production:
            file.write("('"+str(line)+"')"+','+'\n')

if len(n_actor)!=0:
    with open('new_actor.txt', 'a', encoding='utf-8') as file:
        for line in n_actor:
            file.write(str(line)+','+'\n')
    with open('n_actor.txt', 'a', encoding='utf-8') as file:
        for line in n_actor:
            file.write(str(line)+','+'\n')
    
if len(nm_actor)!=0:
    with open('movie_actor.txt', 'w+', encoding='utf-8') as file:
        for line in nm_actor:
            file.write(str(line)+','+'\n')
