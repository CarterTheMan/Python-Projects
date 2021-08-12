# Genetic Algorithm (Words)

This is a program that takes a phrase that the user inputs and starting with a random “population”, it mirrors evolution in real life, to reach the users starting input. For this explanation we will say that the users input is “hello world”.

1. The program starts out with an initial “population” which is made of “individuals”. Each individual is made of characters, which can be called “genes”.

2. Then for each individual it determines their “fitness” based on how many characters from that individual match the users input

   - For example “jells mirld” would have a fitness of 6

3. Then it creates a fitness array that contains each individual based on their fitness.

   - An individual with a fitness of 6 would be in the fitness array 6 times while something with a fitness of 0 wouldn’t be in the array.

4. Next is reproduction, which randomly selects two “parents” from the fitness array and creates a child based on the two adults.

   - If the parents are “hecks worth” and “jello wirld” the child could potentially be “hello world”

5. The final step is mutation which could randomly change single letters in each individual.

   - “hello thire” could mutate and become “hello there” if the “i” in thire becomes an e

6. Repeat steps 2-5 until the desired outcome. Each time you go through those steps it’s called a generation.
