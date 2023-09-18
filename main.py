import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Triángulo Móvil')

# Colores
black = (0, 0, 0)
triangle_color = (0, 159, 255)  # Color azul (#009FFF)

# Triángulo
triangle_base = 60
triangle_height = 100  # Hacer un vértice más largo
triangle_x = (width - triangle_base) // 2
triangle_y = (height - triangle_height) // 2
triangle_speed = 5
triangle_angle = 0
triangle_rotation_speed = 5

# Variables de inercia
inertia = 0.95
inertia_speed_x = 0
inertia_speed_y = 0

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
        triangle_speed_x = math.cos(math.radians(triangle_angle - 90)) * triangle_speed
        triangle_speed_y = -math.sin(math.radians(triangle_angle - 90)) * triangle_speed
        triangle_x += triangle_speed_x
        triangle_y += triangle_speed_y
    if keys[pygame.K_UP]:
        triangle_speed_x = -math.cos(math.radians(triangle_angle - 90)) * triangle_speed
        triangle_speed_y = math.sin(math.radians(triangle_angle - 90)) * triangle_speed
        triangle_x += triangle_speed_x
        triangle_y += triangle_speed_y

    # Movimiento lateral izquierdo y derecho
    if keys[pygame.K_LEFT]:
        triangle_angle += triangle_rotation_speed
    if keys[pygame.K_RIGHT]:
        triangle_angle -= triangle_rotation_speed

    # Actualizar la inercia
    inertia_speed_x *= inertia
    inertia_speed_y *= inertia
    triangle_x += inertia_speed_x
    triangle_y += inertia_speed_y

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
