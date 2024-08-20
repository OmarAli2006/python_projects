import string
import random

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(longitud):
        password += random.choice(caracteres)
    return password

longitud = int(input("Ingrese el tamanio de la contrasenia a generar: "))

nuevo_password = generar_password(longitud)
print("Su nueva contarseña es: " + nuevo_password) 