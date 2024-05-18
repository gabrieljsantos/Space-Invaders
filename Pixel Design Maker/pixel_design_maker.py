from Setup_tela import *
import pickle
import os
import random
import string
import time

os.makedirs('PDM Objects', exist_ok=True)

empty_design = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
created_design = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
created_design_text = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
]



last_button_pressed_state = False
# Função para salvar o estado em um arquivo
def write_design():
    pos_text_x = 810
    pos_text_y = 20
    global created_design
    global created_design_text
    global last_button_pressed_state
    fonte = pygame.font.Font(None, 40)
    write_design_texto = fonte.render("Write_Design", True, test_color)
    tela.blit(write_design_texto, (pos_text_x , 20))
    if pygame.mouse.get_pressed()[0] == False:
        last_button_pressed_state = False
    position_mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == True and last_button_pressed_state == False:
        # Verifica se a posição está dentro dos limites
        if position_mouse[0] > pos_text_x and position_mouse[0] <= write_design_texto.get_width()+ pos_text_x:
            if position_mouse[1] > pos_text_y and position_mouse[1] <= write_design_texto.get_height()+ pos_text_y:
                id_file = str(random.randint(1000, 10000))  
                filepath = os.path.abspath(os.path.join('PDM Objects', f'object_{id_file}.pdm'))
                for i in range(len(created_design[0])):
                    for j in range(len(created_design)):
                        created_design_text[j][i] = str(int(created_design[i][j]))  # Converte para '0' ou '1'
                with open(filepath, 'w') as f:  # Abre o arquivo em modo texto ('w')
                    for row in created_design_text:
                        f.write('(' + ', '.join(row) + '),\n')
                last_button_pressed_state = True
        
    
        

def carregar_estado(arquivo):
    with open(arquivo, 'rb') as f:
        estado = pickle.load(f)
    return estado

def grid_pdm():
    size_pixel = 800 // 13
    for i in range(13):
        for j in range(13):
            posx = i * size_pixel
            posy = j * size_pixel
            pygame.draw.rect(tela, test_color, (posx, posy, size_pixel, size_pixel), 1)

def selecionar(): ## Marcar a seleção e retorna o bloco selecionado
    global created_design
    size_pixel = screen_height // 13
    posision = pygame.mouse.get_pos()
    selecion_x=posision[0]//size_pixel
    selecion_y=posision[1]//size_pixel
    if selecion_x > 12:
        return 'null'
    if (pygame.mouse.get_focused() == True) :
        if (posision[0] <= screen_height):
            lugar_selecionado = pygame.draw.rect(tela, test_color, (selecion_x * size_pixel, selecion_y  * size_pixel, size_pixel, size_pixel))
    


def paint():
    global created_design
    size_pixel = screen_height // 13
    position = pygame.mouse.get_pos()
    alvo_x = int(position[0] // size_pixel)
    alvo_y = int(position[1] // size_pixel)
    # Verifica se o botão esquerdo do mouse está pressionado
    if pygame.mouse.get_pressed()[0]:
        # Verifica se a posição está dentro dos limites
        if 0 <= alvo_y < len(created_design) and 0 <= alvo_x < len(created_design[0]):
            created_design[alvo_x][alvo_y] = True

    # Verifica se o botão direito do mouse está pressionado
    elif pygame.mouse.get_pressed()[2]:
        # Verifica se a posição está dentro dos limites
        if 0 <= alvo_y < len(created_design) and 0 <= alvo_x < len(created_design[0]):
            created_design[alvo_x][alvo_y] = False

def draw_paint():
    global created_design
    size_pixel = screen_height // 13

    for i in range(len(created_design[0])):
        for j in range(len(created_design)):
            if created_design[i][j] == 1:
                pygame.draw.rect(tela, test_color, (i*size_pixel, j*size_pixel, size_pixel, size_pixel))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Adicione a verificação do clique do mouse dentro do bloco do menu
    tela.fill(background_color)
    grid_pdm()
    selecionar()
    paint()
    draw_paint()
    
    write_design()


    # Atualize a tela
    pygame.display.flip()

    # Controle de taxa de atualização (opcional)
    pygame.time.Clock().tick(60)
