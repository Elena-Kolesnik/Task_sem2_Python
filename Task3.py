# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

N = int(input("Введите число N: "))
divider = 1
while divider <= N:
    divider = divider + 1
    if N % divider == 0:
        print(f"Наименьший натуральный делитель целого числа  {N} равен {divider}.")
        break