# open a file
elaine_file = open('elaine.txt', 'r+')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    elaine_file.write('{}\n'.format(num))
# write to the file
elaine_file.write('Student at GA')
# read a file

# print(elaine_file.read())
# close a file
elaine_file.close()

# if file is not found one will be created for you
# adam_file = open('adam_txt', 'w')
# adam_file.write('Adam is an instructor')
# adam_file.close()

# look up how to read lines from a file in python
read = open('adam_txt')
lines = read.readlines()
for i in range(len(lines)):
    each_item = lines[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    lines[i] = each_item[0:-1]
    print(lines)
print(lines)
read.close()

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

list = open('713_list')

list.close()