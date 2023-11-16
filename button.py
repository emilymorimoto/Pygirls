import pygame
from pygame.locals import *

pygame.init()

# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Carregue a imagem do botão
button_image = pygame.image.load("button_image.png")
button_rect = button_image.get_rect(topleft=(200, 200))

# Configurações do botão
hover_color = (200, 200, 200)
click_color = (150, 150, 150)

# Inicialize a janela
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Botão em Pygame")

clock = pygame.time.Clock()

running = True
button_clicked = False

while running:
    screen.fill(BLACK)

    # Desenha a imagem do botão
    screen.blit(button_image, button_rect)

    # Detecta a posição do mouse
    mouse_pos = pygame.mouse.get_pos()

    # Verifica se o mouse está sobre o botão
    if button_rect.collidepoint(mouse_pos):
        # Pode ajustar a cor ou adicionar um efeito visual ao hover se desejar
        pass

    # Verifica eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 representa o botão esquerdo do mouse
                if button_rect.collidepoint(mouse_pos):
                    button_clicked = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if button_clicked and button_rect.collidepoint(mouse_pos):
                    print("Botão clicado!")
                    # Coloque aqui o código que deseja executar quando o botão for clicado

                    
                button_clicked = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
