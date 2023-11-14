import pygame
from pygame.locals import * 
from sys import exit
import random

background_image_filename = "fundo.png"
sprite_image_filename = "araraazul.png"
object_image_fase1 = "bala.png"




pygame.init ()
screen = pygame.display. set_mode ((14950, 674), 0, 32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame. image.load(sprite_image_filename)
object_image = pygame.image.load(object_image_fase1)

clock = pygame.time.Clock()

x = 0
y = 0
move_y = 0
speed = 250
xObject = 0




while True: 
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit()
            exit ()

    screen.blit(background, (x, 0))
    screen.blit(object_image, (1200, 100))
    screen.blit(object_image, ( 2300, 400))
    screen.blit(object_image, ( 3100, 200))



    screen.blit(sprite, (0, y))

    time_passed = clock.tick()
    time_passed_seconds =  time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x -= distance_moved

    distance_moved = time_passed_seconds * speed
    xObject -= distance_moved

    sprite_rect = sprite.get_rect()
    sprite_rect.topleft = (0, y)

    object_rect = object_image.get_rect()
    object_rect.topleft = (xObject + 1200, 100)  # Posição da bala - ajuste conforme necessário

    if sprite_rect.colliderect(object_rect):
        print("Arara colidiu com a bala!")

   

    #up
    if event.type == KEYDOWN:
        if event.key==K_UP:
            move_y=-3
    if event.type == KEYUP:
        if event.key == K_UP:
            move_y=0

    #down
    if event.type == KEYDOWN:
        if event.key==K_DOWN:
            move_y=+3
    if event.type == KEYUP:
        if event.key == K_DOWN:
            move_y=0


    y += move_y

    #if y >= 674:
     #y = 100
    if y <= 0:
        y = 0 
    elif y >= 674 - 201:
        y = 674 - 201

   


    pygame.display.update ()





# import pygame
# from pygame.locals import * 
# from sys import exit 


# background_image_filename = "fundo.png"
# sprite_image_filename = "araraazul.png"


# pygame.init ()
# screen = pygame.display. set_mode ((1400, 500), 0, 32)
# background = pygame.image.load(background_image_filename).convert()
# sprite = pygame. image.load(sprite_image_filename)

# x1 = 0


# x,y=0,0
# move_x, move_y = 0,0


# while True: 
#     for event in pygame.event.get ():
#         if event.type == QUIT:
#             pygame.quit()
#             exit ()

#     screen.blit(background, (0, 0))
#     screen.blit(sprite, (x1, 100))

#     #up
#     if event.type == KEYDOWN:
#         if event.key==K_UP:
#             move_y=-1
#     if event.type == KEYUP:
#         if event.key == K_UP:
#             move_y=0

#     #down
#     if event.type == KEYDOWN:
#         if event.key==K_DOWN:
#             move_y=+1
#     if event.type == KEYUP:
#         if event.key == K_DOWN:
#             move_y=0


#     x += move_x
#     y += move_y

#     x1 += 1

#     # if x > 640:
#     #     x -= 640
#     pygame.display.update ()

  # if event.type == CREATE_OBJECT_EVENT:
    #         random_x = random.randint(0, 1400 - object_image.get_width())
    #         random_y = random.randint(0, 500 - object_image.get_height())
    #         screen.blit(object_image, (random_x, random_y))

    
     # ERRADDO Gera coordenadas x e y aleatórias para o objeto da fase 1



    # if x <= -1400:  # Verifica se o fundo ultrapassou o comprimento total
    #     x = 0  # Reinicia a posição do fundo para 0



    # # Crie retângulos de colisão para os elementos
    # sprite_rect = sprite.get_rect()
    # sprite_rect.topleft = (0, y)

    # object_rect = object_image.get_rect()
    # object_rect.topleft = (xObject + 1200, 100)  # Posição da bala - ajuste conforme necessário

    # # Verifique a colisão entre a arara e a bala
    # if sprite_rect.colliderect(object_rect):
    #     is_grayscale = True
    #     grayscale_time = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos

    # # Se a arara estiver em preto e branco e o tempo passado for maior que a duração definida
    # if is_grayscale and pygame.time.get_ticks() - grayscale_time >= grayscale_duration:
    #     is_grayscale = False
    #     sprite = pygame.image.load(sprite_image_filename)  # Restaura a imagem colorida

    # # Se a arara estiver em preto e branco, blit a versão em escala de cinza
    # if is_grayscale:
    #     screen.blit(sprite_gray, (0, y))
    # else:
    #     screen.blit(sprite, (0, y))




    # sprite_rect = sprite.get_rect()
    # sprite_rect.topleft = (0, y)

    # object_rect = object_image.get_rect()
    # object_rect.topleft = (xObject + 1200, 100)  # Posição da bala - ajuste conforme necessário

    # # Verifique a colisão entre a arara e a bala
    # if sprite_rect.colliderect(object_rect):
    #     # Converta a imagem da arara para escala de cinza
    #     sprite = sprite_gray.copy()
    #     screen.blit(sprite, (0, y))

    #     # Atualize a tela
    #     pygame.display.update()

    #     # Espere por 3 segundos (3000 milissegundos)
    #     pygame.time.delay(3000)

    #     # Restaure a imagem colorida da arara
    #     sprite = pygame.image.load(sprite_image_filename)


# # Defina uma variável de controle para saber se a arara está em preto e branco
# is_grayscale = False
# grayscale_time = 0
# grayscale_duration = 3000  # 3 segundos em milissegundos

# # Função para converter a imagem para escala de cinza
# def grayscale(image):
#     return image.convert_alpha()

# # Carregue as imagens em escala de cinza
# sprite_gray = grayscale(sprite)
# object_image_gray = grayscale(object_image)
