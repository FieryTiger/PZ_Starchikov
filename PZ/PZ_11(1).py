"""Из предложенного текстового файла (text18-26.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно заменив все знаки пунктуации на знак «/»."""
f1 = open('text18-26.txt', 'r', encoding='utf-16')
file = f1.read()
f1.close()
symbols = []
for i in file:  # Цикл перебирает каждый символ содержимого и добваляет в список нужные
    if i in [':', '—', '.']:
        symbols.append(i)
print("Содержимое файла: ", '\n', file)
print('\n', "Количество знаков препинания:", len(symbols), '\n')

new_file = file.replace(':', '/').replace('.', '/').replace('—', '/')  # Замена символов
f2 = open('new_file.txt', 'w', encoding='utf-8')
f2.write(new_file)
f2.close()

f2 = open('new_file.txt', 'r', encoding='utf-8')
print(f2.read())
f2.close()

