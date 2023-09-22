import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Triángulo en Pantalla Circular')

# Colores
black = (0, 0, 0)
triangle_color = (0, 159, 255)  # Color azul (#009FFF)

# Triángulo
triangle_base = 60
triangle_height = 100  # Hacer un vértice más largo
triangle_x = (width - triangle_base) // 2
triangle_y = (height - triangle_height) // 2
triangle_speed = 0.2
triangle_angle = 0
triangle_rotation_speed = 5

# Variables de fricción
friction = 0.995  # Fricción normal (menos deslizamiento)
slippery_friction = 0.99  # Fricción reducida para simular hielo (más deslizamiento)
current_friction = friction

# Velocidades
triangle_speed_x = 0
triangle_speed_y = 0

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detectar teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento hacia adelante y hacia atrás (inverso)
    if keys[pygame.K_DOWN]:
        triangle_speed_x += math.cos(math.radians(triangle_angle - 90)) * triangle_speed
        triangle_speed_y += -math.sin(math.radians(triangle_angle - 90)) * triangle_speed
    if keys[pygame.K_UP]:
        triangle_speed_x += -math.cos(math.radians(triangle_angle - 90)) * triangle_speed
        triangle_speed_y += math.sin(math.radians(triangle_angle - 90)) * triangle_speed

    # Movimiento lateral izquierdo y derecho
    if keys[pygame.K_LEFT]:
        triangle_angle += triangle_rotation_speed
    if keys[pygame.K_RIGHT]:
        triangle_angle -= triangle_rotation_speed

    # Aplicar fricción
    triangle_speed_x *= current_friction
    triangle_speed_y *= current_friction

    # Actualizar posición
    triangle_x += triangle_speed_x
    triangle_y += triangle_speed_y

    # Cambiar fricción según si las teclas están presionadas
    if any(keys):
        current_friction = slippery_friction
    else:
        current_friction = friction

    # Verificar si el triángulo sale de la pantalla y reposicionarlo en el lado opuesto
    if triangle_x > width:
        triangle_x = 0
    elif triangle_x < 0:
        triangle_x = width
    if triangle_y > height:
        triangle_y = 0
    elif triangle_y < 0:
        triangle_y = height

    # Dibujar el fondo
    screen.fill(black)

    # Dibujar el triángulo (vértice principal más largo) en el color azul
    triangle = pygame.Surface((triangle_base, triangle_height), pygame.SRCALPHA)
    pygame.draw.polygon(triangle, triangle_color, [(0, triangle_height), (triangle_base, triangle_height), (triangle_base / 2, 0)])
    triangle = pygame.transform.rotate(triangle, triangle_angle)
    triangle_rect = triangle.get_rect(center=(triangle_x, triangle_y))
    screen.blit(triangle, triangle_rect)

    pygame.display.flip()

    pygame.time.delay(10)

# Salir del juego
pygame.quit()
sys.exit()
