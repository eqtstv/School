import mat4py as m4p
import numpy as np
import matplotlib.pyplot as plt
import random as rnd


data1_load = m4p.loadmat('C:/my_pc/Code/moje/Identyfikacja/zadanie_1i2_zbior_1.mat')
data2_load = m4p.loadmat('C:/my_pc/Code/moje/Identyfikacja/zadanie_1i2_zbior_2.mat')
data3_load = m4p.loadmat('C:/my_pc/Code/moje/Identyfikacja/zadanie_1i2_zbior_3.mat')


def mat_to_list(mat_data):
    temp_zbior = list(mat_data.values())
    zbior = temp_zbior[0]
    return zbior

def plot_theta(data, start, stop, step):
    u = np.array([i[0] for i in data])
    y = np.array([i[1] for i in data])

    theta = np.arange(start, stop, step)
    results = []

    for i in range(len(theta)):
        q = 0
        for j in range(len(u)):
            q += (y[j] - (u[j]*theta[i]))**2
        results.append(q)

    plt.plot(theta, results)
    plt.show()
    return

def plot_values(data):
    u = np.array([i[0] for i in data])
    y = np.array([i[1] for i in data])

    plt.scatter(u, y)
    plt.show()
    return

def print_data(data):
    for i in range(len(data)):
        print(data[i])
    return

def calc_theta_star(data):
    u = np.array([i[0] for i in data])
    y = np.array([i[1] for i in data])

    numerator = 0
    denominator = 0

    for i in range(len(u)):
        numerator += y[i] * u[i]
        denominator += u[i]**2

    theta_star = numerator / denominator
    return theta_star

def find_solution(data, t_start, t_stop, t_step, increment_times):

    def calc_q(u, y, i, j):
        q = pow(y[j] - (u[j] * i), 2)
        return q

    u = np.array([i[0] for i in data])
    y = np.array([i[1] for i in data])

    teta = np.arange(t_start, t_stop, t_step)
    results = []

    for i in teta:
        q = 0
        for j in range(len(u)):
            q += calc_q(u, y, i, j)
        results.append(q)

    improv_x = []
    improv_y = []

    bad_x = []
    bad_y = []

    best_solution = float("Inf")
    best_x = 0

    for i in range(0, increment_times):
        rand_x = rnd.uniform(t_start, t_stop)
        solution = 0

        for j in range(len(u)):
            solution += calc_q(u, y, rand_x, j)

        if (solution < best_solution):
            improv_x.append(rand_x)
            improv_y.append(solution)
            best_solution = solution
            best_x = rand_x

        else:
            bad_x.append(rand_x)
            bad_y.append(solution)

    plt.plot(teta, results)
    plt.scatter(bad_x, bad_y)
    plt.scatter(improv_x, improv_y)
    plt.show()

    print("Best x: " + str(best_x))
    print("Best y: " + str(best_solution))

    return


def least_squares(data):

    u = np.array([i[0] for i in data])
    y = np.array([i[1] for i in data])

    a = 0
    b = 0

    n = len(u)

    a = (n * sum(u * y) - sum(u) * sum(y)) / (n * sum(u**2) - (sum(u)**2))
    b = (sum(y) * sum(u**2) - sum(u) * sum(u * y)) / (n * sum(u**2) - (sum(u)**2))

    return a, b

def plot_least_squares(data, start, stop, step):

    udd = np.array([i[0] for i in data])
    ydd = np.array([i[1] for i in data])

    a = least_squares(data)[0]
    b = least_squares(data)[1]

    def calc_y(x):
        return a*x + b

    u = np.arange(start, stop, step)
    y = []

    for i in range(len(u)):
        val = u[i]
        x = calc_y(val)
        y.append(x)

    plt.scatter(udd, ydd)
    plt.plot(u, y, color='orange')
    plt.show()

    return
    

zbior1 = mat_to_list(data1_load)
zbior2 = mat_to_list(data2_load)
zbior3 = mat_to_list(data3_load)

# wyświetlaj posortowane
#dd = np.array(zbior1)
#da = (dd[dd[:,0].argsort()])
#print(da)

#print_data(zbior1)
#print_data(zbior2)
#print_data(zbior3)


#print(calc_theta_star(zbior1))
#print(calc_theta_star(zbior2))
#print(calc_theta_star(zbior3))


#plot_theta(zbior1, -2.5, 2.5, 0.01)
#plot_theta(zbior2, 0, 2, 0.001)
#plot_theta(zbior3, 0, 2, 0.001)


#plot_values(zbior1)
#plot_values(zbior2)
#plot_values(zbior3)

#find_solution(zbior1, 0, 2, 0.001, 1000)
#find_solution(zbior2, 0, 2, 0.001, 1000)
#find_solution(zbior3, 0, 2, 0.001, 1000)

#print(least_squares(zbior1))
#print(least_squares(zbior2))
#print(least_squares(zbior3))

#plot_least_squares(zbior1, 16, 61, 1)
#plot_least_squares(zbior2, 5, 20, 1)
#plot_least_squares(zbior3, 0, 21, 1)