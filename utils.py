import numpy as np
import pandas as pd
import copy
import random

population_size = 10
mutation_rate = 0.5

def generate_weights(shape):
    layer = []
    for _ in range(shape[0]):
        node = []
        for _ in range(shape[1]):
            random_value = random.uniform(-1, 1)
            node.append(random_value)
        layer.append(np.array(node,dtype= 'float32'))
        
    layer = np.array(layer,dtype= 'float32')
    zeros = np.zeros(shape[1],dtype= 'float32')
    return [layer,zeros]

def generate_chromosome(model):
    chromosome = []
    for layer in model.layers:
        for weights in layer.weights:
            if len(weights.shape) != 1 :
                chromosome += generate_weights(weights.shape)
    return chromosome

def initial_population(model):
    chromosomes = []
    for _ in range(population_size):
        chromosomes.append(generate_chromosome(model))
    return chromosomes

def crossover(x, y):
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

def mutation(base_offsprings):
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