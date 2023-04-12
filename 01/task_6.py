# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
# 001001 -> yes


num_tiket = input("Введите шестизначный номер билета: ")

if int(num_tiket[0]) + int(num_tiket[1]) + int(num_tiket[2]) == int(num_tiket[3]) + int(num_tiket[4]) + int(num_tiket[5]):
    print("yes")
else:
    print("no")
