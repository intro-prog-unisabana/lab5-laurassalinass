import os
import math

# 1. imprimir el directorio actual
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# 2. pedir un entero al usuario
num = int(input("Enter an integer: "))

# calcular log base 2
log_val = math.log2(num)

print(f"Log base 2 of {num} is: {log_val}")

# 3. imprimir piso y techo
print(f"Floor: {math.floor(log_val)}")
print(f"Ceiling: {math.ceil(log_val)}")