#wyświetlanie funkcji kwadratowej

import numpy as np
import matplotlib.pyplot as plt
import random as rnd

u = np.array([2, 1, -1])
y = np.array([3, 2, 1])

teta = np.arange(0, 4, 0.001)
wyniki = []

for i in range(len(teta)):
    q = 0
    for j in range(len(u)):
        q += pow(y[j] - (u[j]*teta[i]), 2)
    wyniki.append(q)



plt.plot(teta, wyniki)
plt.show()