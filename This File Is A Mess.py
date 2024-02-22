import numpy as np
import math
import matplotlib.pyplot as plt

class RadioactiveDecay:
    def __init__(self, _number_of_particles, _decay_constant):
        """Initilize a radioactive decay
        
        Parameters
        ----------
        _number_of_particles : _Integer_
            Starting number of particles
        _decay_constant : _Float_
            decay constant of particle type [s]
        """

        self.t = 0.0
        self.N = _number_of_particles

        # set decay constant and halflife from decay constant given
        self.decay_constant = _decay_constant
        self.half_life = math.log(2.0)/self.decay_constant

        self.dt = 0.1*self.half_life

    def calculate(self, _dt=None):
        dt = self.dt
        if dt is not None:
            dt = _dt
        self.N -= self.decay_constant * self.N * _dt
        self.t += _dt

decay = RadioactiveDecay(1e6, math.log(2.0)/2)
N = [1e6]
time = [0.0]
num = int(decay.half_life*5/decay.dt)
for i in range(1, num):
    decay.calculate()
    N.append(decay.N)
    time.append(decay.t)
plt.semilogy(t, N)
plt.show()
