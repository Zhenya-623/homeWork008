# Напишите функцию read_last(lines, file), которая будет открывать определенный файл
# file и выводить на печать построчно последние строки в количестве lines (на всякий случай
# проверим, что задано положительное целое число). Протестируем функцию на
# файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


# with open('article.txt', 'r', encoding='utf-8') as file:
#     lines = int(input('Введите количество количество строк с конца текста для вывода: '))
#     if lines < 0:
#         lines = lines * -1
#     my_list = file.read().splitlines()
#     print(my_list)
#     count = 0
#     new_list = []
#     for i in range(len(my_list) - 1, -1, -1):
#         new_list.append(my_list[i])
#         count += 1
#         if count == lines:
#             print(list(reversed(new_list)))







# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).



# with open('article.txt', 'r', encoding='utf-8') as file:
#     text = file.read().split()
#     print(text)
#     longest_words = ''
#     new_list = []
#     for i in text:
#         if len(i) > len(longest_words):
#             longest_words = i
#     for i in text:
#         if len(i) == len(longest_words):
#             new_list.append(i)
#     print(new_list)
