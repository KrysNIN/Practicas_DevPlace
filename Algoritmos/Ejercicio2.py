# Algoritmo con 3 intentos para ingresar contraseña.

# Se importa la funcion "getch" para la salida del programa.
from msvcrt import getch

# Inicio del programa
print("\nHay tres intentos disponibles para introducir la contraseña: ")

# Se define el valor inicial de la variable "contador".
contador = 1

# Input para que el usuario ingrese su contraseña.
contraseña = input("\nIngrese una contraseña: ")

# Bucle que se ejecutara, mientras que la variable "contador", sea menor a 3.
while contador <= 3:
    valor = input("\nIngrese nuevamente la contraseña: ")

    # Estructura de control de flujo que define la salida del programa dentro del bucle while.
    if valor == contraseña:
        print("\nFelicitaciones!, recordaste tu constraseña.")
        print()
        break    
    else:
        contador = contador + 1
        print("\nLa contraseña es incorrecta.")

# Control de flujo que define el output, si la variable "contador" es mayor a 3.        
if contador > 3:
    print("\nTenes que ejercitar tu memoria.")
    input("\nPresione cualquier tecla para finalizar...")
    getch
    