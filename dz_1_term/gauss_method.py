''' Метод Гаусса '''
from numpy import array
import numpy as np
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

''' Сначала напишем функции для элемантарных преобразований, которые нам нужны '''

def elem_str_change_1(m, n, matrix): # Перестановка строк с номерами m и n
    for k in range (0, len(matrix[m])):
        x = matrix[m][k]
        matrix[m][k] = matrix[n][k]
        matrix[n][k] = x
    return matrix

def elem_str_change_2(m, n, e, matrix): # Домножаем строку m на e и прибавляем к n.
    matrix[n] += matrix[m] * e
    return matrix

def gauss_method(coef_matrix, value_column):
    st_matrix = coef_matrix
    v_column = value_column
    score = 0
    c = len(st_matrix) - 1
    for l in range (0, c):  # Приведение матрицы к ступенчатому виду.

        while st_matrix[l][l] ==  0: # Поменяем строки,чтобы нуля не было там, где нам он не нужен.
            if score == c - l: # Чтобы не менять строки бесконечно, если весь столбец из нулей.
                break
            score += 1
            st_matrix = elem_str_change_1(l, l + score, st_matrix)
            v_column = elem_str_change_1(l, l + score, v_column)
        score = 0

        for i in range (l + 1, c + 1): # Убиваем столбец
            if st_matrix[i][l] != 0 and st_matrix[l][l] != 0:
                e = (-1) * st_matrix[i][l] / st_matrix[l][l]
                v_column = elem_str_change_2(l, i, e, v_column)
                st_matrix = elem_str_change_2(l, i, e, st_matrix)

    for k in range(0,c):
        for j in range (k + 1, c + 1): # оставим только диагональ
            if st_matrix[c - j][c - k] != 0 and st_matrix[c - k][c - k] != 0:
                d = (-1) * st_matrix[c - j][c - k] / st_matrix[c - k][c - k]
                v_column = elem_str_change_2(c - k, c - j, d, v_column)
                st_matrix = elem_str_change_2(c - k, c - j, d, st_matrix)

    sol_s = array([  # Массив, в который мы запишем решения
        [v_column[0][0] / st_matrix[0][0]]
    ], dtype = float)
    
    for q in range(1, c + 1): # Записываем решения
        sol_s = np.vstack([sol_s, [v_column[q][0] / st_matrix[q][q]]])
    return sol_s


a = array([
    [1.0, 2.0, 1.0, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([
    [5],
    [6],
    [7],
    [8]
],dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss_method(a, b)
print(oob_solution) 
print(solution)
# С дальнейшим print что-то непонятное, однако так все равно наглядно видно, что решения идентичны
