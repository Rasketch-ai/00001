''' Метод Гаусса '''
from numpy import array
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

def gauss_method(coef_matrix, value_column): # Приведение матрицы к ступенчатому виду.
    st_matrix = coef_matrix
    score = 0
    for l in range (0, len(coef_matrix) - 1):
        print(st_matrix, value_column)
        while st_matrix[l][l] ==  0: # Поменяем строки,чтобы нуля не было там, где нам он не нужен.
            if score == len(coef_matrix) - (l + 1): # Чтобы не менять строки бесконечно, если весь столбец из нулей.
                break 
            score += 1 
            st_matrix = elem_str_change_1(l, l + score, st_matrix)
            value_column = elem_str_change_1(l, l + score, value_column)
            print(st_matrix, value_column)
        score = 0
        for i in range (l + 1, len(coef_matrix)): # Убиваем столбец.
            if st_matrix[i][l] != 0 and st_matrix[l][l] != 0:
                st_matrix = elem_str_change_2(l, i, (-1) * st_matrix[i][l] / st_matrix[l][l], st_matrix)
                value_column = elem_str_change_2(l, i, (-1) * st_matrix[i][l] / st_matrix[l][l], value_column)
    return (st_matrix, value_column)

from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
a = array([
    [0.0, 2.0, 1.5, 1.0],
    [3.0, 2.0, 4232.0, 1.0],
    [1.0, 6.0, 0.0, 4 ],
    [2.0, 112.0, 4.0, 3.12 ]
], dtype=float)

b = array([
    [51.0],
    [6.0], 
    [72.0], 
    [88.0]
], dtype = float)

print(gauss_method(a, b)) 
print(elem_str_change_2(0, 1, 1, b))
       

