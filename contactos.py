# Programa para crear una lista de contactos 
# y guardar la informacion en un archivo json
# Creado por: Omar Chanel Ali Fuertes

import json
import os
from datetime import datetime
import re
from turtle import Terminator

#Ruta del archivo para guardar contactos
CONTACTS_FILE = "contactos.json"

def validar_email(email):
    """Valida un email usando una expresion regular"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def cargar_contactos():
    """Carga los contactos desde el archivo json si existe"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return[]
    return []

def guardar_contactos(contactos):
    """Guarda los contactos en el archivo json"""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contactos, file, indent=4)

def agregar_contacto(contactos):
    """Agrega un contacto a la lista de contactos"""
    nombre = input("Ingrese un nombre: ").strip()
    while not nombre:
        print("El nombre no puede estar vacio")
    
    email = input("Ingrese un email: ").strip()
    while not validar_email(email):
        print("El email no es valido")

    telefono = input("Ingrese un telefono: ").strip()
    while not telefono:
        print("El telefono no puede estar vacio")

    contacto = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "fecha": datetime.now().strftime("%d/%m/%Y")
    }
    contactos.append(contacto)
    guardar_contactos(contactos)
    print(f"Contacto {nombre} agregado con exito")

def buscar_contacto(contactos):
    """Busca un contacto en la lista de contactos"""
    termino = input("Ingrese un nombre o email a buscar: ").strip()
    resultados = [c for c in contactos if termino in c["nombre"] or termino in c["email"]]
    if not resultados:
        print("No se encontro ningun contacto con ese nombre o email")
        return
    
    for i, contacto in enumerate(resultados, 1):
        print(f"Contacto {i}: ")
        print(f"Nombre: {contacto['nombre']}")
        print(f"Email: {contacto['email']}")
        print(f"Telefono: {contacto['telefono']}")
        print(f"Fecha: {contacto['fecha']}")

def main():
    """Programa principal"""
    contactos = cargar_contactos()

    while True:
        print("Agenda de contactos")
        print("------------------")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Salir")

        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion == 1:
            agregar_contacto(contactos)
        elif opcion == 2:
            buscar_contacto(contactos)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()