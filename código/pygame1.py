#Importamos la librería pygame
import pygame
#Importamos desde el archivo personaje la clase cubo
from figura_principal import Cubo
from enemigo_principal import Enemigo
import random
from bala_juego import Bala



#Si no se ejecuta pygame.init() las fuentes no se ejecutarán
pygame.init()
# Definir constantes

pygame.mixer.init()
#Cargar y reproducir música de fondo

#Ancho de la pantalla
ANCHO = 400
#Alto de la pantalla  
ALTO = 600
#Ventana en donde se despliega el ancho y alto
VENTANA = pygame.display.set_mode([ANCHO,ALTO])
#Indico la configuración del FPS que se utilizará después con la variable reloj más abajo
FPS = 60
#Definiendo la fuente del texto
FUENTE = pygame.font.SysFont("Arial", 40)
SONIDO_DISPARO = pygame.mixer.Sound('media/1130.wav')
SONIDO_MUERTE = pygame.mixer.Sound('media/358.wav')

#la variable para comenzar  
jugando = True
#variables vidas y puntos para establecer un sistema que permita que el usuario juegue una cantidad de veces determinadas
vida = 5
puntos = 0

#Cada cierto tiempo deben exitir más enemigos, por lo que es necesario ocupar esta variable que me vaya gestionando el tiempo
reloj = pygame.time.Clock()

#con tiempo_pasado y tiempo_entre_enemigos indicamos cuantos milisegundos deben pasar entre que aparece un enemigo y aparece otro
tiempo_pasado = 0
tiempo_entre_enemigos = 250

#creamos la variable cubo en minúsculas a la cual le indicamos la posición inicial
cubo = Cubo(ANCHO/2,ALTO-75)

#Codifico una lista que se guardará en la variable enemigos para poder establecer después las posiciones, velocidades, cómo se mueven, etc
enemigos=[]

#Acá se utilizará esta lista para la función crear_bala()
balas= []

#La variable ultima_bala contendrá los milisegundos que contendrá la última bala
ultima_bala = 0
# tiempo_entre_balas son los tiempos en milisegundos entre cada bala
tiempo_entre_balas = 250

#A través de este código le pasamos al menos un enemigo a la lista enemigos con un ancho y un alto determinado
enemigos.append(Enemigo(ANCHO/2,100))

#Definimos la acción de crear_bala en donde le indicamos que inicie desde dond ese encuentra nuesto cubo con balas.append(Bala(cubo.rect.centerx,cubo.rect.centery))
def crear_bala():
    global ultima_bala

    #get_ticks entrega la cantidad de ticks que han pasado desde la ejecución del juego hasta ahora
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(cubo.rect.centerx,cubo.rect.centery))
        ultima_bala=pygame.time.get_ticks()
        SONIDO_DISPARO.play()


#función para gestionar las teclas
def gestionar_teclas(teclas):
    #Indicamos con el índice pygadme.K_w que al presionar la tecla "W" el objeto vaya hacia arriba
    #Recordar que para arriba y abajo se ocupa el eje Y, y para el izquierda y derecha se ocupa el eje X.
    #Para arrba y a la iozquierda se resta velocidad. 
    #Para abajo y a la derecha se suma velocidad
    #Conenté las telas w y s para que el cuadrado se mueva solo de forma horizontal
    # if teclas[pygame.K_w]:
    #     cubo.y -= cubo.velocidad
    # if teclas[pygame.K_s]:
    #     cubo.y += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
    # Esta condición if teclas [pygame.K_SPACE y la función crear_bala() indica que el espacio será la tecla que activará la función
    if teclas [pygame.K_SPACE]:
        crear_bala()


