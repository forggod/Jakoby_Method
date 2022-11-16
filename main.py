import random

e = 1e-3  # Допустимая погрешность

# region Генератор матрицы
random.seed()
n = int(input('Введите размер матрицы: '))
matrix = []
[matrix.append([(random.randint(1, 10)) for j in range(n)]) for i in range(n)]
x = [random.randint(1, 10) for i in range(n)]
for i in range(n):
    matrix[i][i] *= 1000

#   Ищем приесоединённый вектор
n = len(matrix)
b = []
for i in range(n):
    a = 0
    for j in range(n):
        a += matrix[i][j] * x[j]
    b.append(a)
# endregion

# matrix = [
#     [5, 2, -1],
#     [-4, 7, 3],
#     [2, -2, 4]
# ]
# b = [12, 24, 9]
# n = len(matrix)

# region Метод Якоби

vare = [e + 1] * n  # Вектор изменений переменных
k = 0  # Счётчик итераций
x = [0] * n
xk = [0] * n  # Вектор x новой итерации
while e < max(vare) < 10000 and k < 1000:
    for i in range(n):
        rd = 0
        for d in range(n):
            if i != d:
                rd += float(matrix[i][d] * x[d])
        xk[i] = float(1 / matrix[i][i] * (b[i] - rd))
    for i in range(n):
        vare[i] = float(abs(xk[i] - x[i]))
        x[i] = xk[i]
    k += 1
if max(vare) > 10000:
    print('Расходится')
print('Кол-во итераций:', k)
print('Текущее изменение ошибки:', max(vare))
# endregion
