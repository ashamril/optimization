# Simple python code using Genetic Algorithm to find string

import numpy as np
import datetime

# 1. Initialize Population
# generate new gen
def create_gen(panjang_target):
# create random number from 32 to 126 (Character of ASCII) equal to length of target
    random_number = np.random.randint(32, 126, size=panjang_target)
# convert ASCII-based number to character and combine them all
    gen = ''.join([chr(i) for i in random_number])
    return gen

# calculate fitness of gen
def calculate_fitness(gen, target, panjang_target):
    fitness = 0
    for i in range(panjang_target):
# compare gen woth target array by array
        if gen[i:i+1] == target[i:i+1]:
            fitness += 1
# calculate percentage of fitness
    fitness = fitness / panjang_target * 100
    return fitness

# create population
def create_population(target, max_population, panjang_target):
    populasi = {}
    for i in range(max_population):
        gen = create_gen(panjang_target)
        genfitness = calculate_fitness(gen, target, panjang_target)
        populasi[gen] =  genfitness
    return populasi

# 2. Selection
# selection process
def selection(populasi):
# create dictionary pop and parent
    pop = dict(populasi)
    parent = {}
    for i in range(2):
# select the max fitness of 2 parents
        gen = max(pop, key=pop.get)
        genfitness = pop[gen]
        parent[gen] = genfitness
        if i == 0:
            del pop[gen]
    return parent

# 3. Crossover
# crossover
def crossover(parent, target, panjang_target):
# create dictionary child
    child = {}
# parents divided into 2 same parts
    cp = round(len(list(parent)[0])/2)
    for i in range(2):
# crossover and calculate fitness
        gen = list(parent)[i][:cp] + list(parent)[1-i][cp:]
        genfitness = calculate_fitness(gen, target, panjang_target)
        child[gen] = genfitness
    return child

# 4. Mutation
# mutation
def mutation(child, target, mutation_rate, panjang_target):
# create dictionary mutant
    mutant = {}
    for i in range(len(child)):     
        data = list(list(child)[i])
        for j in range(len(data)):
            if np.random.rand(1) <= mutation_rate:
# if np.random.rand(1) less or equal than mutation rate
                ch = chr(np.random.randint(32, 126))
                data[j] = ch
# combine 1 character from mutation into gen
        gen = ''.join(data)
        genfitness = calculate_fitness(gen, target, panjang_target)
        mutant[gen] = genfitness
    return mutant

# 6. Regeneration of Population
# create new population with new best gen
def regeneration(mutant, populasi):
    for i in range(len(mutant)):
# delete 1 bad parent from the population and replace by mutant
        bad_gen = min(populasi, key=populasi.get)
        del populasi[bad_gen]
    populasi.update(mutant)
    return populasi

# get best gen in a population
def bestgen(parent):
    gen = max(parent, key=parent.get)
    return gen

# get best fitness in a population
def bestfitness(parent):
    fitness = parent[max(parent, key=parent.get)]
    return fitness

# display function
def display(parent):
    timeDiff=datetime.datetime.now()-startTime
    print('{}\t{}\t{}\t{}'.format(bestgen(parent), round(bestfitness(parent), 2), timeDiff, str(total_gen)))

# main program
target = 'Optimization with Natured-Inspired Computing'
max_population = 10
mutation_rate = 0.01

print('')
print('Target Word :', target)
print('Max Population :', max_population)
print('Mutation Rate :', mutation_rate)

panjang_target = len(target)
startTime=datetime.datetime.now()
print('----------------------------------------------------------------------------------')
print('{}\t{}\t{}\t{}'.format('The Best                                   ','Fitness','Time       ','Generation'))
print('----------------------------------------------------------------------------------')
populasi = create_population(target, int(max_population), panjang_target)
parent = selection(populasi)

total_gen = 0
display(parent)
while 1:
    child = crossover(parent, target, panjang_target)
    mutant = mutation(child, target, float(mutation_rate), panjang_target)
    if bestfitness(parent) >= bestfitness(mutant):
        continue
    populasi = regeneration(mutant, populasi)
    parent = selection(populasi)
    total_gen = total_gen + 1
    display(parent)
# 5. Evaluation
    if bestfitness(mutant) >= 100:
        break
