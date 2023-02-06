# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input("Введите вещественное число: ")
num = num.replace('.', '').replace(',', '')
res = sum([int(elem) for elem in num])
print(num,'->', res)