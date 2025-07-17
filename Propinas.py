# Programa para calcular propinas
# Autor: Omar Ali Fuertes

def calcular_propina():
    print("=== CALCULADORA DE PROPINAS ===")

    # Paso 1: Obtener el montototal de la cuenta
    while True:
        try:
            monto_total = float(input("Ingrese el monto total de la cuenta: "))
            if monto_total < 0:
                print("El monto total no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente de nuevo.")

    # Paso 2: Obtener el porcentaje de propina
    while True:
        try:
            porcentaje_propina = float(input("Ingrese el porcentaje de propina (ejemplo: 15 para 15%): "))
            if porcentaje_propina < 0:
                print("El porcentaje de propina no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Intente de nuevo.")

    # Paso 3: Calcular la propina y el total a pagar
    propina = monto_total * (porcentaje_propina / 100)
    total_a_pagar = monto_total + propina

    # Paso 4: Mostrar los resultados
    print("\n=== RESULTADOS ===")
    print(f"Monto total de la cuenta: ${monto_total:.2f}")
    print(f"Porcentaje de propina: {porcentaje_propina:.2f}%")
    print(f"Propina: ${propina:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")

# Llamar a la función principal
if __name__ == "__main__":
    calcular_propina()

        