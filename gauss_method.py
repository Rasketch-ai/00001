''' Метод Гаусса '''
from numpy import array
import numpy as np
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
    for l in range (0, len(coef_matrix) - 1):  # Приведение матрицы к ступенчатому виду.
        while st_matrix[l][l] ==  0: # Поменяем строки,чтобы нуля не было там, где нам он не нужен.
            if score == len(coef_matrix) - (l + 1): # Чтобы не менять строки бесконечно, если весь столбец из нулей.
                break 
            score += 1 
            st_matrix = elem_str_change_1(l, l + score, st_matrix)
            v_column = elem_str_change_1(l, l + score, v_column)
        score = 0
        for i in range (l + 1, len(coef_matrix)): # Убиваем столбец
            if st_matrix[i][l] != 0 and st_matrix[l][l] != 0:
                e = (-1) * st_matrix[i][l] / st_matrix[l][l]
                v_column = elem_str_change_2(l, i, e, v_column)
                st_matrix = elem_str_change_2(l, i, e, st_matrix)
    print(st_matrix, v_column)
    sol_s = array([
        [v_column[-1][0] / st_matrix[-1][-1]]
    ], dtype = float)
    z = 0
    for j in range(1, len(st_matrix)):
        for k in range(0, j):
            z += st_matrix[-1 - j][len(st_matrix) - (k + 1)] * sol_s[k][0]
        sol_s = np.vstack([sol_s, [(v_column[-1 - j][0] - z) / st_matrix[-1 -j][-1 - j]]])
    print(sol_s)
    #for h in range(0, (len(sol_s) // 2) - 1):
        #sol_s = elem_str_change_1(h, len(sol_s) - (h + 1), sol_s)
    return sol_s
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
a = array([
    [1.5, 2.0, 1.5, 2.0],
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
#print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))


