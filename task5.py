# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

with open("task5.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()

longest_word = ""
max_length = 0

for word in words:
    word_length = len(word)
    if word_length > max_length:
        max_length = word_length
        longest_word = word

long = (f"Самое длинное слово: {longest_word} \nЕго длина: {max_length}")

with open("result5.txt", "w", encoding="utf-8") as g:
    g.write(long)

print(longest_word)
print(max_length)




