'''
Porgrama para generar numeros aleatorios usando las librerias 
numpy y matplotlib.
Creado por: Omar Chanel Ali Fuertes
'''

import numpy as np
import matplotlib.pyplot as plt

# Menu de opciones
def mostrar_menu():
    print('GENERADOR DE NUMEROS ALEATORIOS')
    print('-------------------------------')
    print('1. Generar numeros aleatorios')
    print('2. Generar matrtiz de numeros aleatorios')
    print('3. Calcular estadisticas de un conjunto de numeros')
    print('4. Visualizar distribucion de numeros aleatorios')
    print('5. Salir')

# Generar numeros aleatorios
def generar_numeros_aleatorios():
    cantidad = int(input('Ingrese la cantidad de numeros aleatorios que desea generar: '))
    minimo = int(input('Ingrese el minimo del rango de numeros aleatorios: '))
    maximo = int(input('Ingrese el maximo del rango de numeros aleatorios: '))
    numeros = np.random.uniform(minimo, maximo, cantidad)
    print(f'Numeros aleatorios generados: \n', numeros)
    return numeros

# Generar matriz de numeros aleatorios
def generar_matriz_aleatoria():
    filas = int(input('Ingrese la cantidad de filas de la matriz: '))
    columnas = int(input('Ingrese la cantidad de columnas de la matriz: '))
    minimo = int(input('Ingrese el minimo del rango de numeros aleatorios: '))
    maximo = int(input('Ingrese el maximo del rango de numeros aleatorios: '))
    matriz = np.random.uniform(minimo, maximo, (filas, columnas))
    print(f'Matriz de numeros aleatorios generada: \n', matriz)
    return matriz

# Calcular estadisticas de un conjunto de numeros
def calcular_estadisticas(numeros):
    if numeros is None or len(numeros) == 0:
        print('No se han ingresado numeros')
        return
    media = np.mean(numeros)
    mediana = np.median(numeros)
    desviacion_standard = np.std(numeros)
    varianza = np.var(numeros)
    maximo = np.max(numeros)
    minimo = np.min(numeros)
    print("\n Estadisticas de numeros aleatorios:\n")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviacion estandar: {desviacion_standard}")
    print(f"Varianza: {varianza}")
    print(f"Maximo: {maximo}")
    print(f"Minimo: {minimo}")

# Visualizar distribucion de numeros aleatorios
def visualizar_distribucion(numeros):
    if numeros is None or len(numeros) == 0:
        print('No se han ingresado numeros')
        return
    plt.hist(numeros, bins=20, color='blue', edgecolor='black')
    plt.title('Distribucion de numeros aleatorios')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

def main():
    numeros_generados = None  # Alamacena de numeros generados para su posterior uso
    while True:
        mostrar_menu()
        opcion = int(input('Ingrese la opcion deseada: '))
        if opcion == 1:
            numeros_generados = generar_numeros_aleatorios()
        elif opcion == 2:
            numeros_generados = generar_matriz_aleatoria()
        elif opcion == 3:
            calcular_estadisticas(numeros_generados)
        elif opcion == 4:
            visualizar_distribucion(numeros_generados)
        elif opcion == 5:
            break
        else:
            print('Opcion invalida')
    print('Saliendo del programa...')

if __name__ == '__main__':
    main()