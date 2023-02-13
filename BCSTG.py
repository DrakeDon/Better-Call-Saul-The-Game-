#Made By DrakeDon and ThunderPixelGames
import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode([1920, 1080])



Start=True
while Start:
    def intro():
        introscreen=pygame.image.load('IntroscreenBCS.jpeg')
        introscreen = pygame.transform.scale(introscreen, (1920,1080))
        screen.blit(introscreen,(0,0))
        pygame.display.flip()
    
    intro()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Start=False

pygame.display.flip()
