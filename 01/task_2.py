# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


num = int(input("Введите трехзначное число: "))
summa = 0
while num > 0:
    summa = summa + num % 10
    num = num // 10
else:
    print(f"Сумма цифр равна {summa}")
