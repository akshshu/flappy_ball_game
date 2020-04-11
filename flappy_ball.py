import pygame
import random


class ball_begin:
    def __init__(self, x, y, changey):
        self.x = x
        self.y = y
        self.changey = changey


class pole_begin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.upperx = x
        self.uppery = y
        self.lowerx = x
        self.lowery = 500+(self.uppery+170)


pygame.init()

ballchange2 = 0
next_state = 'ready'


def ball_display(x, y):
    screen.blit(ball_icon, (int(x), int(y)))


def check_collision(ball, pole):
    for po in pole:
        if ball.x > po.x-30 and ball.x < po.x+100 and (ball.y < po.uppery+575 or ball.y > po.lowery-32):
            return True
        elif ball.y > 468 or ball.y < 0:
            return True


def show_game_over(score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    over_screen = font.render(
        "Game Over!! Score :"+str(score), True, (255, 255, 255))
    screen.blit(over_screen, (150, 250))


def game_over_task():
    ball.x = -300
    global end
    end = 1
    for po in pole:
        po.lowery = -1000
        po.uppery = -1000


def display_score(score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    curr_Score = font.render(
        "Score :"+str(score), True, (255, 255, 255))
    screen.blit(curr_Score, (5, 5))


def display_poles(pol):
    screen.blit(upper_pole, (int(pol.upperx), int(pol.uppery)))
    screen.blit(lower_pole, (int(pol.lowerx), int(pol.lowery)))


score = 0
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flappy_ball")
ball_icon = pygame.image.load('ball2.png')
background = pygame.image.load('back.png').convert()
lower_pole = pygame.image.load('up.png')
upper_pole = pygame.image.load('low.png')
ball = ball_begin(80, 250, 4)
clock = pygame.time.Clock()
pole = [pole_begin(300, random.randint(-490, -240)), pole_begin(570,
                                                                random.randint(-490, -240)), pole_begin(840, random.randint(-490, -240))]
run = True
x = 0
uppery = random.randint(-432, -130)
end = 0

while run:
    clock.tick(60)
    rel_x = x % background.get_rect().width
    screen.blit(background, (rel_x-background.get_rect().width, 0))
    if rel_x < 500:
        screen.blit(background, (rel_x, 0))
    x -= 2
    for po in pole:
        display_poles(po)
        po.upperx -= 2.5
        po.lowerx -= 2.5
        po.x -= 2.5
        if int(po.lowerx) == 12 and end == 0:
            score += 1
            print(score)
        if int(po.lowerx) <= -102:
            temp = pole[1]
            display_poles(temp)
            pole.remove(pole[0])
            pole.append(pole_begin(
                pole[1].lowerx+270, random.randint(-490, -240)))
    display_score(score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.changey = -5
                ballchange2 = 0
                next_state = 'run'
        else:
            next_state = 'ready'

    if(next_state == 'ready'):
        ballchange2 = ballchange2+0.20
        ball.changey = min(ballchange2, 4)

    ball.y += ball.changey
    ball_display(ball.x, ball.y)
    if check_collision(ball, pole):
        game_over_task()
    if(ball.x == -300):
        show_game_over(score)
    pygame.display.update()
