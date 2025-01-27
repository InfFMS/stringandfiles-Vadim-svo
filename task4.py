# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.



sentences = []
for i in range(5):
    sentence = input()
    sentences.append(sentence)


with open("new_predl4.txt", "w", encoding="utf-8") as f:
    for sentence in sentences:
        new_predl = "_".join(word.upper() for word in sentence.split())
        f.write(new_predl + "\n")


with open("new_predl4.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


