data_list = []

with open('production.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().rstrip(',;')
        data_list.append(eval(line))

print(len(data_list))
production=[]
for i in data_list:
    production.append(i[1])
production=list(set(production))
print(len(production))

with open('n_production.txt', 'w+', encoding='utf-8') as file:
    for line in production:
        file.write("('"+str(line)+"')"+','+'\n')