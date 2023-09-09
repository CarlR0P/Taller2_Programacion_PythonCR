sumapositivos = 0
sumanegativos = 0

while True:
    numero = int(input("Ingrese un numero entero (positivo o negativo)(Se finaliza con 0): "))

    if numero == 0:
        break
    elif numero > 0:
        sumapositivos += 1
    else:
        sumanegativos += 1

print("Positivos son: " + "*" * sumapositivos)
print("Negativos son: " + "*" * sumanegativos)
