def funcion():
    # Se define una variable contador.
    contador = 0

    # Se crea un array con los números.
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # El bucle while se ejecuta mientras el contador sea menor a 5:
    while contador < 5: 

        # Ingreso de datos.
        dato = int(input("Ingrese un Número del 0 al 9: "))
        # Por cada iteracion de bucle, el contador sumara 1.
        contador = contador + 1

        # El bucle for recorrerá el array hasta encontrar el patron.
        for i in array:
            if dato == i:
                array.remove(i)     
        
        # Cuando el contador llega a 5, se imprime el contenido del array.
        if contador == 5:
            print (array)
# Se llama a la funcion.
funcion()