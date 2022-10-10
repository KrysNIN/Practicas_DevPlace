# Algoritmo para cálculo de sueldos.

# Solicitud de entrada de datos para el usuario.
nombre = input("\nIngrese el Nombre del Empleado: ")
años = int(input("\nIngrese los Años de Antiguedad del Empleado: "))
horas = int(input("\nIngrese la Cantidad de Horas Trabajadas: "))
valor = float(input("\nIngrese el Valor Hora: "))

# Control de flujo que definira el sueldo del empleado.
if años > 10:
    sueldo = horas * valor    
    antiguedad = sueldo * años * 30 

    print()
    print(nombre)
    print("\nAntiguedad: " + str(años))
    print("\nTotal de Horas Trabajadas: " + str(horas))
    print("\nSueldo a Cobrar por Antiguedad: $" + str(antiguedad))
    print()

# Si no se cumple la condición del control de flujo, se ejecutará este segmento del código.
else:
    # La variable "sueldo", ya no se multiplica por antiguedad.
    sueldo = horas * valor
    print()
    print(nombre)
    print("\nAntiguedad: " + str(años))
    print("Total de Horas Trabajadas: " + str(horas))
    print("Sueldo a Cobrar por Antiguedad: $" + str(sueldo))
    print()