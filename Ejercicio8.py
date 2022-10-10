# Se define la funcion
def sumar_lista(lista):  
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumar_lista(lista[1:])

# Se crea la lista de numeros a sumar.
numeros = [1, 2, 3, 4, 5]
# Se define la variable resultado, llamando a la función, con el parametro "numeros".
resultado = sumar_lista(numeros)

print ("La suma de los valores de 1 a 5 es igual a: " + str(resultado))
