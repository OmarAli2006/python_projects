# Porgrama para el analisis de la deflexion de vigas
# Creado por: Omar Chanel Ali Fuertes

import numpy as np
import matplotlib.pyplot as plt

def cargar_parametros():
    """ Solicita los parametros de la viga al usuario con validación de entrada. """
    print("Ingrese los parametros de la viga:")
    while True:
        try:
            L = float(input("Ingrese la longitud de la viga (m): "))
            if L <= 0: raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número positivo para la longitud.")
    
    while True:
        try:
            E = float(input("Ingrese el módulo de elasticidad (Pa): "))
            if E <= 0: raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número positivo para la elasticidad.")

    while True:
        try:
            I = float(input("Ingrese el momento de inercia (m^4): "))
            if I <= 0: raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número positivo para la inercia.")

    while True:
        try:
            n = int(input("Ingrese el número de puntos discretos (mínimo 3): "))
            if n < 3: raise ValueError
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero mayor o igual a 3.")

    while True:
        tipo_carga = input("Tipo de Carga (uniforme/no_uniforme): ").strip().lower()
        if tipo_carga in ["uniforme", "no_uniforme"]:
            break
        else:
            print("Tipo de carga no reconocido. Por favor, ingrese 'uniforme' o 'no_uniforme'.")

    while True:
        tipo_apoyo = input("Tipo de Apoyo (simplemente_apoyado/empotrado): ").strip().lower()
        if tipo_apoyo in ["simplemente_apoyado", "empotrado"]:
            break
        else:
            print("Tipo de apoyo no reconocido. Por favor, ingrese 'simplemente_apoyado' o 'empotrado'.")

    return L, E, I, n, tipo_carga, tipo_apoyo

def calcular_carga(L, tipo_carga, n):
    """ Calcula la carga distribuida en función del tipo. """
    x = np.linspace(0, L, n)
    if tipo_carga == "uniforme":
        q = -1000.0  # Carga constante (N/m)
        q_x = np.full(n, q)
    elif tipo_carga == "no_uniforme":
        q_0 = -1000.0  # Amplitud de la carga sinusoidal
        q_x = q_0 * np.sin(2 * np.pi * x / L)
    else:
        # Esto no debería ocurrir si la validación de entrada funciona correctamente
        raise ValueError("Tipo de carga no reconocido")
    return q_x, x

def aplicar_condiciones_de_frontera(A, b, tipo_apoyo, n, dx, E, I):
    """ Aplica las condiciones de frontera según el tipo de apoyo. """
    if tipo_apoyo == "simplemente_apoyado":
        # Deflexión cero en los extremos: w(0) = 0 y w(L) = 0
        A[0, :] = 0
        A[0, 0] = 1
        b[0] = 0

        A[n-1, :] = 0
        A[n-1, n-1] = 1
        b[n-1] = 0

    elif tipo_apoyo == "empotrado":
        # Deflexión cero y pendiente cero en los extremos: w(0)=0, w'(0)=0, w(L)=0, w'(L)=0
        # w(0) = 0
        A[0, :] = 0
        A[0, 0] = 1
        b[0] = 0

        # w'(0) = 0 (aproximación de diferencia central: (w[1] - w[-1]) / (2*dx) = 0 => w[1] = w[-1])
        # Para el primer punto, w'(0) = 0 se aproxima como w[1] - w[0] = 0, o w[1] = w[0]
        # Sin embargo, para la ecuación de diferencias finitas, se usa una aproximación de segundo orden
        # w'(0) = (-3w[0] + 4w[1] - w[2]) / (2*dx) = 0 => -3w[0] + 4w[1] - w[2] = 0
        A[1, :] = 0 # Sobreescribimos la fila 1 que corresponde a la segunda ecuación de diferencias finitas
        A[1, 0] = -3
        A[1, 1] = 4
        A[1, 2] = -1
        b[1] = 0

        # w(L) = 0
        A[n-1, :] = 0
        A[n-1, n-1] = 1
        b[n-1] = 0

        # w'(L) = 0 (aproximación de diferencia central: (w[n-1] - w[n-3]) / (2*dx) = 0 => w[n-1] = w[n-3])
        # w'(L) = (3w[n-1] - 4w[n-2] + w[n-3]) / (2*dx) = 0 => 3w[n-1] - 4w[n-2] + w[n-3] = 0
        A[n-2, :] = 0 # Sobreescribimos la penúltima fila
        A[n-2, n-3] = 1
        A[n-2, n-2] = -4
        A[n-2, n-1] = 3
        b[n-2] = 0

    else:
        # Esto no debería ocurrir si la validación de entrada funciona correctamente
        raise ValueError("Tipo de apoyo no reconocido")

