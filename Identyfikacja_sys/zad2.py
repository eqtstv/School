#optymalizacja funkcji (randomowe punkty)

import numpy as np
import matplotlib.pyplot as plt
import random as rnd

def calc_theta_star(u, y):

    numerator = 0
    denominator = 0

    for i in range(len(u)):
        numerator += y[i] * u[i]
        denominator += u[i]**2

    theta_star = numerator / denominator
    return theta_star



def f_sol(u, y, i, j):
    q = pow(y[j] - (u[j] * i), 2)
    return q


u = [2, 1, -1]
y = [3, 2, 1]

teta = np.arange(1, 1.2, 0.001)
results = []

for i in teta:
    q = 0
    for j in range(len(u)):
        q += f_sol(u, y, i, j)
    results.append(q)

improv_x = []
improv_y = []

bad_x = []
bad_y = []


best_solution = 1000

for i in range(0, 1000):
    rand_x = rnd.uniform(1, 1.2)
    solution = 0
    for j in range(len(u)):

        solution += f_sol(u, y, rand_x, j)

    if (solution < best_solution):
        improv_x.append(rand_x)
        improv_y.append(solution)
        best_solution = solution
        best_x = rand_x

    else:
        bad_x.append(rand_x)
        bad_y.append(solution)





print(calc_theta_star(u, y))

plt.plot(teta, results)
plt.scatter(bad_x, bad_y)
plt.scatter(improv_x, improv_y)
plt.show()

print(best_x)
print(best_solution)
