import pygame
import sys

pygame.init()                              # 初始化

window = pygame.display.set_mode((500, 500))  # 窗口尺寸

# 设置游戏标题
pygame.display.set_caption('小游戏')



while True:      # 绘制画面死循环
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quir()
            sys.exit()        

            # 图像显示与运动         