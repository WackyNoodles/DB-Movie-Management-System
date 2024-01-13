# import random
# import numpy

# def choice():
#     x = numpy.random.choice(numpy.arange(1, 5), p=[0.125, 0.25, 0.5, 0.125])
#     return x

# def cho():
#     x = numpy.random.choice(numpy.arange(1, 4), p=[0.75, 0.175, 0.075])
#     return x

# def ind(n):
#     x=random.randint(0, n-1)
#     return x

# awards = []

# with open('nn_awards.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         line = line.strip()
#         awards.append(eval(line))

# awards = [item[0] for item in awards]

# a=[]
# f_aw=[]
# m_aw=[]
# for i, x in enumerate(awards):
#     if ('Actress' in x) or ('actress' in x):
#         v='f'
#         f_aw.append([i+1, x, v])
#     else:
#         v='m'
#         m_aw.append([i+1, x, v])

# awards=a


# a_g=[]
# with open('actor_gender.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         line = line.strip().rstrip(',;')
#         x=list(eval(line))
#         a_g.append(x)

# a_gg=[]
# for i, x in enumerate (a_g):
#     a_gg.append([i+1, x[0], x[1], x[2] ])

# a_g=a_gg

data=[]
with open('actor_award1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=eval(line)
        data.append(x)

d=[]
for i in data:
    if i[0] not in d:
        d.append(i[0])

print(len(d))

# print(data)
# d=[]
# for i in data:
#     if i[0] not in d:
#         d.append(i[0])


# for i in f_aw:
#     if i[0] in d:
#         f_aw.remove(i)

# for i in m_aw:
#     if i[0] in d:
#         m_aw.remove(i)








# for i in a_g:
#     x=cho()
#     i.append(x)
#     i.append(0)


# for i in m_aw:
#     x=choice()
#     i.append(x)
#     i.append(0)

# for i in f_aw:
#     x=choice()
#     i.append(x)
#     i.append(0)


#f_aw for female awards
#m_aw for male awards
#data for previous combinations
#a_g for actor list
#a_g[4] for count
#m_aw[3] for count, [4] for counter
    

# result=[]
# for x, i in enumerate(a_g):
#     while i[4] != i[5]:
#         cin=ind(len(m_aw))
#         c=m_aw[cin]
#         da=(c[0], i[0])
#         if da not in data:
#             result.append((c[0], i[0]))
#             m_aw[cin][4]=m_aw[cin][4]+1
#             i[5]=i[5]+1
#             if m_aw[cin][3]==m_aw[cin][4]:
#                 m_aw.remove(c)


# with open('actor_award1.txt', 'w+', encoding='utf-8') as file:
#     for line in result:
#         file.write(str(line)+','+'\n')