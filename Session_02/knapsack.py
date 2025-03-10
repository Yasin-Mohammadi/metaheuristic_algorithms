import random

# Problem definition
items = [
    {'weight': 10, 'value': 60},
    {'weight': 20, 'value': 100},
    {'weight': 30, 'value': 120},
    {'weight': 5, 'value': 20},
    {'weight': 15, 'value': 50}
]
capacity = 50
population_size = 20

def fitness(individual):
    total_weight = 0
    total_value = 0
    for i, gene in enumerate(individual):
        if gene == 1:
            total_weight += items[i]['weight']
            total_value += items[i]['value']
    if total_weight > capacity:
        return 0
    return total_value

def generate_individual():
    return [random.choice([0, 1]) for _ in range(len(items))]

def selection(population):
    fitness_values = [fitness(ind) for ind in population]
    total_fitness = sum(fitness_values)
    probabilities = [f/total_fitness for f in fitness_values]
    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    point = random.randint(1, len(items)-1)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

def mutate(individual):
    mutation_point = random.randint(0, len(items)-1)
    individual[mutation_point] = 1 - individual[mutation_point]
    return individual

# Genetic Algorithm
generations = 100
population = [generate_individual() for _ in range(population_size)]

for generation in range(generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = selection(population)
        offspring1, offspring2 = crossover(parent1, parent2)
        offspring1 = mutate(offspring1)
        offspring2 = mutate(offspring2)
        new_population.extend([offspring1, offspring2])
    population = new_population

# Find the best solution
best_solution = max(population, key=fitness)
best_value = fitness(best_solution)
best_weight = sum(items[i]['weight'] for i in range(len(best_solution)) if best_solution[i] == 1)

print(f'Best solution: {best_solution}')
print(f'Total value: {best_value}, Total weight: {best_weight}')
