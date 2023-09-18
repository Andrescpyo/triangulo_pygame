import pygame
import math

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definir el tamaño de la pantalla
ANCHO = 800
ALTO = 600

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Crear el triángulo
triangulo = pygame.draw.polygon(pantalla, ROJO, ((100, 100), (200, 200), (300, 100)))

# Definir la velocidad del triángulo
velocidad = 10

# Definir el ángulo del triángulo
angulo = 0

# Crear el bucle principal
while True:

    # Comprobar si el usuario ha pulsado alguna tecla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocidad += 1
            elif event.key == pygame.K_DOWN:
                velocidad -= 1
            elif event.key == pygame.K_LEFT:
                angulo -= 1
            elif event.key == pygame.K_RIGHT:
                angulo += 1

    # Mover el triángulo
    triangulo.move_ip(velocidad * math.cos(angulo), velocidad * math.sin(angulo))

    # Dibujar el triángulo
    pygame.draw.polygon(pantalla, ROJO, ((100, 100), (200, 200), (300, 100)))

    # Actualizar la pantalla
    pygame.display.update()