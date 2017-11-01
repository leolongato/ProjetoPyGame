import menu
import pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer.music.load("modulos\midias\Theme.mp3")
pygame.mixer.music.play()

menu.menu()
