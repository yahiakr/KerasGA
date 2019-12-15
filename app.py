import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from GeneticAlgorithm import GeneticAlgorithm


model = keras.Sequential([
    layers.Dense(4,input_dim=2, activation='sigmoid', name='fc1'),
    layers.Dense(2,activation='softmax', name='output')])

model.compile(optimizer=keras.optimizers.Adam(0.01),loss='categorical_crossentropy', metrics=['accuracy'])

GA = GeneticAlgorithm(model,population_size=5)



population = GA.initial_population()
