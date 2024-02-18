from Setup_tela import *
from Draw_Objects import *
from Menu_File import *
from Objects import *
from Setup_Game import *

import random
import time

running = True
skin = -3
skin2 = 0 
skin3 = 0 
move_x = 1
moved_x = 0
move_y = 0

# Loop principal
alien_generator()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                running = not running  # Inverte o estado de pausa

    # Se o jogo estiver pausado (running == False)
    if not running:
        tela.fill(background_color)  # Cor branca
        fonte = pygame.font.Font(None, 90)
        Menu_texto = fonte.render("Menu", True, test_color)
        tela.blit(Menu_texto, (screen_width // 2 - Menu_texto.get_width() // 2, screen_height // 2 - Menu_texto.get_height() // 2 - 350))
        fonte = pygame.font.Font(None, 40)
        Press_texto = fonte.render("Pressione qualquer tecla para continuar", True, test_color)
        tela.blit(Press_texto, (screen_width // 2 - Press_texto.get_width() // 2, screen_height // 2 - Press_texto.get_height() // 2 - 310))
    
        fonte = pygame.font.Font(None, 50)

        create_design_text = fonte.render("Create Design", True, test_color)
        tela.blit(create_design_text, (screen_width // 2 - create_design_text.get_width() // 2, screen_height // 2 + 20))  # Ajuste vertical
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
                    mouse_pos = pygame.mouse.get_pos()
                    # Verifica se o clique ocorreu dentro da área do texto "Play"
                    if (screen_width // 2 - Play_text.get_width() // 2 < mouse_pos[0] < screen_width // 2 + create_design_text.get_width() // 2
                            and screen_height // 2 + 20 < mouse_pos[1] < screen_height // 2 + 20 + create_design_text.get_height()):
                        
                        tela.fill(background_color)  # Cor branca
            elif evento.type == pygame.KEYDOWN:
                running = True  # Sai do menu quando qualquer tecla é pressionada



        # Adicione a verificação do clique do mouse dentro do bloco do menu

        Play_text = fonte.render("Play", True, test_color)
        tela.blit(Play_text, (screen_width // 2 - Play_text.get_width() // 2, screen_height // 2 + 50))  # Ajuste vertical
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
                    mouse_pos = pygame.mouse.get_pos()
                    # Verifica se o clique ocorreu dentro da área do texto "Play"
                    if (screen_width // 2 - Play_text.get_width() // 2 < mouse_pos[0] < screen_width // 2 + Play_text.get_width() // 2
                            and screen_height // 2 + 50 < mouse_pos[1] < screen_height // 2 + 50 + Play_text.get_height()):
                        running = not running
            elif evento.type == pygame.KEYDOWN:
                running = True  # Sai do menu quando qualquer tecla é pressionada

    # Se o jogo estiver em execução (running == True)
    elif running:
        # Preencha a tela com uma cor de fundo
        tela.fill(background_color)  # Cor branca
        #draw_grid()
        """
        if skin == 1:
            skin = 0
        else:
            skin = 1
        """

        
        moved_x = moved_x + move_x
        if moved_x > 20 or moved_x < -20:
            move_x = -1 * move_x
            move_y = 4
        for i in range(len(objects)):
            objects[i][3] = objects[i][3] + move_x
            objects[i][4] = objects[i][4] + move_y
            skin = random.randint(0, 1)
            objects[i][1] = skin 
            draw_actor(objects[i])
        move_y = 0
 

    pygame.display.flip()
    time.sleep(0.15)
    pygame.time.Clock().tick(60)

    tela.fill(background_color)  # Cor branca
    draw_grid()
