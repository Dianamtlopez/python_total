#******************************************************
#* LEMA:                * INTENTA, INSISTE Y RESISTE  *
#* DESARROLLADA POR:    * DIANA MARÍA TORO LÓPEZ      *
#* CURSO:               * PYTHON TOTAL                *
#* INSTRUCTOR:          * FEDERICO GARAY              *
#* ENTIDAD:             * UDEMY                       *
#******************************************************
# Importa la librería pygame para crear la interfaz y manejar gráficos y eventos del juego.
import pygame  
# Importa la librería random para generar números aleatorios que se usarán en el movimiento de los enemigos.
import random  
# Importa math para realizar operaciones matemáticas avanzadas, como calcular distancias.
import math  
# Importa mixer de pygame para cargar y controlar los sonidos y la música de fondo del juego.
from pygame import mixer  
# Importa io para Crea una función que transforme el nombre de las fuentes de string a objeto Bytes.
import io

# Inicializa todos los módulos de pygame para prepararlos antes de usarlos.
pygame.init()

# función que transforme el nombre de la fuente (“Wedgie Regular.ttf”) de string a objeto Bytes
def fuente_bytes(fuente):
    # Abre el archivo TTF en modo lectura binaria
    with open(fuente, 'rb') as f:
        # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
        # Crea un objeto BytesIO a partir de los bytes de un archivo TTF
        return io.BytesIO(ttf_bytes)

# Crea una ventana de 800x600 píxeles para el juego.
pantalla = pygame.display.set_mode((800, 600))

# Establece el título de la ventana del juego.
pygame.display.set_caption("Invasión Espacial")
# Carga una imagen que se usará como icono de la ventana.
icono = pygame.image.load("ovni.png")
# Establece la imagen cargada como el icono de la ventana.
pygame.display.set_icon(icono)
# Carga una imagen de fondo para la pantalla del juego.
fondo = pygame.image.load('fondo.jpg')

# Carga un archivo de música para el fondo del juego.
mixer.music.load('MusicaFondo.mp3')
# Ajusta el volumen de la música de fondo a un 50%.
mixer.music.set_volume(0.5)
# Inicia la reproducción de la música en bucle, para que se repita indefinidamente.
mixer.music.play(-1)

# Carga la imagen del jugador (nave espacial).
img_jugador = pygame.image.load("cohete.png")
# Establece la posición inicial en el eje X del jugador en el centro de la pantalla.
jugador_x = 368
# Establece la posición inicial en el eje Y del jugador en la parte inferior de la pantalla.
jugador_y = 500
# Inicializa la variable de cambio en la posición X del jugador a 0, para usar en el movimiento horizontal.
jugador_x_cambio = 0

# Comentado: Variables del enemigo para una sola nave enemiga, se reemplaza por múltiples enemigos en listas.

# Inicializa listas para múltiples enemigos (imágenes, posiciones y velocidades).
img_enemigo = []  # Lista que almacena las imágenes de cada enemigo.
enemigo_x = []  # Lista que almacena las posiciones X de cada enemigo.
enemigo_y = []  # Lista que almacena las posiciones Y de cada enemigo.
enemigo_x_cambio = []  # Lista para la velocidad de movimiento horizontal de cada enemigo.
enemigo_y_cambio = []  # Lista para la velocidad de movimiento vertical de cada enemigo.
cantidad_enemigos = 8  # Número total de enemigos en el juego.

# Bucle para inicializar los atributos de cada enemigo (imagen, posición y velocidad).
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))  # Carga y agrega la imagen del enemigo.
    enemigo_x.append(random.randint(0, 736))  # Posición X aleatoria para cada enemigo.
    enemigo_y.append(random.randint(50, 200))  # Posición Y aleatoria para cada enemigo.
    enemigo_x_cambio.append(0.3)  # Velocidad inicial de movimiento horizontal de cada enemigo.
    enemigo_y_cambio.append(50)  # Velocidad de descenso de cada enemigo cuando toca un borde.

# Carga la imagen de la bala que disparará el jugador.
img_bala = pygame.image.load("bala.png")
# Inicializa la posición X de la bala (se ajustará al disparo del jugador).
bala_x = 0
# Inicializa la posición Y de la bala en la misma posición vertical que el jugador.
bala_y = 500
# Velocidad de la bala en el eje X (no se usa aquí, porque solo se mueve en el eje Y).
bala_x_cambio = 0
# Velocidad de la bala en el eje Y.
bala_y_cambio = 3
# Estado de visibilidad de la bala: False significa que no se muestra hasta dispararse.
bala_visible = False

# Lista para múltiples balas, permite al jugador disparar varias al mismo tiempo.
balas = []
# Bucle que controla el movimiento de cada bala en pantalla y su eliminación.
for bala in balas:
    bala["y"] += bala["velocidad"]  # Mueve la bala hacia arriba en el eje Y.
    pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))  # Dibuja la bala en pantalla.
    if bala["y"] < 0:  # Si la bala sale de la pantalla, se elimina de la lista.
        balas.remove(bala)

