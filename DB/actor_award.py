actor = []
awards=[]

with open('actor_award_data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        actor.append(eval(line))

actor = [item[0] for item in actor]
ac=[]
for i in range(len(actor)):
    ac.append((i+1,actor[i]))
actor=ac
# print(actor)

# print(actor[1])
# award=[]

# for i in actor:
#     if i [3] != 0:
#         award.append(i)
#         # if i[3] not in award:
#         #     award.append(i[3])

# print(len(award))

with open('nn_awards.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        awards.append(eval(line))
aw=[]

for i in range(len(awards)):
    aw.append((i+1,awards[i]))

awards=aw


n_award=[]
act_aw=[]
for i in actor:
    check=0
    if i[1][3] !=0:
        for j in awards:
            if i[1][3] ==j[1]:
                act_aw.append((j[0], i[0]))
                check=1
        if check==0:
            num=awards[-1][0]+1
            n_award.append((i[1][3]))
            awards.append((num, i[1][3]))
            act_aw.append((num, i[0]))


with open('actor_award.txt', 'w+', encoding='utf-8') as file:
    for line in act_aw:
        file.write(str(line)+','+'\n')


if len(n_award)!=0:
    with open('new_award.txt', 'a', encoding='utf-8') as file:
        for line in n_award:
            file.write("('"+str(line)+"')"+','+'\n')
    with open('n_awards.txt', 'a', encoding='utf-8') as file:
        for line in n_award:
            file.write("('"+str(line)+"')"+','+'\n')