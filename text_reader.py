from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as file:
		content = file.read().lower()  # приводим к нижнему регистру

# Фильтруем: оставляем только буквы и цифры
filtered_text = ' '.join(char for char in content if char.isalnum())

# Считаем частоту
char_frequency = Counter(filtered_text)

# Выводим топ-10
print("ТОП-10 букв и цифр (регистр не учитывается):")

counter_all_simbols = 0
counter_unic_simbols = 0
x = []
z = [x.append(i) for i in filtered_text if i not in x]


for i, (char, count) in enumerate(char_frequency.most_common(10), 1):
		counter_all_simbols += count
		print(f"'{char}' : {count}")

# общее количество символов
print(f'Всего символов: {counter_all_simbols}')
print(f'Уникальных символов: {len(x)}')
