numeros = []

while True:
    entrada = input("Ingrese un número (Se finaliza con '.'): ")

    if entrada == ".":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")

if not numeros:
    print("No se ingresaron números.")
else:
    numeros.sort()

    cantidad = len(numeros)
    mitad = cantidad // 2

    if cantidad % 2 == 0:
        mediana = (numeros[mitad - 1] + numeros[mitad]) / 2.0
        print("La mediana es:", mediana)
    else:
        mediana = numeros[mitad]
        print("La mediana es:", mediana)
