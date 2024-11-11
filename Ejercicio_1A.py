while True:
    numero = float(input("Introduce un número (negativo para salir): "))
    
    if numero < 0:
        print("¡Hasta luego! Has introducido un número negativo.")
        break
    
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}.")