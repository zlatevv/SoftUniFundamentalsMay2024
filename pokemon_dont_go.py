pokemons = list(map(int, input().split()))
result = 0
flag = False
while pokemons:
    index = int(input())
    if index < 0:
        index = 0
        pokemons[0] = pokemons[-1]
        flag = True
    if index > len(pokemons) - 1:
        index = len(pokemons) - 1
        pokemons[-1] = pokemons[0]
        flag = True
    if not flag:
        removed_pokemon = int(pokemons.pop(index))
    if flag:
        removed_pokemon = pokemons[index]
    
    for i in range(len(pokemons)):
        if pokemons[i] <= removed_pokemon:
            pokemons[i] += removed_pokemon
        else:
            pokemons[i] -= removed_pokemon
    result += removed_pokemon
    flag = False
print(result)