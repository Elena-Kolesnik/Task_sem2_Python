# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

N = int(input("Введите количество монет на столе: "))
k = 0
for i in range(N):
    coin = int(input())
    if coin == 1:
        k += 1
print(f"Минимальное количество монет, которые нужно перевернуть: {k if k < N / 2 else N - k}")
