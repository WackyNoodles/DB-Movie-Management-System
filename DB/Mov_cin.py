data_list=[]
with open('movie_cinema.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        data_list.append(eval(line))

new_list = [item[0] for item in data_list]


u=[]
for i in new_list:
    if i[1] not in u:
        u.append(i[1])

print(len(u))