# Inicializa el puntaje del jugador en 0.
puntaje = 0
# Configura la fuente para mostrar el marcador en pantalla.
fuente_como_bytes = fuente_bytes('Wedgie Regular.ttf')
fuente = pygame.font.Font(fuente_como_bytes, 32)
# Posición en X donde se mostrará el marcador en pantalla.
texto_x = 10
# Posición en Y donde se mostrará el marcador en pantalla.
texto_y = 10

# Configura la fuente y tamaño del texto final de "Juego Terminado".
fuente_final = pygame.font.Font(fuente_como_bytes, 50)

# Función para mostrar el texto de "Juego Terminado" en la pantalla.
def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255,255,255))  # Renderiza el texto en color blanco.
    pantalla.blit(mi_fuente_final, (50, 200))  # Dibuja el texto en el centro de la pantalla.

# Función para mostrar el puntaje en pantalla.
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))  # Renderiza el texto del puntaje.
    pantalla.blit(texto, (x, y))  # Dibuja el puntaje en la posición especificada.

# Función para mostrar la imagen del jugador en pantalla.
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))  # Dibuja la imagen del jugador en las coordenadas especificadas.

# Función para mostrar un enemigo en pantalla.
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))  # Dibuja la imagen del enemigo en la posición especificada.

# Función para disparar la bala desde la posición del jugador.
def disparar_bala(x, y):
    global bala_visible  # Permite modificar el estado de visibilidad de la bala.
    bala_visible = True  # Cambia la visibilidad de la bala para que sea visible.
    pantalla.blit(img_bala, (x + 16, y + 10))  # Dibuja la bala en el centro del jugador.

# Función para detectar si hay una colisión entre la bala y un enemigo.
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))  # Calcula la distancia entre dos puntos.
    if distancia < 27:  # Si la distancia es menor a 27, se considera una colisión.
        return True
    else:
        return False

# Variable de control para mantener el juego en ejecución.
se_ejecuta = True

# Bucle principal del juego.
while se_ejecuta:
    pantalla.blit(fondo, (0, 0))  # Dibuja la imagen de fondo en la pantalla.

    # Revisa eventos (como cerrar la ventana o presionar teclas).
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False  # Salir del bucle si se cierra la ventana.

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:  # Si se presiona la tecla de flecha izquierda.
                jugador_x_cambio -= 1
            if evento.key == pygame.K_RIGHT:  # Si se presiona la tecla de flecha derecha.
                jugador_x_cambio += 1
            if evento.key == pygame.K_SPACE:  # Si se presiona la barra espaciadora.
                sonido_bala = mixer.Sound("disparo.mp3")  # Reproduce el sonido de disparo.
                sonido_bala.play()
                nueva_bala = {  # Nueva bala creada con posición y velocidad.
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)  # Agrega la nueva bala a la lista de balas.

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:  # Si se deja de presionar las teclas de dirección.
                jugador_x_cambio = 0  # Detener el movimiento en X.

    jugador_x += jugador_x_cambio  # Actualiza la posición en X del jugador.

    # Limita el movimiento del jugador dentro de los bordes de la pantalla.
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Bucle para actualizar la posición de cada enemigo.
    for e in range(cantidad_enemigos):
        if enemigo_y[e] > 450:  # Verifica si un enemigo toca la base.
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000  # Envía todos los enemigos fuera de la pantalla.
            texto_final()  # Muestra el texto de "Juego Terminado".
            break

        enemigo_x[e] += enemigo_x_cambio[e]  # Actualiza la posición X de cada enemigo.

        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3  # Cambia la dirección del enemigo hacia la derecha.
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3  # Cambia la dirección del enemigo hacia la izquierda.
            enemigo_y[e] += enemigo_y_cambio[e]

        # Verifica colisiones entre cada enemigo y las balas.
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")  # Reproduce sonido de colisión.
                sonido_colision.play()
                balas.remove(bala)  # Remueve la bala que impactó.
                puntaje += 1  # Incrementa el puntaje.
                enemigo_x[e] = random.randint(0, 736)  # Reubica el enemigo en X.
                enemigo_y[e] = random.randint(20, 200)  # Reubica el enemigo en Y.
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)  # Dibuja cada enemigo.

    # Actualiza el movimiento de las balas en pantalla.
    for bala in balas:
        bala["y"] += bala["velocidad"]  # Mueve la bala en el eje Y.
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))  # Dibuja la bala en pantalla.
        if bala["y"] < 0:
            balas.remove(bala)  # Elimina la bala si sale de la pantalla.

    jugador(jugador_x, jugador_y)  # Dibuja el jugador.
    mostrar_puntaje(texto_x, texto_y)  # Muestra el puntaje actual.

    pygame.display.update()  # Actualiza la pantalla para mostrar cambios.
