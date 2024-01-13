data_list = []

with open('language.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        data_list.append(eval(line))

new_list = [item[0] for item in data_list]

print(len(new_list))
new_list=sorted(list(set(new_list)))
print(len(new_list))

with open('n_language.txt', 'w+', encoding='utf-8') as file:
    for line in new_list:
        file.write("('"+str(line)+"')"+','+'\n')