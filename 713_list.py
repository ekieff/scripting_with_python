squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Yoel',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]

list = open('general_assembly.txt', 'a')
for i in range(len(squad_713)):
    person = squad_713[i]
    if i == 0:
        list.write(f'{person}')
    else:
        list.write(f'\n{person}')
    print(list)
list.close()