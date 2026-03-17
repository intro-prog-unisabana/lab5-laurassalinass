import random
aleatorio= random.seed(123)
print("Enter the start value:\n")
inicial=int(input())
print("Enter the end value:\n")
final= int(input())
entero_aleatorio = random.randint(inicial, final)
print("Generated random number:", entero_aleatorio)