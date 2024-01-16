"""Книжные магазины предлагают следующие коллекции книг.
Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
БукМаркет – Пушкин, Достоевский, Маяковский.
Галерея – Чехов, Тютчев, Пушкин. Определить:
1. Полный список всех книг магазинов.
2. Какие книги есть во всех магазинах.
3. Хотя бы одну книгу, которая есть не во всех магазинах."""
Magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
Housebooks = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
BookMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
Gallery = {'Чехов', 'Тютчев', 'Пушкин'}
print(Magistr | Housebooks | BookMarket | Gallery)
print(Magistr & Housebooks & BookMarket & Gallery)
print(Magistr - Housebooks - BookMarket - Gallery)