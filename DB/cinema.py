data_list = []

with open('cinema.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        data_list.append(eval(line))

new_list = [item[0] for item in data_list]

print(len(new_list))
new_list=sorted(list(set(new_list)))
print(len(new_list))

u=[]
y=[]
for i in new_list:
    a=i[3]
    b=a.split(',')    
    b[1]=b[1].lstrip(" ")
    if b[0]==b[1]:
        pass
    else:
        x=(i[0], b[0])
        if x not in u:
            u.append(x)
            y.append(i)

new_list=y
print(len(new_list))

with open('nn_cinema.txt', 'w+', encoding='utf-8') as file:
    for line in range (len(new_list)):
        file.write(str(line+1)+' '+str(new_list[line][0])+ ' '+str(new_list[line][1])+'\n')

with open('n_cinema.txt', 'w+', encoding='utf-8') as file:
    for line in new_list:
            file.write(str(line)+ ','+'\n')