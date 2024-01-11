import pygame, random      # 6-1 导入 random 模块
pygame.init()

width = 288
height = 512

clock = pygame.time.Clock()

FLY = 20001
pygame.time.set_timer(FLY, 200)

# 3. 创建PIPE自定义事件，用来控制生成管道
PIPE = 20002
pygame.time.set_timer(PIPE, 1000)

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

# 2. 字典添加键，pipe_down 存储画面下方的管道图片， pipe_up 存储画面上方的管道图片
images['pipe_down'] = pygame.image.load('images/pipe-green.png')
images['pipe_up'] = pygame.transform.flip(images['pipe_down'], False, True)

# 5. 创建2个空列表，分别存储管道图片和管道矩形区域
pipe_img = []
pipe_rect = []

v = -15
g = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == FLY:
            index = index + 1
            index = index % 3

        # 4. 判断PIPE事件，打印输出event
        if event.type == PIPE:
            print(event)

            # 6. 随机生成画面上方管道的y坐标，并将管道图片和矩形区域添加至列表中
            y = random.randint(100, 200)
            up = images['pipe_up'].get_rect()
            up.bottomleft = (width, y)
            down = images['pipe_down'].get_rect()
            down.topleft = (width, y+100)
            pipe_img.append(images['pipe_up'])
            pipe_img.append(images['pipe_down'])
            pipe_rect.append(up)
            pipe_rect.append(down)
            print(pipe_rect)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: color = 'red'
            if event.key == pygame.K_2: color = 'yellow'
            if event.key == pygame.K_3: color = 'blue'
            if event.key == pygame.K_SPACE: v = -10


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: bird_rect.y -= 2
    if keys[pygame.K_DOWN]: bird_rect.y += 2
    if keys[pygame.K_LEFT]: bird_rect.x -= 2
    if keys[pygame.K_RIGHT]: bird_rect.x += 2

    window.blit(images['bg'], (0, 0))

    # 8. for循环控制管道移动
    for rect, img in zip(pipe_rect, pipe_img):
        rect.x -= 1
        if rect.x < -width:
            pipe_rect.remove(rect)
            pipe_img.remove(img)

    # 7. for循环绘制管道图片
    for rect, img in zip(pipe_rect, pipe_img):
        window.blit(img, rect)

    v += g
    bird_rect.y += v

    if bird_rect.bottom > floor_rect.top:
        bird_rect.bottom = floor_rect.top
    if bird_rect.left < 0: bird_rect.left = 0
    if bird_rect.right > width: bird_rect.right = width
    if bird_rect.top < 0: bird_rect.top = 0

    # 1. 创建 bird 变量存储根据速度旋转后的小鸟图片
    bird = pygame.transform.rotate(images[color][index], v)
    window.blit(bird, bird_rect)
    # window.blit(images[color][index], bird_rect) # 1.1 修改为绘制旋转后的图片

    floor_rect.x -= 1
    floor_rect.x %= -48
    window.blit(images['floor'], floor_rect)

    pygame.display.update()
    clock.tick(30)