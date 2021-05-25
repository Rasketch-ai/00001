import math
import numpy as np
from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.01

U = 500
angle = 4.047

class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.
        
        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT

class Rocket(Body):
    def __init__(self, x, y, vx, vy, rocket_mass, powder_mass):
        super().__init__(x, y, vx, vy)
        self.rocket_mass = rocket_mass
        self.powder_mass = powder_mass
    
    def advance(self):
        if self.powder_mass != 0:
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)
        
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
            #self.vy += MODEL_G**2 * MODEL_DT
            #self.vx += MODEL_G**2 * MODEL_DT

            self.vy += 0.5*U/self.rocket_mass - MODEL_G*MODEL_DT/np.sin(angle)
            self.vx += 0.5*U/self.rocket_mass
            self.powder_mass -= 0.5
        else:
            super().advance()


np.sin

b = Body(100, 100, 5, 109)
r = Rocket(100, 100, 5, 4, 1550, 155)

bodies = [b, r]
# Дальше мы уже не будем думать, кто тут ёжик, кто ракета, а кто котлета —
# благодаря возможностям ООП будем просто работать со списком тел

for t in np.r_[0:25:MODEL_DT]: # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг


from matplotlib import pyplot as pp

for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории

pp.show()
