# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
# №1 выводятся только 0
# for i in range(1, 6):
#        print(0)
#
# №2 номерация строк выводится через текстовыую запись...
# for i in range (1):
#         print('1.' "0")
#         print('2.' "0")
#         print('3.' "0")
#         print('4.' "0")
#         print('5.' "0")
#
# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
# cnt = 0
# for i in range(1, 101, 10):
#      # print (i)
#         if i == 5:
#             cnt = cnt+1
#     print('Количество цифр 5:' + str(cnt))
#
#
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
#
# sum = 0
# for i in range(1,101):
#     sum+=i
#     print(sum)
#
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
#
# mult = 1
# for i in range(1,11):
#    mult*=i
# print(mult)
#
# Задача 5
# Вывести цифры числа на каждой строчке.
#
# integer_number = 316379
# print(integer_number%10, integer_number//100)
#
# while integer_number>0:
#    print (integer_number%10)
#    integer_number = integer_number//10
#
# Задача 6
# Найти сумму цифр числа.
# x=8
# y=9
# z=(x+y)
# print(z)
#
# Задача 7
# Найти произведение цифр числа.
# x=8
# y=9
# z=(x*y)
# print(z)
#
# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?
# integer_number = 2537609
# while integer_number>0:
#    if integer_number%10 == 5:
#        print('Yes')
#        break
#    integer_number = integer_number//10
# else: print('No')
#
# Задача 9
# Найти максимальную цифру в числе
# Первый вариант (не получилось):
# x = input (137569)
# m = max([int(i) for i in str(x)])
# print(m)
# Второй вариант (не получилось):
# a = int(input(137569))
# m = a%10
# a = a//10
# while a > 0:
#         if a%10 > m:
#             m = a%10
#             a = a//10
# print(m)
# Третий вариант:
# integer_num = 569286347
# х = 0
# integer_num > 0
#     if integer_num% 10> = х:
#         х = integer_num%10
#     integer_num = integer_num // 10
# print ('Максимальное число:', х)
#
#
# Задача 10
# Найти количество цифр 5 в числе
# Тоже не получилось:
# integer = int(input(2364895))
# i= 0
# while integer > 0:
#     last=integer%10
#     if last==5:
#         i= i+1
#         integer = integer // 10
# print('Количество цифр 5:', i)
