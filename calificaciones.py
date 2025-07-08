# Programa par ael registro de etsudiantes y calificaciones
# usando diccionarios
# Creado por: Omar Chanel Ali Fuertes

import json

ARCHIVO_JSON = 'estudiantes.json'

estudiantes = {}

def cargar_estudiantes():
    global estudiantes
    try:
        with open(ARCHIVO_JSON, 'r') as f:
            estudiantes = json.load(f)
        print("Datos de estudiantes cargados exitosamente.")
    except FileNotFoundError:
        print("Archivo de estudiantes no encontrado. Se creará uno nuevo.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Se iniciará con datos vacíos.")
        estudiantes = {}

def guardar_estudiantes():
    try:
        with open(ARCHIVO_JSON, 'w') as f:
            json.dump(estudiantes, f, indent=4)
        print("Datos de estudiantes guardados exitosamente.")
    except IOError:
        print("Error al guardar los datos de estudiantes.")

def registrar_estudiante():
    """  Registra un nuevo alumno """
    try:
        id_estudiante = int(input("Ingrese el id del estudiante: "))
        if id_estudiante in estudiantes:
            print("El estudiante ya existe")
            return
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        calificaciones_str = input("Ingrese las calificaciones separadas por una coma (ej. 7.5,8,9.2): ")
        calificaciones = [float(c.strip()) for c in calificaciones_str.split(',') if c.strip()]

        # Guardar los datos del estudiante en el diccionario
        estudiantes[id_estudiante] = {
            "nombre": nombre,
            "edad": edad,
            "calificaciones": calificaciones
        }

        print(f"Estudiante {nombre} registrado con exito")
        guardar_estudiantes() # Guardar después de registrar
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números para ID, edad y calificaciones.")

def consultar_estudiante():
    """ Consultar la informacion de un estudiante """
    try:
        id_estudiante = int(input("Ingrese el id del estudiante: "))
        estudiante = estudiantes.get(id_estudiante)

        if not estudiante:
            print("Estudiante no encontrado")
            return

        print(f"Estudiante: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Calificaciones: {', '.join(map(str, estudiante['calificaciones']))}")
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar un número para el ID.")

def actualizar_calificaciones():
    """ Actualizar las calificaciones de un estudiante """
    try:
        id_estudiante = int(input("Ingrese el id del estudiante: "))
        estudiante = estudiantes.get(id_estudiante)

        if not estudiante:
            print("Estudiante no encontrado")
            return

        calificaciones_str = input("Ingrese las nuevas calificaciones separadas por una coma (ej. 7.5,8,9.2): ")
        calificaciones = [float(c.strip()) for c in calificaciones_str.split(',') if c.strip()]
        estudiantes[id_estudiante]["calificaciones"] = calificaciones
        print(f"Calificaciones actualizadas con exito para {estudiante['nombre']}")
        guardar_estudiantes() # Guardar después de actualizar
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números para el ID y las calificaciones.")

def mostrar_estudiantes():
    """ Mostrar todos los estudiantes registrados """
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    
    print("Estudiantes registrados:")
    for id_estudiante, estudiante in estudiantes.items():
        print(f"ID: {id_estudiante}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Calificaciones: {', '.join(map(str, estudiante['calificaciones']))}")
        print("-" * 30)

def menu():
    """ Menú principal """
    while True:
        print("\nMENÚ DE ESTUDIANTES")
        print("-------------------")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Actualizar calificaciones")
        print("4. Mostrar estudiantes")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese la opcion deseada: "))
            if opcion == 1:
                registrar_estudiante()
            elif opcion == 2:
                consultar_estudiante()
            elif opcion == 3:
                actualizar_calificaciones()
            elif opcion == 4:
                mostrar_estudiantes()
            elif opcion == 5:
                print("Saliendo del programa...")
                guardar_estudiantes() # Guardar antes de salir
                break
            else:
                print("Opcion invalida. Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    cargar_estudiantes() # Cargar datos al iniciar
    menu()

