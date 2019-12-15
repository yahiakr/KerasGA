import random

def Crossover(algorithm):
    return uniform

def uniform(x, y):
    offspring_x = x
    offspring_y = y
    for layer in range(len(x)):
        for i in range(x[layer].shape[0]):
            if x[layer].ndim != 1 :
                for j in range(x[layer].shape[1]):
                    if random.choice([True, False]):
                        offspring_x[layer][i][j] = y[layer][i][j]
                        offspring_y[layer][i][j] = x[layer][i][j]
    return offspring_x, offspring_y