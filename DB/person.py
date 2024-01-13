import random
from datetime import datetime

data_list = []

with open('persons_data.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        data_list.append(eval(line))

new_list = [item[0] for item in data_list]

print(len(new_list))
new_list=sorted(list(set(new_list)))

print(len(new_list))



def day():
    x=random.randint(1, 28)
    return x

def month():
    x=random.randint(1, 12)
    return x

def year():
    x=random.randint(1940, 2010)
    return x

def age(dob):
    birthdate = datetime.strptime(dob, '%Y-%m-%d')
    now = datetime.now()
    ag = now.year - birthdate.year - ((now.month, now.day) < (birthdate.month, birthdate.day))
    return ag

a=[]
ua=[]
for x, i in enumerate(new_list):
    if i[0] !=i[1]:
        if i not in a:
            y=year()
            date=str(y)+'-'+str(month())+'-'+str(day())
            o=age(date)
            a.append((i[0], i[1], date, o))
            ua.append((x+1, i[0], i[1], date, o, y))

new_list=a
print(len(new_list))

with open('n_persons.txt', 'w+', encoding='utf-8') as file:
    for line in new_list:
        file.write(str(line)+','+'\n')

with open('nn_persons.txt', 'w+', encoding='utf-8') as file:
    for line in ua:
        file.write(str(line)+','+'\n')