import numpy as np
import pandas as pd
import copy
import random
from random import shuffle

selection_rate = 0.4
population_size = 500
mutation_rate = 0.3

parents = int(population_size * selection_rate)

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

def strongest_parents(population, scores):
    scores_for_chromosomes = []
    for i in range(0, len(population)):
        scores_for_chromosomes.append(( population[i],scores[i] ))
    scores_for_chromosomes.sort(key=lambda x: x[1])
    top_performers = scores_for_chromosomes[-parents:]
    return top_performers

def pair(parents):
    total_parents_score = sum([x[1] for x in parents])
    pick = random.uniform(0, total_parents_score)
    return [roulette_selection(parents, pick), roulette_selection(parents, pick)]

def roulette_selection(parents, pick):
    shuffle(parents)
    current = 0
    for parent in parents:
        current += parent[1]
        if current > pick:
            return parent

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