import random

def fitness(x):
    # Objective function to maximize f(x) = x^2
    return x**2

# Generate initial population
population_size = 20
lower_bound = 0
upper_bound = 1000
population = [random.randint(lower_bound, upper_bound) for _ in range(population_size)]

def selection(population):
    # Select two parents based on their fitness (roulette wheel selection)
    fitness_values = [fitness(x) for x in population]
    total_fitness = sum(fitness_values)
    probabilities = [f/total_fitness for f in fitness_values]
    
    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    # Single-point crossover
    point = random.randint(1, len(bin(upper_bound))-2)
    bin1 = bin(parent1)[2:].zfill(len(bin(upper_bound))-2)
    bin2 = bin(parent2)[2:].zfill(len(bin(upper_bound))-2)
    
    offspring1 = int(bin1[:point] + bin2[point:], 2)
    offspring2 = int(bin2[:point] + bin1[point:], 2)
    
    return offspring1, offspring2

def mutate(offspring):
    # Random bit flip mutation
    bin_offspring = bin(offspring)[2:].zfill(len(bin(upper_bound))-2)
    mutation_point = random.randint(0, len(bin_offspring)-1)
    mutated = list(bin_offspring)
    mutated[mutation_point] = '1' if mutated[mutation_point] == '0' else '0'
    
    return int(''.join(mutated), 2)

# Genetic Algorithm
generations = 100
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
print(f'Best solution: x = {best_solution}, f(x) = {fitness(best_solution)}')
