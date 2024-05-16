"""В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
Достоевского (т.е. с различными окончаниями, например, Достоевский,
Достоевского) в единственном экземпляре."""
import re
with open('Dostoevsky.txt', 'r', encoding='utf-8') as f1:
    file = f1.read()
    ends = re.findall(r'\bДостоевск[а-яё]+\b', file)   # Поиск совпадений в файле
    ready = list(set(ends))   # Исключение совпдений
print(ready)
