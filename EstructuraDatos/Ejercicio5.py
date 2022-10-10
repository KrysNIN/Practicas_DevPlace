# Algoritmo para identificar Números.

# Se define la variable numeros como una lista.
numeros = []
# Se define la variable dato como vacia.
dato = ()

# Bucle que se ejecutará mientras que el valor de la variable "Dato", sea distinto a -1.
while dato != -1:
    
    # Se le pide el ingreso del dato al usuario.
    dato = int(input("\nIngrese un Número: "))

    # Cuando el usuario ingresa el dato, se almacena en la lista numeros.
    numeros.append(dato)

    # Cuando el valor de la variable dato sea igual a -1, se ejecutaran los outputs.
    if dato == -1:
        print("\nMayor Numero introducido: "+str(max(numeros)))
        print("\nMenor Número introducido: "+str(min(numeros)))
        print("\nLa suma de los numeros es: "+str(sum(numeros)))        
        print("\nCantidad de Numeros: "+str(len(numeros)))
        print()
        