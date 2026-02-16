# Мини-проект №3 — Подготовка данных для обучения

# символ → число | stoi = string-to-index
# число → символ | itos = index-to-strin

# Задача.

# 1. Вывести первые 10 элементов X
# 2. Вывести первые 10 элементов Y
# 3. Проверить, что Y — это X, сдвинутый на 1

"""Читаем текст из файла"""
with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

"""Фильтруем текст. Оставляем только буквы, цифры и пробелы"""
filtered_text = ''.join(
    i for i in content if i.isalnum() or i == ' '
)

"""1. Получаем список уникальных символов"""
unic_simb = sorted(set(filtered_text))
# print("1. Получаем список уникальных символов")
# print(unic_simb)
# print("***" * 7)


"""2. Создаем словарь string-to-index"""
char_index = {v: i for i, v in enumerate(unic_simb)}
# print("2. Создаем словарь string-to-index")
# print(char_index)
# print("***" * 7)


"""3. Создаем обратный словарь index-to-strin"""
index_char = {i: v for i, v in enumerate(unic_simb)}
# print("3. Создаем обратный словарь index-to-strin")
# print(index_char)
# print("***" * 7)


"""4. перевести весь текст в список чисел"""

# Кодирование через цикл
# encoded_text = []

# for i in filtered_text:
#     if i in char_index:
#         encoded_text.append(char_index[i])

# альтернативный вариант кодировки, более короткий
encoded_text = [char_index[i] for i in filtered_text]

# print("4. перевести весь текст в список чисел используя словарь index-to-strin ")
# print(encoded_text[:15])
# print("***" * 7)
# print(len(encoded_text))

# Вывести первые 10 элементов encoded_text в X
x = encoded_text[:-1]

# Вывести первые 10 элементов encoded_text в Y
y = encoded_text[1:]

print(x[:10])
print(y[:10])



# ОТДЕЛЬНЫЙ ВЫВОД.
# # уникальные элементы
# unic_list_char = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л',
#                 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
#
# # Создаем словарь string-to-index первых десяти элементов
# char_index_2 = {v: i for i, v in enumerate(unic_list_char)}
#
# # первод элементов в список чисел
# ten = [i for i in char_index_2.values()]
#
# # вывод чисел со свигом вправо
# x = ten[:-1]
# y = ten[1:]
#
# print(ten)
# print(x[:10])
# print(y[:10])