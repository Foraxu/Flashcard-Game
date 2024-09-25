with open('en_300.txt' , 'r') as file:
    content = file.readlines()
    
line_list = []

for line in content:
    for i in line:
        if i == ' ':
            pass
        elif i == '\n':
            line_list.append(i)
        else:
            try:
                int(i)
            except ValueError:
                line_list.append(i)

print(line_list)
formated_content = ''.join(line_list)

with open('en_300_formated.txt', 'w') as file:
    file.write(formated_content)
