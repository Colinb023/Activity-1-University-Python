total = 0
while True:
    numero = float(input("Introduce un número (0 para terminar): "))

    if numero == 0:
        break
    
    total += numero

print(f"La suma total es: {total}.")