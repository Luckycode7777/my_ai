import torch
import torch.nn as nn
import torch.nn.functional as F

# ================= Читаем текст =================
with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

# Оставляем только буквы, цифры и пробелы
filtered_text = ''.join(
    i for i in content if i.isalnum() or i == ' '
)

# ================= Словари =================
unic_simb = sorted(set(filtered_text))
char_index = {v: i for i, v in enumerate(unic_simb)}
index_char = {i: v for i, v in enumerate(unic_simb)}

# Кодируем текст
encoded_text = [char_index[i] for i in filtered_text]

# Данные для обучения
X = torch.tensor(encoded_text[:-1], dtype=torch.long)
Y = torch.tensor(encoded_text[1:], dtype=torch.long)

print("Размер X:", X.shape)
print("Размер Y:", Y.shape)

# ================= Модель =================
class BigramModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, vocab_size)

    def forward(self, x, targets=None):
        logits = self.embedding(x)  # (N, vocab_size)

        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, start_idx, max_new_tokens):
        idx = torch.tensor([start_idx], dtype=torch.long)

        for _ in range(max_new_tokens):
            logits, _ = self(idx)
            logits = logits[-1]  # берём последний символ
            probs = torch.softmax(logits, dim=0)
            next_idx = torch.multinomial(probs, num_samples=1)

            idx = torch.cat((idx, next_idx))

        return idx


# ================= Создание модели =================
vocab_size = len(unic_simb)
model = BigramModel(vocab_size)

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# ================= Обучение =================
for step in range(1000):
    logits, loss = model(X, Y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 100 == 0:
        print(f"step {step}, loss {loss.item()}")

# ================= Генерация =================
print("\n--- Генерация текста ---")

with torch.no_grad():
    start_symbol = 0  # можно менять
    generated = model.generate(start_symbol, 100)

decoded = ''.join(index_char[i.item()] for i in generated)
print(decoded)

