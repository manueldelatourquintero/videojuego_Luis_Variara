#importando módulos
import pygame, sys
from pygame.surface import *
from pygame import *
from pygame_colliders import *
from random import *
import random

#inicializar librería Pygame
pygame.init()

#Configurando tamaño pantalla
W, H = 1000, 600
FPS = 60
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

#titulo de la ventana
pygame.display.set_caption("Luis Variara in Action")

#icono de la ventana
icono = pygame.image.load("./resources/img/icon.jpeg").convert()
pygame.display.set_icon(icono)

#Constantes
AZUL = (0, 0, 255)

#color de fondo pantalla
#PANTALLA.fill(AZUL)

pygame.display.flip()

#Fondo del juego
fondo = pygame.image.load("resources/img/background.jpg").convert()
rectanguloFondo = fondo.get_rect()
rectanguloFondo.left = 950
rectanguloFondo.top = 500

#personaje
personaje = pygame.image.load("resources/img/padreluisvariara-edit4.png").convert()
personaje.set_colorkey([0, 0, 0])
rectanguloPersonaje = personaje.get_rect()
rectanguloPersonaje.left = 200
rectanguloPersonaje.top = 400

#obstaculos
obstaculo = pygame.image.load("resources/img/obstaculo4.png")
obstaculo.set_colorkey([0,0,0])


coord_x=200
coord_y=400
x_speed=0
y_speed=0

isJump = False
salto=10

x2 = 50

px=50
py=200
ancho=48
velocidad=0

#variables dirección
izquierda = False
derecha = False

camara_x = 0
x=0

#pasos
cuentaPasos = 0

#Movimiento
def recargaPantalla():
    #Variables Globales
    global cuentaPasos
    global x    
    x_relativa = x % fondo.get_rect().width
    PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < W:
        PANTALLA.blit(fondo, (x_relativa, 0))
    x -= 5

    if x_relativa < W:
        PANTALLA.blit(obstaculo, (x_relativa, 430))
        PANTALLA.blit(obstaculo, [x_relativa, 430])
    x -= 10


#Bucle Principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    RELOJ.tick(FPS)


     #Eventos Teclado
    pulsada = pygame.key.get_pressed()

    if pulsada[K_LEFT]:
        coord_x -= 5
    if pulsada[K_RIGHT]:
        coord_x += 5

    PANTALLA.blit(personaje, [coord_x, coord_y])

    #salto personaje
    if pulsada[K_SPACE]:
        isJump=True

    if pulsada[K_UP]:
        isJump=True


    if isJump==False:
        if salto >= -10:
            coord_y -= (salto * abs(salto)) *0.5
            salto -= 1
    else:
        salto = 10
        isJump = False
    

    #collide = pygame.Rect.colliderect(rectanguloFondo, rectanguloPersonaje)

    #PANTALLA.blit(obstaculo, [700, 200])
    

    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

#Salida del juego
pygame.quit() 