def calcular_momento_y_cortante(w, dx, E, I):
    """ Calcula el momento flector (M) y el esfuerzo cortante (V) a partir de la deflexión. """
    # Segunda derivada de la deflexión (d2w/dx2)
    # np.gradient calcula la derivada usando diferencias finitas
    d2w_dx2 = np.gradient(np.gradient(w, dx), dx)
    M = E * I * d2w_dx2
    
    # Primera derivada del momento flector (dV/dx = -q, dM/dx = V)
    V = np.gradient(M, dx)
    return M, V

def main():
    # Solicitar parametros al usuario
    L, E, I, n, tipo_carga, tipo_apoyo = cargar_parametros()

    # Discretizacion del dominio
    dx = L / (n - 1)
    x, qx = calcular_carga(L, tipo_carga, n)

    # Construcción de la matriz de coeficientes (A) y el vector de términos independientes (b)
    # para la ecuación diferencial de la viga: E*I*d4w/dx4 = q(x)
    # Usando diferencias finitas de segundo orden para la cuarta derivada:
    # w'''' approx (w[i-2] - 4w[i-1] + 6w[i] - 4w[i+1] + w[i+2]) / dx^4
    # Sin embargo, el código original usa una aproximación para d2w/dx2 = qx / (E*I)
    # que es más común para problemas de deflexión donde se integra dos veces.
    # El enfoque actual resuelve d2w/dx2 = M/(EI) y luego integra dos veces.
    # El código original parece estar resolviendo d2w/dx2 = qx / (E*I) con condiciones de frontera.
    # Vamos a mantener la estructura original y corregir las condiciones de frontera.
    
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Llenar la matriz A y el vector b para las ecuaciones internas
    # E*I * (w[i-1] - 2w[i] + w[i+1]) / dx^2 = M_i (aproximación de la segunda derivada)
    # Si estamos resolviendo d2w/dx2 = qx / (E*I), entonces:
    # (w[i-1] - 2w[i] + w[i+1]) / dx^2 = qx[i] / (E*I)
    # w[i-1] - 2w[i] + w[i+1] = qx[i] * dx^2 / (E*I)
    for i in range(1, n - 1):
        A[i, i-1] = 1
        A[i, i] = -2
        A[i, i+1] = 1
        b[i] = qx[i] * dx**2 / (E * I)

    # Aplicar condiciones de frontera
    aplicar_condiciones_de_frontera(A, b, tipo_apoyo, n, dx, E, I)

    # Resolver el sistema lineal para obtener la deflexión (w)
    try:
        w = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        print(f"Error al resolver el sistema lineal: {e}")
        print("Asegúrese de que las condiciones de frontera y el número de puntos sean adecuados.")
        return

    # Calcular el momento flector y el esfuerzo cortante
    M, V = calcular_momento_y_cortante(w, dx, E, I)

    # Visualizar los resultados
    plt.figure(figsize=(12, 10))

    # Gráfico de Deflexión
    plt.subplot(3, 1, 1)
    plt.plot(x, w, label="Deflexión w(x)", color="blue")
    plt.title("Deflexión de la Viga")
    plt.xlabel("Posición (m)")
    plt.ylabel("Deflexión (m)")
    plt.grid(True)
    plt.legend()

    # Gráfico de Momento Flector
    plt.subplot(3, 1, 2)
    plt.plot(x, M, label="Momento Flector M(x)", color="green")
    plt.title("Momento Flector")
    plt.xlabel("Posición (m)")
    plt.ylabel("Momento Flector (N.m)")
    plt.grid(True)
    plt.legend()

    # Gráfico de Esfuerzo Cortante
    plt.subplot(3, 1, 3)
    plt.plot(x, V, label="Esfuerzo Cortante V(x)", color="red")
    plt.title("Esfuerzo Cortante")
    plt.xlabel("Posición (m)")
    plt.ylabel("Fuerza (N)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()