#Welcome menu
print('HTML Converter')
print()
#Opens file and reads lines
myfile = open('p9-1_groceries.html')
lines = myfile.readlines()
#replaces all the lines
for line in lines:
    lines= line.replace('h1', ' ').strip().replace('<', ' ').replace('>', ' ').replace('/', ' ').replace('ul', ' ').replace('li', '').strip().replace('Eggs', '* Eggs ').strip().replace('Milk', '* Milk ').replace('Butter', '* Butter ')
    print(lines)








