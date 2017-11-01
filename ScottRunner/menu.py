def menu():
    import pygame
    import sys
    import pygame.gfxdraw
    from modulos import jogo
    from modulos import aboutus

    pygame.init()
    pygame.font.init()
    
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    fonte = pygame.font.Font("PressStart2P.ttf", 30)
    jogar = fonte.render("Play", True, [0,0,0])
    score = fonte.render("About", True, [0,0,0])
    screen = pygame.display.set_mode((960,416))
    pygame.display.set_caption("Scott Runner - Menu")
    imagemfundo = pygame.image.load("modulos\midias\sky_backgroundmenu.png")
    x=1
    y=1
    screen.blit(imagemfundo,[x,y])
    screen.blit(jogar, [290,250])
    screen.blit(score, [490,250])
    rect = pygame.Surface((148,30), pygame.SRCALPHA, 32)
    rect.fill((0, 0, 0, 0))
    rect2 = pygame.Surface((176,30), pygame.SRCALPHA, 32)
    rect2.fill((0, 0, 0, 0))
    screen.blit(rect, (290,250))
    screen.blit(rect2, (490,250))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x>290 and x<430) and (y>250 and y<290):
                    jogo.jogo()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x>490 and x<666) and (y>250 and y<290):
                    aboutus.aboutus()
