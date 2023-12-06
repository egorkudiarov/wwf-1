def count_lines(name):
    file_path = f'3\{name}'
    with open(file_path, 'r', encoding='UTF-8') as f:
        count = len(list(f.readlines()))
        return [name, count]
    
def rearrange(files):
    file_list = []
    for file_name in files:
        file_list.append(count_lines(file_name))
    file_list.sort(key=lambda x: x[1])
    with open('3\result.txt', 'w', encoding='UTF-8') as f:
        for file_name in file_list:
            f.write(f'{file_name[0]}\n')
            f.write(f'{str(file_name[1])}\n')
            with open(f'3\{file_name[0]}', 'r', encoding='UTF-8') as t:
                for line in t.readlines():
                    f.write(line)
                f.write('\n')

files = ['1.txt', '2.txt', '3.txt']
rearrange(files)
print('1')