#Iniciamos el bucle
while jugando and vida > 0:
    # reloj.tick(FPS) permitirá que la ejecutción del juego se mueva a unos determinados FPS. A menor FPS más lento
    # A partir del segundo bucle se comieza a sumar en tiempo_pasado la cantidad de milisegundos que quedan para que aparezca un enemigo y aparezca otro
    tiempo_pasado += reloj.tick(FPS)

    #Indico con un if que si tiempo_pasado es mayor a tiempre_entre_enemigos, se cree un nuevo enemigo en la lista enemigos
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))
        #Para que no se creen de manera constante y existe espacio entre ellos, le indico que la variable tiempo_pasado debe volver a 0 cada vez
        tiempo_pasado = 0
    #Eventos como clickear una tecla o presionar algo en la pantalla serán denominados de tal manera (eventos)
    eventos = pygame.event.get()
    #Se guardará en la variable teclas las teclas que se presionen
    #la función pygame.key.get_pressed() devuelve una lista con todas las teclas que están siendo presionadas
    teclas = pygame.key.get_pressed()
    #Asigno el texto que eventualmente aparecerá en la pantalla
    texto_vida = FUENTE.render(f"Vida: {vida}", True, "white")
    #
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")

    #Se crea una función para gestionar las teclas
    gestionar_teclas(teclas)
    #Por cada evento dentro de la variable eventos comprobaremos que tipo de evento es
    for evento in eventos:
        # pygame.QUIT es cuando haces F4, cierras la ventana, cierres el navegador, etc.
        if evento.type == pygame.QUIT:
            jugando = False
    #Acá se indica con qué color se rellenará el espacio que ya no este ocupando el cubo
    VENTANA.fill("black")
    #Cada vez que de una vuelta al bucle principal dibuje el cubo
    cubo.dibujar(VENTANA)

    #Hay que actualizar las posiciones de los enemigos, por lo que ocupamos un for en enemigos
    # y pasamos enemigo.dibujar(VENTANA)s
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        #llamo la función movimiento para que eejecute el movimiento del enemigo
        enemigo.movimiento()
        #COn esta condición si el enemigo colisiona con el cubo se restará un punto de vida
        if pygame.Rect.colliderect(cubo.rect,enemigo.rect):
            vida -= 1 
            print(f"Te quedan {vida} vidas")
            enemigos.remove(enemigo)
        #Esta condición permite que sumemos punstos y que remueva los cuadrados enemigos al llegar al final
        #if enemigo.y + enemigo.alto > ALTO:
        #Si quiero que se elimine el enemigo no cuando toque el suelo, sino que, cuando todo su cuadrado traspase el suelo,
        #se ocupa esta condición 
        if enemigo.y > ALTO:
            puntos +=1
            enemigos.remove(enemigo)
        #Este for permite que al colisionar la bala con el enemigo, ambos desaparezcan.
        for bala in balas:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigos.remove(enemigo)
                #al colisionar la bala con el enemigo, se le resta 1 vida al enemigo
                enemigo.vida -= 1
                balas.remove(bala)
                puntos += 1
        
        #if enemigo.vida <= 0 permite que al llegar el enemigo a 0 vidas desaparezca
        if enemigo.vida <= 0:
            SONIDO_MUERTE.play()
            enemigos.remove(enemigo)
        
    for bala in balas:
        bala.dibujar(VENTANA)
        bala.movimiento()


    #El comando blit toma un objeto y lo pega en la pantalla
    #le indicamos el objeto "texto_vida"
    #Después le indcamos las coordenadas de donde estará
    VENTANA.blit(texto_vida, (20, 20))
    #Hacemos lo mismo pero con los puntos
    VENTANA.blit(texto_puntos, (20, 60))
    
    pygame.display.update()

SONIDO_MUERTE.play()
pygame.time.delay(1500)  # 1.5 segundos para que suene el sonido antes de cerrar
#Acá cerramos la ventana de  pygame
pygame.quit()

nombre = input("Introduce tu nombre: ")
with open ('puntuaciones.txt','a') as archivo:
    archivo.write(f"{nombre} - {puntos}\n")
    print("Tus puntos han sido registrados")

#la función quit finalmente nos permite salir del juego al estar la variable jugando como False
quit()