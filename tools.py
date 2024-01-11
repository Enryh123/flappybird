import pygame
pygame.init()


score = 0

img = [pygame.image.load(f'images/num/{i}.png') for i in range(10)]
point = pygame.mixer.Sound('sound/sfx_point.wav')
def show_score(pipe_rect, bird_rect, window):
    global score
    for r in pipe_rect:
        if bird_rect.centerx == r.centerx and bird_rect.y > r.y:
            score += 1
            point.play()

    rects = [ img[int(i)].get_rect() for i in str(score)]
    width = 0
    for r in rects: width+=r.width

    x = (288-width)//2
    for n in str(score):
        r = img[int(n)].get_rect(topleft=(x,50))
        window.blit(img[int(n)], r)
        x += r.width
    print(score)