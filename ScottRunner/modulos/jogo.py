import pygame

pygame.init()

max_distance = 0
iBackground = 0
nuvens = [pygame.image.load("modulos\\midias\\nuvem\\n4.png"), pygame.image.load("modulos\\midias\\nuvem\\n5.png"),pygame.image.load("modulos\\midias\\nuvem\\n6.png"),
        pygame.image.load("modulos\\midias\\nuvem\\n7.png"), pygame.image.load("modulos\\midias\\nuvem\\n8.png"),pygame.image.load("modulos\\midias\\nuvem\\n9.png")]
def mudarBackground():
    global iBackground
    iBackground += 1
    if iBackground > 5:
        iBackground = 0
    return nuvens[iBackground]

def telalose(pont):
    import pygame
    import sys
    import menu
    
    pygame.init()
    pygame.font.init()
    pygame.mixer.pre_init()
    pygame.mixer.init()

    fonte = pygame.font.Font("PressStart2P.ttf", 50)
    fonte2 = pygame.font.Font("PressStart2P.ttf", 25)
    losetxt = fonte.render("YOU LOSE!", True, [255,0,0])
    scoretxt = fonte2.render("Your score: " + str(pont), True, [0,0,0])
    retrybtn = fonte2.render("Retry", True, [0,0,0])
    menubtn = fonte2.render("Menu", True, [0,0,0])
    screen = pygame.display.set_mode((960,416))
    pygame.display.set_caption("Scott Runner")
    imagemfundo = pygame.image.load("modulos\midias\sky_backgroundoficial.png")
    x=1
    y=1
    screen.blit(imagemfundo,[x,y])
    screen.blit(losetxt,[265,50])
    screen.blit(scoretxt,[295,120])
    screen.blit(retrybtn,[295,230])
    screen.blit(menubtn,[520,230])
    pygame.display.flip()
    clock = pygame.time.Clock()

    pygame.display.flip()
    clock.tick(60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if (x>295 and x<410) and (y>230 and y<260):
                jogo()
            if (x>520 and x<635) and (y>230 and y<260):
                menu.menu()
    
def jogo():
        
    import pygame
    import sys

    pygame.init()
    pygame.font.init()

        
    def pontos(pontos):
        text = fonte.render("Distance: " + str(pontos) + "m", True, cor)
        screen.blit(text, [10,10])
        max_Distance = fonte2.render("High Score: " + str(max_distance) + "m", True, cor)
        screen.blit(max_Distance, [10,40])

    jump = pygame.mixer.Sound("modulos\midias\Jump.wav")
    fonte = pygame.font.Font("PressStart2P.ttf", 30)
    fonte2 = pygame.font.Font("PressStart2P.ttf", 15)
    screen = pygame.display.set_mode((960,416))
    pygame.display.set_caption("Scott Runner")
    imagemfundo = pygame.image.load("modulos\midias\sky_backgroundoficial.png")
    x=1
    y=1
    screen.blit(imagemfundo,[x,y])
    pygame.display.flip()
    clock = pygame.time.Clock()

    personagens = [pygame.image.load("modulos\midias\p1.png"),pygame.image.load("modulos\midias\p2.png"), pygame.image.load("modulos\midias\p3.png"),
                       pygame.image.load("modulos\midias\p4.png"), pygame.image.load("modulos\midias\p5.png"),pygame.image.load("modulos\midias\p6.png"),
                       pygame.image.load("modulos\midias\p7.png"), pygame.image.load("modulos\midias\p8.png")]



    rectPersonagem = None
    x_missile = 960
    y_missile = 260
    x_char=100
    y_char=216
    deslocando = False
    y_change=0
    i = 0
    fps = 60
    timer = 0
    timer_n = 0
    global max_distance
    cor = [185,129,80]
    distancia = 0
    timer_score = 0
    correndo = True
    missile = pygame.image.load("modulos\midias\missile1.png")
    pygame.time.set_timer(pygame.USEREVENT + 2, 1)
    pygame.time.set_timer(pygame.USEREVENT + 3, 200)
    while True:     
        timer_n +=1
        timer_score += 1
        timer += 1
        screen.blit(imagemfundo,[x,y])

        #Fechar---------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #---------------#

            #Movimentaçao--------#
            elif event.type == pygame.USEREVENT + 1:
                y_char += y_change
                if y_char < 60:
                    y_change = 5
                elif y_char > 216:
                    y_char = 216
                    y_change = 0
                    deslocando = False
                    pygame.time.set_timer(pygame.USEREVENT + 1, 0)
            elif event.type == pygame.USEREVENT + 2:
                x_missile -= min(10 + (distancia / 50), 20)
            elif event.type == pygame.USEREVENT + 3:
                imagemfundo = mudarBackground()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    jump.play()
                    if deslocando == False:
                        deslocando = True
                        y_change = -4
                        pygame.time.set_timer(pygame.USEREVENT + 1, 5)
        y_char +=y_change
            #--------------------#
        
        #Movimentação missel------#
        rectMissile = missile.get_rect()
        rectMissile.left, rectMissile.top = x_missile, y_missile
        screen.blit(missile,rectMissile)
        if x_missile < 0:
            x_missile = 960
        #---------------------#

        #Animação de correr----------#
        if correndo == True:
            rectPersonagem = personagens[i].get_rect()
            rectPersonagem.width -= 45
            rectPersonagem.height -= 40
            rectPersonagem.left, rectPersonagem.top = x_char, y_char
            screen.blit(personagens[i], rectPersonagem)
            if i == 0 and timer == 5:
                i = 1
            elif i == 1 and timer == 10:
                i = 2
            elif i == 2 and timer == 15:
                i = 3
            elif i == 3 and timer == 20:
                i = 4
            elif i == 4 and timer == 25:
                i = 5
            elif i == 5 and timer == 30:
                i = 6
            elif i == 6 and timer == 35:
                i = 7
            elif i == 7 and timer == 40:
                i = 0
                timer = 0

        #Colisão-----------------#
        if rectMissile.colliderect(rectPersonagem):
           telalose(distancia)
        #Velocidade do contador de distancia e distancia maxima-------#
        if timer_score % 15 == 0:
            distancia += 1
        if distancia > max_distance:
            max_distance = distancia
            
        pontos(distancia)
        pygame.display.flip()
        clock.tick(fps)
