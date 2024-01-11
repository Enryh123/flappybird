import pygame, random
import tools
pygame.init()

width = 288
height = 512

clock = pygame.time.Clock()

FLY = 20001
pygame.time.set_timer(FLY, 200)

PIPE = 20002
pygame.time.set_timer(PIPE, 3000)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('flappy bird')

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


color = 'red'
index = 0
bird_rect = images[color][index].get_rect()
bird_rect.center = (width / 2, height / 2)

images['bg'] = pygame.image.load('images/background-day.png')
images['floor'] = pygame.image.load('images/base.png')
floor_rect = images['floor'].get_rect()
floor_rect.y = height*0.8

images['pipe_down'] = pygame.image.load('images/pipe-green.png')
images['pipe_up'] = pygame.transform.flip(images['pipe_down'], False, True)

pipe_img = []
pipe_rect = []

# 6. 加载gameover图片存储在字典中,并获取矩形区域，设置为屏幕中心位置
images['gameover'] = pygame.image.load('images/gameover.png')
game_rect = images['gameover'].get_rect()
game_rect.center = (width/2, height/2)

# 8. 加载音频存储在字典 sound 中
sound = {
    'die': pygame.mixer.Sound('sound/sfx_die.wav'),
    'flap': pygame.mixer.Sound('sound/sfx_wing.wav'),
}

v = -15
g = 1

# 1. 创建变量 GAMEOVER 控制游戏状态
GAMEOVER = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == FLY:
            index = index + 1
            index = index % 3

        if event.type == PIPE:
            y = random.randint(100, 200)
            up = images['pipe_up'].get_rect()
            up.bottomleft = (width, y)
            down = images['pipe_down'].get_rect()
            down.topleft = (width, y+100)
            pipe_img.append(images['pipe_up'])
            pipe_img.append(images['pipe_down'])
            pipe_rect.append(up)
            pipe_rect.append(down)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: color = 'red'
            if event.key == pygame.K_2: color = 'yellow'
            if event.key == pygame.K_3: color = 'blue'
            # 5. 设置游戏未结束时才能进行跳跃操作
            if event.key == pygame.K_SPACE and not GAMEOVER:
                v = -10
                sound['flap'].play()
            # if event.key == pygame.K_SPACE: v = -10


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: bird_rect.y -= 2
    if keys[pygame.K_DOWN]: bird_rect.y += 2
    if keys[pygame.K_LEFT]: bird_rect.x -= 2
    if keys[pygame.K_RIGHT]: bird_rect.x += 2

    window.blit(images['bg'], (0, 0))

    # 2. 判断 GAMEOVER 变量，游戏没有结束时，才移动管道和碰撞检测
    if not GAMEOVER:
        for rect, img in zip(pipe_rect, pipe_img):
            rect.x -= 1
            if rect.x < -width:
                pipe_rect.remove(rect)
                pipe_img.remove(img)

        # 3. 管道碰撞检测
        for rect in pipe_rect:
            if rect.colliderect(bird_rect):
                print('GAMEOVER')
                # 4. 检测成功，修改 GAMEOVER 变量
                GAMEOVER = True
                sound['die'].play()

    # for rect, img in zip(pipe_rect, pipe_img):
    #     rect.x -= 1
    #     if rect.x < -width:
    #         pipe_rect.remove(rect)
    #         pipe_img.remove(img)
    #
    # # 1. 管道碰撞检测
    # for rect in pipe_rect:
    #     if rect.colliderect(bird_rect):
    #         print('GAMEOVER')

    for rect, img in zip(pipe_rect, pipe_img):
        window.blit(img, rect)

    v += g
    bird_rect.y += v

    if bird_rect.bottom > floor_rect.top:
        bird_rect.bottom = floor_rect.top
    if bird_rect.left < 0: bird_rect.left = 0
    if bird_rect.right > width: bird_rect.right = width
    if bird_rect.top < 0: bird_rect.top = 0

    bird = pygame.transform.rotate(images[color][index], v)
    window.blit(bird, bird_rect)

    floor_rect.x -= 1
    floor_rect.x %= -48
    window.blit(images['floor'], floor_rect)

    # 7. 判断游戏结束，绘制结束图片
    if GAMEOVER:
        window.blit(images['gameover'], game_rect)

    # 显示分数
    tools.show_score(pipe_rect, bird_rect, window)

    pygame.display.update()
    clock.tick(30)