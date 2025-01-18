# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
new_text = ''
c = 0
with open('task2.txt', 'r', encoding='utf-8') as f:
    line = f.read()

    word = line.split(' ')
    for i in range(len(word)):
        if word[i] == 'Python':
            word[i] = 'Питон'
            c += 1
        if word[i] == '\nPython':
            word[i] = '\nПитон'
            c += 1
        new_text += word[i] + ' '

    print(new_text)
    print(c)

with open('new_file.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_text)