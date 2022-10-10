# Algoritmo para Adivinar el Número.

# Se importa la funcion random para la generación aleatoria.
import random

# Definición de la variable.
intentos = 0

# Entrada de datos de usuario.
print("\nHola!, como te llamas?")
print()
nombre = input()

# Se define que la variable numero, va a iterar de 0 a 1000.
numero = random.randint (0,1000)

print("\nMuy bien, "+nombre+", estoy pensando...en un número entre 1 y 1000.")

# Bucle while, que se ejecutará mientras la variable intentos sea menor a 1000.
while intentos < 1000:

    print("\nIntenta Adivinar!")
    print()
    estimacion = input()
    estimacion = int(estimacion)

    intentos = intentos + 1

    if estimacion < numero:
        print("\nEste numero es Menor al que estoy pensando")
    
    if estimacion > numero:
        print("\nEste número es Mayor al que estoy pensando")
    
    if estimacion == numero:
        break

if estimacion == numero:
    intentos = str(intentos)
    print("\nMuy bien!, "+nombre+", adivinaste el numero en: "+intentos+"intentos!")

if estimacion != numero:    
    numero = str(numero)
    print("\nEl número en el que pensaba era el: "+numero)
    print()