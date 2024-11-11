suma_sueldos = 0
contador_mayores = 0

for i in range(10):
    sueldo = float(input(f"Introduce el sueldo #{i + 1}: "))
    
    suma_sueldos += sueldo
    
    if sueldo > 1000:
        contador_mayores += 1

print(f"La suma total de los sueldos es: {suma_sueldos}.")
print(f"Hay {contador_mayores} sueldos mayores a 1000 dólares.")