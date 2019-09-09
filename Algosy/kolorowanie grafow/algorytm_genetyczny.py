import random as rd
import numpy as np

# sum values (1; x+1)
def consecutive_sum(x):
    w = 0
    for i in range(1, x+1):
        w += x
    return w

# draw random gene
def draw_random_gene(color_no):
    return rd.randint(0, color_no-1)

# draw starting population
def draw_starting_population(no_of_individuals, n, color_no):
    population = np.zeros((no_of_individuals, n))
    for i in range(no_of_individuals):
        for j in range(n):
            population[i][j] = draw_random_gene(color_no)
    return population

# rate individual
def rating(individual, M, n):
    fail_no = 0
    for i in range(len(individual)):
        for j in range(n):
            if M[i][j] != 0:
                if individual[i] == individual[j]:
                    fail_no += 1
    return fail_no

# select new population by ranking method
def selection_by_ranking_method(population, rating, M, n, no_of_individuals):
    measuring_indiv = []
    for i in range(population.shape[0]):
        measuring_indiv.append([population[i], rating(population[i], M, n)])
    sorted(measuring_indiv, key= lambda measuring_indiv: measuring_indiv[1], reverse=True)

    new_population = draw_starting_population(no_of_individuals, n, 1)
    max_los = consecutive_sum(population.shape[0])
    for i in range(population.shape[0]):
        los = rd.randint(0, max_los-1)
        x = 0
        while los < consecutive_sum(x):
            x += 1
        for j in range(population.shape[1]):
            new_population[i][j] = measuring_indiv[0][x][j]
    return new_population

# hybridizate population
def crossover(population, cross_condition, n):
    for i in range(0, population.shape[0], 2):
        cross = rd.random()
        if cross < cross_condition:
            cross_point = rd.randint(1, n-1)
            parent1 = population[i]
            parent2 = population[i+1]
            for j in range(n):
                if j <= cross_point:
                    population[i][j] = parent2[j]
                    population[i+1][j] = parent1[j]
    return population

# mutate populaton
def mutation(population, mutating_condition, color_no):
    for i in range(0, population.shape[0]):
        mutate = rd.random()
        if mutate < mutating_condition:
            for j in range(population.shape[1]):
                mutate_gene = rd.random()
                if mutate_gene < mutating_condition:
                    population[i][j] = draw_random_gene(color_no)
    return population

# return best individual
def best_individual(population, rating, M, n, best, best_f):
    best_grade = 99999999999
    for individual in population:
        grade = rating(individual, M, n)
        if grade < best_grade:
            best_grade = grade
            if grade < best_f:
                best_f = grade
                best = individual
    return best, best_f

# function for genetic coloring
def genetic_colloring(color_no, M, n, max_iter, no_of_individuals, stop_condition, cross_condition, mutating_condition):
    iter_no = 0
    best_f = 99999999
    population = draw_starting_population(no_of_individuals, n, color_no)
    best = population[0]
    rd.seed()

    while iter_no < max_iter and best_f > stop_condition:
        # selection
        population = selection_by_ranking_method(population, rating, M, n, no_of_individuals)
        # crossover
        population = crossover(population, cross_condition, n)
        # mutation
        population = mutation(population, mutating_condition, color_no)
        # check result
        best, best_f = best_individual(population, rating, M, n, best, best_f)
        iter_no += 1

    best_f /= 2
    if best_f <= stop_condition:
        return True, best_f
    else:
        return False, best_f





file = open("C:/my_pc/Code/moje/Algosy/kolorowanie grafow/q6x6.txt", 'r')
n = int(file.readline())
M = np.zeros((n,n))
for line in file:
    pom = line.split()
    M[int(pom[0])-1][int(pom[1])-1] = 1
file.close()

czy, best_f = genetic_colloring(10, M, n, 1000, 10, 5, 0.3, 0.8)
print(czy, best_f)