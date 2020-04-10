import pygame
import random


class ball_begin:
    def __init__(self, x, y, changey):
        self.x = x
        self.y = y
        self.changey = changey


class pole_begin:
    def __init__(self, x, y, upper, lower):
        self.x = x
        self.y = y


pygame.init()

ballchange2 = 0
next_state = 'ready'


def ball_display(x, y):
    screen.blit(ball_icon, (x, y))


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flappy_ball")
ball_icon = pygame.image.load('ball2.png').convert()
background = pygame.image.load('back.png').convert()
ball = ball_begin(250, 250, 4)
clock = pygame.time.Clock()
run = True
x = 0
while run:
    clock.tick(60)
    rel_x = x % background.get_rect().width
    screen.blit(background, (rel_x-background.get_rect().width, 0))
    if rel_x < 500:
        screen.blit(background, (rel_x, 0))
    x -= 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.changey = -4
                ballchange2 = 0
                next_state = 'run'
        else:
            next_state = 'ready'

    if(next_state == 'ready'):
        ballchange2 = ballchange2+0.20
        print(ballchange2)
        ball.changey = min(ballchange2, 4)
        print(ball.changey)

    ball.y += ball.changey
    ball_display(ball.x, ball.y)
    pygame.display.update()
