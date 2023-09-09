total_tiempo = 0

while True:
    tiempo = int(input("Ingrese el tiempo del tramo en min (Se finaliza con 0): "))

    if tiempo == 0:
        break

    total_tiempo += tiempo

horas = total_tiempo // 60
minutos_restantes = total_tiempo % 60

print(f"El tiempo total de viaje fue: {horas} horas y {minutos_restantes} minutos.")