import numpy as np
import multiprocessing
import time
import matplotlib.pyplot as plt

''' Запустить несколько раундов генерации сумм равномерно распределённых псевдослучайных величин,
собрать результаты, построить и показать гистограмму при помощи matplotlib '''

ITERATIONS = 10000

def sum_randoms (number): # складываем чиселки от 1 до number
    sum_ = 0
    for i in range(0,number):
        sum_ += np.random.uniform(0,number)
    return sum_

def test_all(pool): # Параллелим и строим гистограмму
    set_ = pool.map(sum_randoms, [1000] * ITERATIONS )
    axis_1 = np.arange(1,ITERATIONS + 1)
    axis_2 = set_
    fig, hyst = plt.subplots()
    hyst.bar(axis_1, axis_2)
    return set_

def comm_test_all(number): #  Без распараллеливания
    st = [1000] * number
    result = []
    for i in range(0, number):
        result.append(st[i])
    axis_1 = np.arange(1,ITERATIONS + 1)
    axis_2 = result
    fig, hyst = plt.subplots()
    hyst.bar(axis_1, axis_2)
    return result


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    s_time = time.time()
    rr = test_all(pool)
    print("Затраты времени с распараллеливанием:", time.time() - s_time)
    plt.show()
else:
    print(__name__)


'''s_time = time.time()
tt = comm_test_all(ITERATIONS)
print("Затраты времени без распараллеливания:", time.time() - s_time)
plt.show()'''
