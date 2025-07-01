'''
Porgrama para simular el movimiento de particulas en un espacio.
Creado por: Omar Chanel Ali Fuertes
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# configuracion inicial
NUM_PARTICLES = 100   # numero de particulas
SPACE_SIZE = 10      # tamano del espacio
TIME_STEPS = 200     # numero de pasos de tiempo
DT = 0.1            # paso de tiempo
GRAVITY = np.array([0, -0.05])   # aceleracion de gravedad
REPULSION_CONSTANT = 1        # constante de repulsion

# Inicializacion de las particulas
np.random.seed(42)
positions = np.random.uniform(-SPACE_SIZE/2, SPACE_SIZE/2, (NUM_PARTICLES, 2))  # posiciones iniciales
velocities = np.random.uniform(-0.5, 0.5, (NUM_PARTICLES, 2))  # velocidades iniciales

# Funcion para aplicar condiciones de contorno reflexivas
def apply_boundary_conditions(positions, velocities, space_size):
    # Se Aplica la condicion de contorno reflexivo en las direcciones x y y
    for i in range(len(positions)):
        if positions[i, 0] < 0 or positions[i, 0] > space_size:
            velocities[i, 0] = -velocities[i, 0]
        if positions[i, 1] < 0 or positions[i, 1] > space_size:
            velocities[i, 1] = -velocities[i, 1]
    return positions, velocities

# Funcion para aplicar la repulsion entre particulas
def calculate_repulsion_forces(positions):
    # Calcular la fuerza de repulsion entre particulas
    forces = np.zeros_like(positions)
    for i in range(NUM_PARTICLES):
        for j in range(i+1, NUM_PARTICLES):
            r = positions[i] - positions[j]
            distance = np.linalg.norm(r)
            if distance > 0.1:  # Añadido umbral mínimo para evitar fuerzas infinitas
                force_magnitude = REPULSION_CONSTANT / distance**2
                force_direction = r / distance
                forces[i] += force_magnitude * force_direction
                forces[j] -= force_magnitude * force_direction
    return forces

# Funciones para actualizar las posiciones y velocidades de las particulas
def update_positions_and_velocities(positions, velocities, dt, gravity):
    # Clacular las fuerzas de repulsion
    repulsion_forces = calculate_repulsion_forces(positions)

    #actualizar velocidades (gravedad + repulsion)
    velocities += dt * gravity + dt * repulsion_forces

    # Actualizar las posiciones
    positions += dt * velocities

    #aplicar condiciones de contorno reflexivo
    positions, velocities = apply_boundary_conditions(positions, velocities, SPACE_SIZE)
    return positions, velocities

# configuracion de la animacion
fig, ax = plt.subplots(figsize=(6, 6))
scat = ax.scatter(positions[:, 0], positions[:, 1], color= "blue", s=50)
ax.set_xlim(-SPACE_SIZE, SPACE_SIZE)
ax.set_ylim(-SPACE_SIZE, SPACE_SIZE)
ax.set_aspect('equal', adjustable='box')
ax.set_title('Simulacion del Movimiento de particulas')
ax.set_xlabel('Posicion X')
ax.set_ylabel('Posicion Y')

# Funcion para actualizar la animacion

def update(frame):
    global positions, velocities
    positions, velocities = update_positions_and_velocities(positions, velocities, DT, GRAVITY)
    scat.set_offsets(positions)
    return scat,

# Crear la animacion
ani = FuncAnimation(fig, update, frames=TIME_STEPS, interval=50, blit=True)
plt.show()