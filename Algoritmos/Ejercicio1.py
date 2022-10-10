# Algoritmo para números primos.

# Se genera el input en el que el usuario ingresa el número.
print()
n = int(input("Ingresa un Número: "))
a = 1
b = 0

# Se ejecuta el bucle mientras se cumpla la condición.
while a <= n:
    if n % a == 0:
        b = b + 1
    a = a + 1
    
# Estructura de control de flujo que define el output.
if b == 2:
    print()
    print("El Número", n,"es Primo")
    print()
else:
    print()
    print("El Número", n,"NO es Primo")
    print()