import pandas as pds
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np


''' Измерение показателя адиабаты воздуха методом Клемана-Дезорма '''
# Результат лабы
results = pds.Series([1.3302, 1.2820, 1.2765, 1.2708, 1.2641, 1.2790, 1.3240, 1.3148])

# А теперь закроем глазки и представим, что у нас все настолько хорошо, что распределение получилось нормальным
n_r = np.random.normal(results.mean(), results.std(), len(results))
normal_results = pds.Series(n_r)

# Сравним мечты с реальностью
print("Результат лабы:", stats.kstest(results, "norm", (results.mean(), results.std()), N = len(results)))
print("Нормальное распределение:", stats.kstest(normal_results, "norm", (results.mean(), results.std()), N = len(results)))


#normal_results.plot.kde()
#results.plot.kde()
#plt.show()