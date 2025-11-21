#Acá se crea el personaje del juego
#Importamos la librería pygame
import pygame

#El personaje será un cubo
class Cubo:
    def __init__(self,x,y):
        #Comenzamos a configurar las posiciones iniciales y dimensiones
        self.x=x
        self.y=y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 10
        self.color = "red"
        #rect corresponde a rectángulo
        #pygame.Rect(self.x, self.y,self.ancho,self.alto) aca indicamos las dimensiones y coordenanas (posiciones) que previamente habíamos determinao
        self.rect=pygame.Rect(self.x, self.y,self.ancho,self.alto)
    
    def dibujar(self,ventana):
        self.rect=pygame.Rect(self.x, self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)