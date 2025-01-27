# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.

iskl = ['!', '.', ',', '-', '—']

with open('task1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    count_lines = len(lines)
    count_words = 0
    count_simv = 0
    #count_iskl_words = 0

    for line in lines:
        line = ''.join(c for c in line if c not in iskl)
        word = line.split()
        count_words += len(word)
        count_simv += len(line)

    print(lines)
    print('колво строк:', count_lines)
    print('колво слов:', count_words)
    print('колво символов:', count_simv)
