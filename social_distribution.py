population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)
required_wealth = len(population) * min_wealth


if total_wealth < required_wealth:
    print("No equal distribution possible")
else:

    for i in range(len(population)):
        if population[i] < min_wealth:

            amount_needed = min_wealth - population[i]
            

            wealthiest_index = population.index(max(population))
        
            population[wealthiest_index] -= amount_needed
            population[i] += amount_needed

    print(population)