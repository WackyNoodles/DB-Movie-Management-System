data_list = []

with open('actor.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        data_list.append(eval(line))

new_list = [item[0] for item in data_list]

print(len(new_list))
new_list=list(set(new_list))

print(len(new_list))

ua=[]
a=[]

for i in new_list:
    x=i[0]+ ' '+ i[1]
    if x not in ua:
        ua.append (x)
        a.append(i)

new_list=a
print(len(new_list))

with open('n_actor.txt', 'w+', encoding='utf-8') as file:
    for line in new_list:
        file.write(str(line)+','+'\n')