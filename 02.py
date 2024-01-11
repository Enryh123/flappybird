import pygame
pygame.init()

width = 288
height = 512

# 3. 创建时钟
clock = pygame.time.Clock()

# 7. 创建自定义事件
FLY = 20001
pygame.time.set_timer(FLY, 200)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('flappy bird')

bg_image = pygame.image.load('images/background-day.png')

# 5. 使用bird列表存储鸟的图片，并删除bird_image
bird = [
    pygame.image.load('images/bluebird-upflap.png'),
    pygame.image.load('images/bluebird-midflap.png'),
    pygame.image.load('images/bluebird-downflap.png')
]
index = 0
bird_rect = bird[index].get_rect()
bird_rect.center = (width / 2, height / 2)

# 1. 地板图片与矩形区域
floor_image = pygame.image.load('images/base.png')
floor_rect = floor_image.get_rect()  


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()

        # 8. 判断自定义事件并实现鸟动画
        if event.type == FLY:
            index += 1
            index %= 3


    window.blit(bg_image, (0, 0))


    # 6. 使用列表访问鸟的图片并绘制
    window.blit(bird[index], bird_rect)


    # 2. 绘制地板并移动
    floor_rect.y = height*0.8
    floor_rect.x -= 1
    floor_rect.x %= -48
    window.blit(floor_image, floor_rect)

    pygame.display.update()

    # 4. 设置帧率
    clock.tick(30)
