import numpy as np
import pandas as pd
import random

from KerasGA.Selection import Selection
from KerasGA.Crossover import Crossover
from KerasGA.Mutation import Mutation

class GeneticAlgorithm(object):

    def __init__(self, model, population_size = 500, selection_rate = 0.4, mutation_rate = 0.3, 
                selection='roulette_selection',crossover='uniform',mutation='random_mutation'):
        self.model = model
        self.population_size = population_size
        self.parents = int(population_size * selection_rate)
        self.mutation_rate = mutation_rate
        self.selection = Selection(selection)
        self.crossover = Crossover(crossover)
        self.mutation = Mutation(mutation,mutation_rate)

    def generate_weights(self,shape):
        weights = []
        for _ in range(shape[0]):
            node = []
            for _ in range(shape[1]):
                random_value = random.uniform(-1, 1)
                node.append(random_value)
            weights.append(np.array(node,dtype= 'float32'))
            
        weights = np.array(weights,dtype= 'float32')
        biases = np.zeros(shape[1],dtype= 'float32')
        return [weights,biases]

    def generate_chromosome(self):
        chromosome = []
        for layer in self.model.layers:
            for weights in layer.weights:
                if len(weights.shape) != 1 :
                    chromosome += self.generate_weights(weights.shape)
        return chromosome

    def initial_population(self):
        chromosomes = []
        for _ in range(self.population_size):
            chromosomes.append(self.generate_chromosome())
        return chromosomes
    
    def strongest_parents(self, population, scores):
        scores_for_chromosomes = []
        for i in range(0, len(population)):
            scores_for_chromosomes.append(( population[i],scores[i] ))
        scores_for_chromosomes.sort(key=lambda x: x[1])
        top_performers = scores_for_chromosomes[-self.parents:]
        return top_performers
    
    def pair(self,strongest_parents):
        total_parents_score = sum([x[1] for x in strongest_parents])
        pick = random.uniform(0, total_parents_score)
        return [self.selection(strongest_parents, pick), self.selection(strongest_parents, pick)]