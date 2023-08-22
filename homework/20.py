# with open('hw.txt', 'w') as hw:
#     hw.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')

# Обмен местами 2-ух строк

# with open('hw.txt', 'r') as hw:
#     pos1 = int(input('-> '))
#     pos2 = int(input('-> '))
#     read_file = hw.readlines()
#     print(read_file)
#     read_file[pos1], read_file[pos2] = read_file[pos2], read_file[pos1]
#     print(read_file)

# Реверсирование строк

# with open('hw.txt', 'r') as hw:
#     read_file = '\n'.join(reversed(hw.readlines()))
#     print(read_file)

# Объединение 2-ух файлов в 3-ий

# with open('file1.txt', 'w') as f1:
#     f1.write('Первый файл.')
#
# with open('file2.txt', 'w') as f2:
#     f2.write('Второй файл.')

file1 = 'file1.txt'
file2 = 'file2.txt'

with open(file1, 'r') as f1, open(file2, 'r') as f2, open('file3.txt', 'w') as f3:
    f3.write(f1.read() + f2.read())









