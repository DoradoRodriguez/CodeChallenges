import random
from random import uniform

precio = uniform(1, 100)
descuento = random.randint(1, 100)

print(precio)
print(descuento)

def descontar(precio, descuento):
    return round(precio * (descuento / 100))

print("Resultado: ")
print(descontar(precio, descuento))

 

