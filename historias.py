import random

personajes = ['un astronauta', 'un mago', 'un chef', 'una modelo']
escenarios = ['en un castillo', 'en marte', 'en un bar', 'en una ciudad futurista']
problemas = ['ha perdido un objeto valioso', 'se encuentra en un lugra misterioso', 'se encuentra un objeto valioso']
soluciones = ['encuentra el objeto valioso', 'sale del lugar misterioso', 'resuleven el acertijo']

def generar_historia():
    personaje = random.choice(personajes)
    escenario = random.choice(escenarios)
    problema = random.choice(problemas)
    solucion = random.choice(soluciones)

    #construyendo la historia
    historia = f"{personaje} {escenario} {problema} {solucion}"
    return historia
print(generar_historia())