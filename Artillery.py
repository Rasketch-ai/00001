''' Модель полета обычного тела и ракеты '''
import math
import numpy as np
from matplotlib import pyplot as plt
g = 9.8
dt = 0.01
class Body: #Обычное тело
    def __init__(self, x, y, Vx, Vy):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.trajectory_x = []
        self.trajectory_y = []
    def advance(self):
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vy -= g * dt
dm = 0.1
U = 500
angle = 1.047
class Rocket(Body): #Ракета
    def __init__(self, x, y, Vx, Vy, m_fuel, m):
            self.x = x
            self.y = y
            self.m = m
            self.m_fuel = m_fuel
            self.Vx = Vx
            self.Vy = Vy
            self.trajectory_x = []
            self.trajectory_y = []
    def advance(self):
        while self.m_fuel != 0:
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)
            self.x += self.Vx * dt
            self.y += self.Vy * dt
            self.m -= dm
            self.m_fuel -= dm
            self.Vx += U*dm/self.m
            self.Vy += U*dm/self.m - g*dt/np.sin(angle)
        super() .__init__(self.x, self.y, self.Vx, self.Vy)
r = Rocket(0, 0, 10, 10, 60, 100)
b = Body(0, 0, 10, 10)
bodies = [r,b]
for t in np.r_[0:2:dt]: 
    for b in bodies: 
        b.advance()  
for b in bodies: 
    plt.plot(b.trajectory_x, b.trajectory_y)