# Importa configurações da tela e do jogo
from Setup_tela import *
from Setup_Game import *
# Função para desenhar um ator na tela
def draw_actor(draw_inf):
    # Extrai informações do ator da tupla fornecida
    type, skin, color, act_posx, act_posy = draw_inf
    global size_pixel # Tamanho do pixel (globalmente definido)
    # Verifica se o ator é do tipo
    if type == 'alien a':
        # Verifica a variante da pele (skin) para determinar o design
        if skin == 0:
            design = [
                (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1),
                (1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
                (0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0)
            ]
        if skin == 1:  
            design = [
                (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0),
                (1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1),
                (1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1),
                (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0)
            ]
    
    if type == 'alien b':
        if skin == 0:
            design = [
                (0, 0, 0, 1, 0, 0, 0),
                (0, 0, 1, 1, 1, 0, 0),
                (0, 1, 1, 1, 1, 1, 0),
                (1, 1, 0, 1, 0, 1, 1),
                (1, 1, 1, 1, 1, 1, 1),
                (0, 1, 0, 1, 0, 1, 0),
                (1, 0, 0, 0, 0, 0, 1),
                (0, 1, 0, 0, 0, 1, 0)
            ]
        if skin == 1:  
            design = [
                (0, 0, 0, 0, 1, 0, 0, 0, 0),
                (0, 0, 0, 1, 1, 1, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 0, 1, 0, 1, 1, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 0),
                (0, 0, 1, 0, 0, 0, 1, 0, 0),
                (0, 1, 0, 1, 1, 1, 0, 1, 0),
                (1, 0, 0, 0, 0, 0, 0, 0, 1)
            ]
    if type == 'alien c':
        if skin == 0:
            design = [
                (0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0),
                (0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0),
                (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0)
            ]
        if skin == 1:  
            design = [
                (0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0),
                (1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1),
            ]
    if type == 'cannon':
        if skin == 0:
            design = [
                (0, 0, 0, 1, 0, 1, 0, 0, 0),
                (0, 0, 1, 1, 0, 1, 1, 0, 0),
                (0, 0, 1, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 0, 1, 0, 1, 0, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 0),
                (0, 1, 1, 1, 0, 1, 1, 1, 0),
                (1, 1, 1, 1, 1, 1, 1, 1, 1)
            ]
        if skin == 1:  
            design = [
                (0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 1, 0, 0),
                (0, 0, 1, 1, 0, 1, 1, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 0),
                (0, 1, 1, 1, 0, 1, 1, 1, 0),
                (1, 1, 1, 1, 1, 1, 1, 1, 1)
            ]
    if type == 'ship':
        if skin == 0:
            design = [
                (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0)
            ]
        if skin == 1:  
            design = [
                (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1),
                (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                (0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0)
            ]
    if type == 'plasma':
        if skin == 0:
            design = [
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0)
            ]
        if skin == 1:
            design = [
                (0, 1, 0),
                (0, 1, 1),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (1, 1, 0),
                (0, 1, 1),
                (0, 1, 0)
            ]
        if skin == 2:
            design = [
                (0, 1, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
                (0, 1, 0),
                (1, 1, 0),
                (0, 1, 0),
                (0, 1, 1)
            ]
        if skin == 3:
            design = [
                (0, 0, 0),
                (0, 0, 0),
                (0, 0, 0),
                (0, 0, 0),
                (0, 1, 0),
                (1, 1, 0),
                (1, 1, 1),
                (0, 1, 1)
            ]
        if skin == 4:
            design = [
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
                (0, 1, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
                (0, 1, 0)
            ]
        if skin == 5:
            design = [
                (0, 1, 0),
                (1, 0, 0),
                (1, 0, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, 1, 1),
                (0, 1, 0),
                (1, 0, 0)
            ]    
    if type == 'explosion':
        if skin == 0:
            design = [
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
                (0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0),
                (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
                (0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            ]
        if skin == 1:
            design = [
                (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0),
                (0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0),
                (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0)
            ]
        if skin == 2:
            design = [
                (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                (0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0)
            ]
    if type == 'shot':
        if skin == 0:
            design = [
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
                (0, 1, 0),
                (1, 0, 0)
            ]
        if skin == 1:
            design = [
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0)
            ]
        if skin == 2:
            design = [
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 0, 1),
                (0, 1, 0),
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1)
            ]
        
        if skin == 3:
            design = [
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0),
                (0, 1, 0)
            ]

    # Calcula o tamanho do design em relação ao eixo x e y
    size_design_x = len(design[0])
    size_design_y = len(design)

    # Inicializa o índice de linha (L) para 0
    L = 0  # Inicializa L

    # Loop através das linhas do design
    for pixel in design:
        for i in range(len(pixel)):
            
            # Calcula a posição do pixel na tela
            posx = (act_posx*size_pixel) - ((size_design_x // 2) * size_pixel) + (i * size_pixel)
            posy = (act_posy*size_pixel) - ((size_design_y // 2) * size_pixel) + (L * size_pixel)


            # Verifica se o valor na posição atual é 1 antes de desenhar
            if pixel[i] == 1:
                pygame.draw.rect(tela, color, (posx, posy, size_pixel, size_pixel))
                
        L += 1  # Incrementa L após cada linha


def draw_grid():
    # Tamanho do pixel utilizado na grade
    global size_pixel

    # Loop para iterar sobre as colunas da grade
    for i in range(screen_width // size_pixel):
        # Loop para iterar sobre as linhas da grade
        for j in range(screen_height // size_pixel):
            # Calcula as coordenadas (posx, posy) do ponto de início de cada célula
            posx = i * size_pixel
            posy = j * size_pixel

            # Desenha uma pequena célula na tela representando a grade
            pygame.draw.rect(tela, grid_color, (posx, posy, 1, 1))
