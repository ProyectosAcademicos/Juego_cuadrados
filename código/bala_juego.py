#Acá se crea la bala del juego
#Importamos la librería pygame
import pygame

#El enemigo también será un cubo
class Bala:
    def __init__(self,x,y):
        #Comenzamos a configurar las posiciones iniciales y dimensiones
        self.x=x
        self.y=y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 10
        self.color = "white"
        #rect corresponde a rectángulo
        #pygame.Rect(self.x, self.y,self.ancho,self.alto) aca indicamos las dimensiones y coordenanas (posiciones) que previamente habíamos determinado
        self.rect=pygame.Rect(self.x, self.y,self.ancho,self.alto)
    
    def dibujar(self,ventana):
        self.rect=pygame.Rect(self.x, self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)
    #Función para que la bala se mueva para abajo
    def movimiento(self):
        self.y -= self.velocidad