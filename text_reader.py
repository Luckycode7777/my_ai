with open('text.txt', 'r', encoding='utf-8') as file:
		content = file.read().lower()
# print(content)
print("Файл закрыт")

key_counter = {}

for i in content:
		if i in key_counter:
				key_counter[i] += 1
		else:
				key_counter[i] = 1

print(f"{key_counter}")
print("-------------------")

for i, count in sorted(key_counter.items()):
		print(f"'{i}': {count}")
