def aboutus():
    import pygame
    import sys
    import menu

    pygame.init()
    pygame.font.init()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    fonte = pygame.font.Font("PressStart2P.ttf", 30)
    fonte2 = pygame.font.Font("PressStart2P.ttf", 14)
    aboutUs = fonte.render("Description:", True, [0,0,0])
    btnBack = fonte.render("Back", True, [0,0,0])
    aboutUs2 = fonte.render("How to play:", True, [0,0,0])
    description = fonte2.render("- Scott Runner is about a character named Scott. The objective", True, [0,0,0])
    description2 = fonte2.render("is jump over the missiles and run as far as you can.", True, [0,0,0])
    description3 = fonte2.render("- As the character runs, the speed of the game increases.", True, [0,0,0])
    instruction = fonte2.render("Press ↑ or SPACE to jump.", True, [0,0,0])
    screen = pygame.display.set_mode((960,416))
    pygame.display.set_caption("Scott Runner - About")
    imagemfundo = pygame.image.load("modulos\midias\sky_backgroundaboutUs.png")
    x=1
    y=1
    screen.blit(imagemfundo,[x,y])
    screen.blit(aboutUs,[35,40])
    screen.blit(aboutUs2,[35,160])
    screen.blit(description,[45,80])
    screen.blit(description2,[45,100])
    screen.blit(description3,[45,120])
    screen.blit(instruction,[45,200])
    screen.blit(btnBack,[45,300])
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if (x>45 and x<160) and (y>300 and y<330):
                menu.menu()
