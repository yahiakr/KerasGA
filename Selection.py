from random import shuffle


def Selection(algorithm):
    return roulette_selection

def roulette_selection(parents, pick):
    shuffle(parents)
    current = 0
    for parent in parents:
        current += parent[1]
        if current > pick:
            return parent