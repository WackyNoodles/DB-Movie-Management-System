data=[]
with open('actor_award.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=eval(line)
        data.append(x)

a_g=[]
with open('actor_gender.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        x=list(eval(line))
        a_g.append(x)

a_gg=[]
for i, x in enumerate (a_g):
    a_gg.append([i+1, x[0], x[1], x[2] ])

a_g=a_gg