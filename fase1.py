import pygame
from pygame.locals import *
import sys

# Seus caminhos para as imagens
background_image_filename = "fundo.png"
arara_image_filename = "araraazul.png"
bala_image_fase1 = "bala.png"
madeira_image_filename = "madeira.png"
fogo_image_filename = "fogo.png"

pygame.init()
screen = pygame.display.set_mode((14950, 674), 0, 32)
background = pygame.image.load(background_image_filename).convert()
arara_img = pygame.image.load(arara_image_filename)
bala_img = pygame.image.load(bala_image_fase1)
madeira_img = pygame.image.load(madeira_image_filename)
fogo_img = pygame.image.load(fogo_image_filename)

bala_img = pygame.transform.scale(bala_img, (100, 100))
madeira_img = pygame.transform.scale(madeira_img, (100, 100))
fogo_img = pygame.transform.scale(fogo_img, (100, 100))

clock = pygame.time.Clock()

x = 0
y = 0
move_y = 0
speed = 150

arara_rect = arara_img.get_rect()
arara_rect.topleft = (0, y)

bala_rects = [
    bala_img.get_rect(x=3200, y=100),
    bala_img.get_rect(x=4500, y=250)
]

madeira_rects = [
    madeira_img.get_rect(x=2000, y=100),
    madeira_img.get_rect(x=3000, y=250)
]

fogo_rects = [
    fogo_img.get_rect(x=1300, y=100),
    fogo_img.get_rect(x=3800, y=250)
]

vidas = 3
colisao = [False, False, False, False]  # Lista para controlar colisão com cada bala
colisao_madeira = [False, False]  # Lista para controlar colisão com cada madeira
colisao_fogo = [False, False]  # Lista para controlar colisão com cada fogo

piscar = False  # Variável para alternar a visibilidade da arara
piscar_countdown = 0  # Contador para controlar o tempo de piscagem
piscar_duration = 10  # Duração da piscagem (em ciclos)

running = True
while running:
    screen.blit(background, (x, 0))

    if piscar:
        if piscar_countdown % 2 == 0:
            screen.blit(arara_img, (0, y))
    else:
        screen.blit(arara_img, (0, y))

    for bala_rect in bala_rects:
        screen.blit(bala_img, bala_rect.topleft)

    for madeira_rect in madeira_rects:
        screen.blit(madeira_img, madeira_rect.topleft)

    for fogo_rect in fogo_rects:
        screen.blit(fogo_img, fogo_rect.topleft)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Vidasss: {vidas}", True, (255, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x -= distance_moved

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                move_y = -4
            if event.key == K_DOWN:
                move_y = 4
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                move_y = 0

    y += move_y

    for bala_rect in bala_rects:
        bala_rect.x -= int(distance_moved)

    for madeira_rect in madeira_rects:
        madeira_rect.x -= int(distance_moved)  # Movimento da direita para a esquerda

    for fogo_rect in fogo_rects:
        fogo_rect.x -= int(distance_moved)  # Movimento da direita para a esquerda

    if move_y != 0:
        for i, bala_rect in enumerate(bala_rects):
            if arara_rect.colliderect(bala_rect) and not colisao[i]:
                vidas -= 1
                colisao[i] = True
                del bala_rects[i]

                piscar = True
                piscar_countdown = piscar_duration

        for i, madeira_rect in enumerate(madeira_rects):
            if arara_rect.colliderect(madeira_rect) and not colisao_madeira[i]:
                vidas -= 1
                colisao_madeira[i] = True
                del madeira_rects[i]

                piscar = True
                piscar_countdown = piscar_duration

        for i, fogo_rect in enumerate(fogo_rects):
            if arara_rect.colliderect(fogo_rect) and not colisao_fogo[i]:
                vidas -= 1
                colisao_fogo[i] = True
                del fogo_rects[i]

                piscar = True
                piscar_countdown = piscar_duration

    if piscar:
        piscar_countdown -= 1
        if piscar_countdown <= 0:
            piscar = False

    for i, bala_rect in enumerate(bala_rects[:]):
        if not arara_rect.colliderect(bala_rect) and colisao[i]:
            colisao[i] = False

    for i, madeira_rect in enumerate(madeira_rects[:]):
        if not arara_rect.colliderect(madeira_rect) and colisao_madeira[i]:
            colisao_madeira[i] = False

    for i, fogo_rect in enumerate(fogo_rects[:]):
        if not arara_rect.colliderect(fogo_rect) and colisao_fogo[i]:
            colisao_fogo[i] = False

    if vidas == 0:
        print("Você perdeu todas as vidas! Fim de jogo!")
        running = False

    if y <= 0:
        y = 0
    elif y >= 674 - 201:
        y = 674 - 201

    arara_rect.topleft = (0, y)

pygame.quit()
sys.exit()