import random

x = random.randint(1, 100)
y = random.randint(1, 100)

print(f"x: {x}, y: {y}")

def solucion(x, y):
    return x + y

print("Resultado:")
print(solucion(x, y))

