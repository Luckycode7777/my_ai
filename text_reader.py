from collections import Counter

with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()  # приводим к нижнему регистру
    print(type(content))

"""1 Фильтруем: оставляем только буквы и цифры учитывая пробел"""
filtered_text = list(' '.join(char for char in content if char.isalnum()))
filtered_text_1 = ' '.join(char for char in content if char.isalnum())

"""2. - общее число символов"""
lst_simb = []
all_simbols = [lst_simb.append(i) for i in content]
print(len(all_simbols))

"""2. - число уникальных символов"""
lst_unic_simb = []
unic_simb = [lst_unic_simb.append(i) for i in filtered_text if i not in lst_unic_simb]
print(len(unic_simb))

"""3. Отсортируй вывод по убыванию частоты вручную, без most_common()"""
dic_all_simb = {}


for i in filtered_text:
    if i in dic_all_simb:
        dic_all_simb[i] += 1
    else:
        dic_all_simb[i] = 1
print(dic_all_simb)

print("*" * 10)
z = sorted(dic_all_simb)
print(z)


