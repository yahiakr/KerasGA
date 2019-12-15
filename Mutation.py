import numpy as np
import copy
import random

mutation_rate = 0,3

def Mutation(algorithm,mutation_r):
    global mutation_rate
    mutation_rate = mutation_r
    return random_mutation

def random_mutation(base_offsprings):
    offsprings = []
    for offspring in base_offsprings:
        offspring_mutation = copy.deepcopy(offspring)
        for layer in range(len(offspring)):
            for i in range(offspring[layer].shape[0]):
                if offspring[layer].ndim != 1 :
                    for j in range(offspring[layer].shape[1]):
                        if np.random.choice([True, False], p=[mutation_rate, 1-mutation_rate]):
                            offspring_mutation[layer][i][j] = random.uniform(-1, 1)
        offsprings.append(offspring_mutation)
    return offsprings