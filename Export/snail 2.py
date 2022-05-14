#!/usr/bin/python
# -*- coding: utf-8 -*-

def filling(num):
    """
    Заполняем квадратную матрицу "улиткой"
    принимаем размер матрицы
    возвращаем заполненную матрицу в виде списка списков
    """
    result = []
    last = 1
    a = 0
    b = num
    for i in range(num):  # заполняем массив Нонами
        spam = []
        for y in range(num):
            spam.append(None)
        result.append(spam)
    while last < num ** 2 + 1:
        if last == num ** 2:
            result[a][a] = last
            break
        else:
            for y in range(a, b):
                result[a][y] = last
                last += 1
            for y in range(a + 1, b - 1):
                result[y][b - 1] = last
                last += 1
            for y in range(b - 1, a - 1, -1):
                result[b - 1][y] = last
                last += 1
            for y in range(b - 2, a, -1):
                result[y][a] = last
                last += 1
            a = a + 1
            b = b - 1
    for i in range(len(result)):
        for y in range(len(result[i])):
            result[i][y] = str(result[i][y])
        result[i] = '\t'.join(result[i])
    result = '\n'.join(result)
    return result


n = int(input('Введите число '))
print(filling(n))
