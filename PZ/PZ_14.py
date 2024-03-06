"""В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
Достоевского (т.е. с различными окончаниями, например, Достоевский,
Достоевского) в единственном экземпляре."""
import re
f1 = open('Dostoevsky.txt', 'r', encoding='utf-8')
file = f1.read()
ends = re.findall(r'\bДостоевск[а-яё]+\b', file)   # Поиск совпадений в файле
ready = list(set(ends))   # Исключение совпдений
f1.close()
print(ready)
