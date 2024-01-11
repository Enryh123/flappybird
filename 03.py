import pygame
pygame.init()

width = 288
height = 512

clock = pygame.time.Clock()

FLY = 20001
pygame.time.set_timer(FLY, 200)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('flappy bird')

# 1. 创建 images 字典，存储小鸟图片，并删除 bird 变量
images = {
    'red': [pygame.image.load('images/redbird-upflap.png'),
            pygame.image.load('images/redbird-midflap.png'),
            pygame.image.load('images/redbird-downflap.png')],
    'yellow': [pygame.image.load('images/yellowbird-upflap.png'),
            pygame.image.load('images/yellowbird-midflap.png'),
            pygame.image.load('images/yellowbird-downflap.png')],
    'blue': [pygame.image.load('images/bluebird-upflap.png'),
            pygame.image.load('images/bluebird-midflap.png'),
            pygame.image.load('images/bluebird-downflap.png')],
}
# bird = [
# pygame.image.load('images/bluebird-upflap.png'),
# pygame.image.load('images/bluebird-midflap.png'),
# pygame.image.load('images/bluebird-downflap.png')
# ]

# 2. 创建 color 变量存储鸟的颜色，并修改所有小鸟图片访问的代码
color = 'red'
index = 0
bird_rect = images[color][index].get_rect()
# bird_rect = bird[index].get_rect()     # 2-1. 修改为字典访问
bird_rect.center = (width / 2, height / 2)

# 3. 使用字典添加键，存储背景图片和地板图片，删除 bg_image, 和 floor_image 变量
images['bg'] = pygame.image.load('images/background-day.png')
# bg_image = pygame.image.load('images/background-day.png')
images['floor'] = pygame.image.load('images/base.png')
# floor_image = pygame.image.load('images/base.png')
# floor_rect = floor_image.get_rect()  # 3-1. 修改为字典访问
floor_rect = images['floor'].get_rect()
floor_rect.y = height*0.8

# 7. 创建 v 变量控制速度，创建 g 变量表示重力
v = 0
g = 1

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()

        if event.type == FLY:
            index = index + 1
            index = index % 3

        # 4. 判断键盘按下事件，使用 1，2，3 切换小鸟颜色
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: color = 'red'
            if event.key == pygame.K_2: color = 'yellow'
            if event.key == pygame.K_3: color = 'blue'


            # 9. 判断空格按键，设置速度为-10
            if event.key == pygame.K_SPACE: v = -10



    # 5. 使用 get_pressed() 控制移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: bird_rect.y -= 2
    if keys[pygame.K_DOWN]: bird_rect.y += 2
    if keys[pygame.K_LEFT]: bird_rect.x -= 2
    if keys[pygame.K_RIGHT]: bird_rect.x += 2

    window.blit(images['bg'], (0, 0))
    # window.blit(bg_image, (0, 0))   # 3-2. 修改为字典访问

    # 8. 利用速度和重力，计算小鸟y坐标
    v += g
    bird_rect.y += v

    # 6. 限制小鸟移动不能超过地板、屏幕上边，左边和右边
    if bird_rect.bottom > floor_rect.top:
        bird_rect.bottom = floor_rect.top
    if bird_rect.left < 0: bird_rect.left = 0
    if bird_rect.right > width: bird_rect.right = width
    if bird_rect.top < 0: bird_rect.top = 0

    window.blit(images[color][index], bird_rect)
    # window.blit(bird[index], bird_rect)  # 2-2. 修改为字典访问

    floor_rect.x -= 1
    floor_rect.x %= -48
    window.blit(images['floor'], floor_rect)
    # window.blit(floor_image, floor_rect)  # 3-3. 修改为字典访问

    pygame.display.update()
    clock.tick(30)