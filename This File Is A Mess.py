import numpy as np
import math
import matplotlib.pyplot as plt

class RadioactiveDecay:
    def __init__(self, _number_of_particles, _decay_constant):
        self.time = 0.0
        self.number_of_particles = _number_of_particles
        self.decay_constant = _decay_constant
        self.half_life = math.log(2.0)/self.decay_constant
        self.dt = 0.1*self.half_life

    def calculate(self, dt=None):
        _dt = self.dt
        if dt is not None:
            _dt = dt
        self.number_of_particles -= self.decay_constant * self.number_of_particles * _dt
        self.t += _dt

decay = RadioactiveDecay(1e6, math.log(2.0)/2)
N = [1e6]
time = [0.0]
num = int(decay.half_life*5/decay.dt)
for i in range(1, num):
    decay.calculate()
    N.append(decay.number_of_particles)
    time.append(decay.time)
plt.semilogy(t, N)
plt.show()
