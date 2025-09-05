# first we import the " random " module ( library ) so we can use its functions
import random

# random.random() => returns a random float between 0.0 and 1.0

print ("the random number is : ", random.random())

# random.randint(a,b) returns a random integer between a and b

print ("the random number is : ", random.randint(0,10))

# random.uniform(a,b) returns a random float between a and b

print("the random number is : ", random.uniform(0,100))

# random.choice(seq) picks a random element from a list, tuple or string

list = ["meriem", "inas", "ines", "ferdaous", "hiba"]

print("random name : ", random.choice(list))
