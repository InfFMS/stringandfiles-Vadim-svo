# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
from collections import Counter
import re

words = []
with open('task3.txt', 'r', encoding='utf-8') as f:
    line = f.read()
    line = re.sub(r'[.,]', '', str(line))
    linelow = line.lower()
    words = linelow.split()
res = words.sort()

word_counts = Counter(words)


words_list = list(word_counts.keys())
counts_list = list(word_counts.values())


print(words_list)
print(counts_list)

sorted_word_counts = sorted(word_counts.items())

with open('newer_file3.txt', 'w', encoding='utf-8') as newer_file:
    for word, count in sorted_word_counts:
        newer_file.write(f"{word}: {count}\n")
