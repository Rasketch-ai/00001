#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Подключаем модули math и pyplot,а также библиотеку numpy
import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':       
    #Магия
    arguments = numpy.r_[0:200:0.1]
    #Задаем значения аргумента и шаг
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    #Строим график
    mpp.show()
    #Показываем график в окне

