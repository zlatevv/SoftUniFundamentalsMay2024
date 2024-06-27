class Zoo:
    __animals = 0
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        self.species = species
        if self.species == "mammal":
            self.mammals.append(name)
        elif self.species == "fish":
            self.fishes.append(name)
        elif self.species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1
    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        result += f"\nTotal animals: {Zoo.__animals}"
        return result
name = input()
number = int(input())
zoo = Zoo(name)
for _ in range(number):
    animal_info = input().split()
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)
species = input()
print(zoo.get_info(species))