import pygame
import sys

pygame.init()                              # 初始化

screen = pygame.display.set_mode((500, 500))  # 窗口尺寸

while True:      # 绘制画面死循环
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quir()
            sys.exit()         
