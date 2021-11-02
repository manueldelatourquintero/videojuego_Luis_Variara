#importando módulos
import pygame, sys
from pygame.surface import *
from pygame import *
from random import *
import random
from pygame.locals import *

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

bright_green = (0,255,0)
black = (0,0,0)
#pantalla ver valores
valores = pygame.image.load("resources/backgrounds/los_valores.png")

#main menu
main_menu = pygame.image.load("resources/backgrounds/main_menu.png")
main_menu.set_colorkey([0,0,0])
clock = pygame.time.Clock()
counter, text = 50, '50'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 5000)
font = pygame.font.SysFont('Consolas', 30)
#font2 = pygame.font.SysFont(Arial, 70)

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

clock = pygame.time.Clock()
counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

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

def game():
    global isJump
    global salto
    global coord_x
    global coord_y
    global text
    global pulsada
    global counter

    #Eventos Teclado
    pulsada = pygame.key.get_pressed()

    if pulsada[K_v]:
        PANTALLA.blit(valores, [0,0])

    if pulsada[K_ESCAPE]:
        pygame.quit()
        sys.exit()

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
    
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'Press Key "V" '
        if e.type == pygame.QUIT: break
    else:
        PANTALLA.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
   
    #collide = pygame.Rect.colliderect(rectanguloFondo, rectanguloPersonaje)

    #PANTALLA.blit(obstaculo, [700, 200])
    

    pygame.display.update()
    #Llamada a la función de actualización de la ventana
    recargaPantalla()

def gameMenu():
    global pulsada
    global intro
    
    pulsada = pygame.key.get_pressed()

    intro = True

    while intro==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    print(1+1)
                    intro=False
                    game()            

        PANTALLA.blit(main_menu, [0,0])

        mouse = pygame.mouse.get_pos()
        #print(mouse)

        #condicion mouse 
        #if 400+150 > mouse[0] > 400 and 530+190 > mouse[1] > 150:
            #pygame.draw.rect(PANTALLA, bright_green, (400,150, 530, 190))
        #else:
            #pygame.draw.rect(PANTALLA, (255,255,255), (400,150, 530, 190))

        #pygame.draw.rect(PANTALLA, (255, 255, 255), [400, 450, 530, 70]) 
        pygame.display.update()
        RELOJ.tick(FPS)
    while intro==False:
        game()

#Bucle Principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    RELOJ.tick(FPS)

    pygame.display.update()

    gameMenu()    
    game()
#Salida del juego
pygame.quit() 


if __name__ == '__main__':
    print("Hola mundo")