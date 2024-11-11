contador = 0

while True:
    numero = float(input("Introduce un número (negativo para terminar): "))
    
    if numero < 0:
        break
    
    contador += 1

print(f"Se ingresaron {contador} números.")