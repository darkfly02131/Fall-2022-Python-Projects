#Opens file
with open('pig_dice_rules.txt') as file:
    pig = file.read()
    print(pig)
    

#reads the rules
def read_rules():
    rules= []
    with open('pig_dice_rules.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            rules.append(line)

    for rule in rules:
        print(rule)
        


def main():
    rules = read_rules()
    


if __name__ == '__main__':
    main()
