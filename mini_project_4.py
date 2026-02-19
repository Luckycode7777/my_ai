# Мини-проект №4 — Первая языковая модель (Bigram)
# создадим самую простую языковую модель

# Она будет учиться: текущий символ → следующий символ  --->> Это называется Bigram Model.

# У нас есть: vocab_size = количество уникальных символов
# Мы создаём таблицу: vocab_size × vocab_size

# Каждая строка = текущий символ
# Каждый столбец = вероятность следующего символа

# Модель просто учится заполнять эту таблицу.
# =======================================================================
import torch
import torch.nn as nn
import torch.nn.functional as F

"""Читаем текст из файла"""
with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

"""Фильтруем текст. Оставляем только буквы, цифры и пробелы"""
filtered_text = ''.join(
    i for i in content if i.isalnum() or i == ' '
)

"""1. Получаем список уникальных символов"""
unic_simb = sorted(set(filtered_text))

"""2. Создаем словарь string-to-index"""
char_index = {v: i for i, v in enumerate(unic_simb)}

"""3. Создаем обратный словарь index-to-strin"""
index_char = {i: v for i, v in enumerate(unic_simb)}

"""4. перевести весь текст в список чисел"""

# альтернативный вариант кодировки, более короткий
encoded_text = [char_index[i] for i in filtered_text]

# print("4. перевести весь текст в список чисел используя словарь index-to-strin ")
# print(encoded_text[:15])
# print("***" * 7)
# print(len(encoded_text))


x = encoded_text[:-1]  # Срез элементов списка, выводит все элементы кроме последнего

y = encoded_text[1:]  # Срез элементов списка, выводит эл списка начиная со второго элемента

# здесь начинается 4 проект =======================
X = torch.tensor(encoded_text[:-1], dtype=torch.long)  # Создается целочисленный тензор(тензор-многомерный массив)
Y = torch.tensor(encoded_text[1:], dtype=torch.long)  # Создается целочисленный тензор(тензор-многомерный массив)

print(X.shape)  # Выводит размерность (форму) тензора X
print(Y.shape)


class BigramModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, vocab_size)

    def forward(self, x, targets=None):
        logits = self.embedding(x)
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits, targets)

        return logits, loss


vocab_size = len(unic_simb)
model = BigramModel(vocab_size)

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for step in range(1000):
    logits, loss = model(X, Y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 100 == 0:
        print(f"step {step}, loss {loss.item()}")
