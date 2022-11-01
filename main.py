import random

# https://old.math.tsu.ru/EEResources/cm/text/5_2.htm

def divide_line(line, j):
    div = line[j]
    for i in range(len(line)):
        line[i] /= div


def substract_line(first, second, num):
    div = second[num] / first[num]
    for i in range(len(second)):
        second[i] -= first[i] * div


r = 10

# region Генератор матрицы
random.seed()
n = int(input('Введите размер матрицы: '))
matrix = []
x = [random.randint(1, 20) for i in range(n)]
for i in range(n):
    matrix.append([round(float(random.randint(1, 50) / x[j]), r) for j in range(n)])
#   Запись матрицы в файл
f = open('matrix.txt', 'w')
for i in range(n):
    line = ''
    for j in range(n):
        line += str(matrix[i][j]) + ' '
    f.write(line + '\n')
f.write('\n(')
for i in range(n):
    si = ', '
    if i == n - 1:
        si = ')'
    f.write(str(x[i]) + si)
f.close()

# matrix = [
#     [1, 2, 4],
#     [-2, 1, -3],
#     [3, -2, -5]
# ]
# x = [-1, 2, -2]
# endregion

#   Ищем приесоединённый вектор
n = len(matrix)
b = []
for i in range(n):
    a = 0
    for j in range(n):
        a += matrix[i][j] * x[j]
    b.append(a)

for i in range(n):
    matrix[i].append(b[i])

# region Поиск вектора x
for j in range(n):
    for i in range(j + 1, n):
        if abs(matrix[i - 1][j]) < abs(matrix[i][j]):
            mat = matrix[i - 1]
            matrix[i - 1] = matrix[i]
            matrix[i] = mat
    #   Делим строку на главный элемент
    divide_line(matrix[j], j)
    #   Приводим к нулю значения ниже главного элемента
    for k in range(j + 1, n):
        substract_line(matrix[j], matrix[k], j)
#   Получили нашу матрицу
#   Находим вектор x
xe = [0] * n
for i in range(n - 1, -1, -1):
    xe[i] = matrix[i][n]
    for j in range(n - 1, i, -1):
        xe[i] -= matrix[i][j] * xe[j]
# endregion

print('Погрешность:')
maxim = 0
for i in range(n):
    if maxim < abs(round(x[i], r) - round(xe[i], 15)):
        maxim = abs(round(x[i], r) - round(xe[i], 15))
print(maxim)
