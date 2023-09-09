minimo = 0
maximo = 100
intentos = 0

print("Piensa en un número entre 0 y 100, y yo trataré de adivinarlo.")

while True:
    numero_adivinado = (minimo + maximo) // 2
    intentos += 1

    respuesta = input(f"¿Es {numero_adivinado} tu número? (responde '<', '>', '='): ")

    if respuesta == "=":
        print(f"¡OMG! Tu número es el {numero_adivinado}.")
        print(f"Me tomó {intentos} intentos para adivinarlo B)")
        break
    elif respuesta == "<":
        maximo = numero_adivinado - 1
    elif respuesta == ">":
        minimo = numero_adivinado + 1
    else:
        print("Respuesta no válida. Por favor, responde '<', '>' o '='.")
