from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as file:
		content = file.read().lower()  # приводим к нижнему регистру


# Фильтруем: оставляем только буквы и цифры
filtered_text = ' '.join(char for char in content if char.isalnum())



counter_all_simbols = 0
counter_unic_simbols = 0
simb = []
x = []
z = [x.append(i) for i in filtered_text if i not in x]
# char_frequency = Counter(filtered_text) # список уникальных символов


# общее число символов
v = [simb.append(i) for i in content]
print(len(v))


# общее количество символов
print(f'Всего символов: {counter_all_simbols}')
print(f'Число уникальных символов: {len(x)}')

# 3.Отсортируй вывод по убыванию частоты вручную, без most_common()
count_chastoti = Counter(filtered_text)
# count_chastoti = list(count_chastoti)
print(count_chastoti)



