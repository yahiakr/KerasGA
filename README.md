# KerasGA
A simple and easy-to-use implementation of Genetic Algorithm for Keras NN models in Python.

## Features
* Instead of using backpropagation, use Genetic Algorithm to update the parameters/weights of the neural network while training the model.
* Create an initial population (of size: `population_size`) of randomly initialized chromosomes (i.e model weights).
* You can adjust the `selection_rate` & the `mutation_rate`.
* Perform the different GA operations (i.e Selection, Crossover, & Mutation).

## Examples
Here are a few projects based on this package:
* [yahiakr/FlappyAI](https://github.com/yahiakr/FlappyAI)
* [yahiakr/SnakeAI](https://github.com/yahiakr/SnakeAI)

## Usage
* Install `KerasGA` :
```
$ pip install KerasGA
```

* import `GeneticAlgorithm` from `KerasGA` and initiate an object :
```python
from KerasGA import GeneticAlgorithm

population_size =  10
GA = GeneticAlgorithm(model, population_size = population_size, selection_rate = 0.1, mutation_rate = 0.2)
```

**PS:** `model` is a Keras model.

* Generate the initial population:
```python
population = GA.initial_population()
```
* To set the wights of a model you can use `.set_weights()` built-in function:
```python
for chromosome in population:
	model.set_weights(chromosome)
	# then evaluate the chromosome (i.e assign its final score)
```

* After calculating the scores for each chromosome, it's time to select the top-performers:
```python
# Selection:
# 'scores' is a list of length = population_size
# 'top_performers' is a list of tuples: (chromosome, it's score)
top_performers = GA.strongest_parents(population,scores)

# Make pairs:
# 'GA.pair' return a tuple of type: (chromosome, it's score)
pairs = []
while len(pairs) != GA.population_size:
	pairs.append( GA.pair(top_performers) )

# Crossover:
base_offsprings =  []
for pair in pairs:
	offsprings = GA.crossover(pair[0][0], pair[1][0])
	# 'offsprings' contains two chromosomes
	base_offsprings.append(offsprings[-1])

# Mutation:
new_population = GA.mutation(base_offsprings)
```
And that's it :)
