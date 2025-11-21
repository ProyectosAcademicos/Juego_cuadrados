#Acá se crea el enemigo del juego
#Importamos la librería pygame
import pygame

#El enemigo también será un cubo
class Enemigo:
    def __init__(self,x,y):
        #Comenzamos a configurar las posiciones iniciales y dimensiones
        self.x=x
        self.y=y
        self.ancho = 200
        self.alto = 50
        self.velocidad = 18
        self.color = "purple"
        #rect corresponde a rectángulo
        #pygame.Rect(self.x, self.y,self.ancho,self.alto) aca indicamos las dimensiones y coordenanas (posiciones) que previamente habíamos determinao
        self.rect=pygame.Rect(self.x, self.y,self.ancho,self.alto)
        # self.vida= 5 establece la cantidad de vidas del enemigo
        self.vida= 5
    
    def dibujar(self,ventana):
        self.rect=pygame.Rect(self.x, self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)
    #Función para que el enemigo se mueva para abajo
    def movimiento(self):
        self.y += self.velocidad