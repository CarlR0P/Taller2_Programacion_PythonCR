import random

random_number = random.randint(1, 100)

numero = 0
intento = 0

while True:
    intento += 1
    numero = int(input("Intenta adivinar el número misterioso: "))

    if numero > random_number:
        print(f"El número {numero} es mayor al número misterioso.")
    elif numero < random_number:
        print(f"El número {numero} es menor al número misterioso.")
    else:
        print(f"Adivinaste, el {random_number} es el número misterioso.")
        print(f"Te tomó {intento} intentos para adivinarlo.")
        break
