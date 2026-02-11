from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as file:
		content = file.read().lower()   # приводим к нижнему регистру

# Фильтруем: оставляем только буквы и цифры
filtered_text = ' '.join(char for char in content if char.isalnum())

# Считаем частоту
char_frequency = Counter(filtered_text)

# Выводим топ-10
print("ТОП-10 букв и цифр (регистр не учитывается):")

for i, (char, count) in enumerate(char_frequency.most_common(10), 1):
		print(f"'{char}' : {count}")
