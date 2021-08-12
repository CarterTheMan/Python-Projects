import random

##Initialize (Create population)
##Create array of fitness
##Selection (Evaluate fitness of each population)
##Reproduction
    ##Pick two parents (According to fitness)
    ##Crossover - create a child by combining parents
    ##Mutation - Mutate child's DNA based on a given probability
    ##Add new children to population

popMax = 50
cont = 0
gen = 1
mutationRate = 2
generation = []
solutions = []
chars = 'abcdefghijklmnopqrstuvwxyz '

##Method to split words into individual letters
def split(word):
    return [char for char in word]


##Get the target phrase
target = input("What is the target phrase? (lowercase only) ")

##Creates the random first generation
for i in range(popMax):
    genInsert = ""
    ##Generates the random first population
    for j in target:
        genInsert = genInsert + random.choice(chars)
    ##Adds the generation to the population
    generation.append(genInsert)

while cont != 1:
    ##Printes the generation number
    print("Generation: ", gen)

    ##Prints the population
    for i in range(popMax):
        print(i + 1, ": ", generation[i])

    ##Create and fill array of fitness
    fitness = []
    ##Fills the fitness array
    for i in range(popMax):
        fitnessTest = 0
        ##Tests to see if some letters lined up to match and if they do it adds one to the fitness
        for j in range(len(target)):
            genz = generation[i]
            if target[j] == genz[j]:
                fitnessTest = fitnessTest + 1
        ##Adds the fitnessTest to the fitness array
        fitness.append(fitnessTest)
        ##If the fitness equals the target then the solution has been found and it ends the while statement
        if fitnessTest == len(target):
            cont = 1
            solutions.append(i + 1)

    ##Creates fitness array
    fitnessArray = []
    for i in range(popMax):
        for j in range(fitness[i] * fitness[i]):
            fitnessArray.append(generation[i])

    ##Prints combination array
    ##print(fitnessArray)

    ##Pick two parents and create child added to new generation
    for i in range(popMax):
        ##Initializes the two parents out of fitnessArray
        parentA = random.choice(fitnessArray)
        parentB = random.choice(fitnessArray)
        newGen1 = ""
        ##Crosses the parents to make the new generation
        for j in range(len(target)):
            rand = random.randint(0, 9)
            if rand <= 4:
                newGen1 = newGen1 + parentA[j]
            if rand > 4:
                newGen1 = newGen1 + parentB[j]
        newGen2 = split(newGen1)
        newGenWord = ""
        ##Mutates the child of the parents
        for j in range(len(target)):
            rand = random.randint(0, 100)
            if rand <= mutationRate:
                newGen2[j] = random.choice(chars)
            newGenWord = newGenWord + newGen2[j]
        ##Sets the child as the new adult
        generation[i] = newGenWord

    ##Adds one to the generation count
    gen = gen + 1

##Print out the solutions
if len(solutions) == 1:
    print("Solved in: ", gen, " generations")
    print("The solution is on line: ", solutions)
if len(solutions) > 1:
    for i in range(len(solutions)):
        print("Solved in: ", gen, " generations")
        print("The solutions are on lines: ", solutions)
