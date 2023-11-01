import math

def calculadora_cientifica():
    print("Calculadora Científica")
    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Exponencial")
        print("8. Logaritmo natural (ln)")
        print("9. Logaritmo base 10 (log)")
        print("10. Seno")
        print("11. Coseno")
        print("12. Tangente")
        print("0. Salir")
        
        opcion = int(input("Elige una opción: "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion in [1, 2, 3, 4]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if opcion == 1:
                resultado = a + b
            elif opcion == 2:
                resultado = a - b
            elif opcion == 3:
                resultado = a * b
            elif opcion == 4:
                if b != 0:
                    resultado = a / b
                else:
                    print("No se puede dividir por cero.")
                    continue
        elif opcion == 5:
            a = float(input("Ingrese la base: "))
            b = float(input("Ingrese el exponente: "))
            resultado = math.pow(a, b)
        elif opcion == 6:
            a = float(input("Ingrese el número para calcular la raíz cuadrada: "))
            resultado = math.sqrt(a)
        elif opcion == 7:
            a = float(input("Ingrese el número para calcular la exponencial: "))
            resultado = math.exp(a)
        elif opcion == 8:
            a = float(input("Ingrese el número para calcular el logaritmo natural (ln): "))
            resultado = math.log(a)
        elif opcion == 9:
            a = float(input("Ingrese el número para calcular el logaritmo en base 10: "))
            resultado = math.log(a)/(math.log(10))
        elif opcion in [10, 11, 12]:
            a = float(input("Ingrese el ángulo en radianes: "))
            if opcion == 9:
                resultado = math.sin(a)
            elif opcion == 10:
                resultado = math.cos(a)
            elif opcion == 11:
                resultado = math.tan(a)
        else:
            print("Opción no válida.")
            continue

        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora_cientifica()
