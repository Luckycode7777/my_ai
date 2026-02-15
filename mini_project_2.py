# Мини-проект №2 — Токенизация

# символ → число | stoi = string-to-index
# число → символ | itos = index-to-strin

# Задача.

# 1. Получить список уникальных символов
# 2. Создать словарь: {'а': 0, 'б': 1, 'в': 2, ...}
# 3. Создать обратный словарь: {0: 'а', 1: 'б', 2: 'в', ...}
# 4. Превратить весь текст в список чисел

"""Читаем текст из файла"""
with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

"""Фильтруем текст. Оставляем только буквы, цифры и пробелы"""
filtered_text = ''.join(
    i for i in content if i.isalnum() or i == ' '
)

"""1. Получаем список уникальных символов"""
unic_simb = sorted(set(filtered_text))
print("1. Получаем список уникальных символов")
print(unic_simb)
print("***" * 7)


"""2. Создаем словарь string-to-index"""
char_index = {v: i for i, v in enumerate(unic_simb)}
print("2. Создаем словарь string-to-index")
print(char_index)
print("***" * 7)


"""3. Создаем обратный словарь index-to-strin"""
index_char = {i: v for i, v in enumerate(unic_simb)}
print("3. Создаем обратный словарь index-to-strin")
print(index_char)
print("***" * 7)


"""4. перевести весь текст в список чисел"""

# Кодирование через цикл
# encoded_text = []

# for i in filtered_text:
#     if i in char_index:
#         encoded_text.append(char_index[i])

# альтернативный вариант кодировки, более короткий
encoded_text = [char_index[i] for i in filtered_text]

print("4. перевести весь текст в список чисел используя словарь index-to-strin ")
print(encoded_text[:50])
print("***" * 7)
