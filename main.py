import pygame as pg
from random import *
from time import *

def check_end_game(x, y, snake):
    if x >= 800 or x <= -20 or y >= 480 or y <= -20:
        return True
    elif len(snake) >  4  and snake[-1] in snake[:-1]:
        return True
    else:
        return False


def set_default_values():
    return 200, 320, 400, 120, "right", 0, [[200, 320]]

pg.init()
disp = pg.display.set_mode((800, 480))
pg.display.set_caption("my big green snake")
pg.display.update()

game_over = False
clock = pg.time.Clock()
font = pg.font.Font(None, 40)
direction = "right"

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

apple_img = pg.image.load('appl.png')
body_img = pg.image.load('body.png')
snek_img = pg.image.load('snek.png')
anger_img = pg.image.load('angr!!!.png')
boost_img = pg.image.load('boost.png')
x = 200
y = 320
apple_x = 400
apple_y = 120
boost_x = 600
boost_y = 80
score = 0
snake = [[x, y]]
while not game_over:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
            print("game over you racial slur")
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a and direction != "right":
                direction = "left"
            if event.key == pg.K_d and direction != "left":
                direction = "right"
            if event.key == pg.K_w and direction != "down":
                direction = "up"
            if event.key == pg.K_s and direction != "up":
                direction = "down"

    if direction == "left":
        x -= 40
    if direction == "right":
        x += 40
    if direction == "up":
        y -= 40
    if direction == "down":
        y += 40

    for i in range(len(snake) - 1):
        snake[i] = snake[i + 1]
    snake[-1] = [x, y]

    if x == apple_x and y == apple_y:
        snake = [snake[0]] + snake
        score += 1
        while [apple_x, apple_y] in snake:
            apple_x = randint(1, 19) * 40
            apple_y = randint(1, 11) * 40
    if x == boost_x and y == boost_y:
        snake = [snake[0]] + snake
        snake = [snake[1]] + snake
        snake = [snake[2]] + snake
        score += 3
        while [boost_x, boost_y] == [apple_x, apple_y] or [boost_x, boost_y] in snake:
            boost_x = randint(1, 19) * 40
            boost_y = randint(1, 11) * 40
    if check_end_game(x, y, snake):
        # game_over = True
        disp.blit(anger_img, [x - 40, y - 40])
        pg.display.update()
        x, y, apple_x, apple_y, direction, score, snake = set_default_values()
        message = font.render("you lost lmfao", True, WHITE)
        disp.blit(message, [200, 40])
        pg.display.update()
        pg.time.delay(1000)
        continue
    disp.fill(BLACK)
    for i in range(len(snake)):
       # pg.draw.rect(disp, GREEN, (snake[i][0], snake[i][1], 40, 40))
        disp.blit(body_img, snake[i])

    if direction == "up":
        disp.blit(snek_img, [x, y])
    if direction == "left":
        disp.blit(pg.transform.rotate(snek_img, 90), [x, y])
    if direction == "right":
        disp.blit(pg.transform.rotate(snek_img, -90), [x, y])
    if direction == "down":
        disp.blit(pg.transform.rotate(snek_img, -180), [x, y])

    # pg.draw.rect(disp, RED, [apple_x, apple_y, 40, 40])
    disp.blit(apple_img, [apple_x, apple_y, 40, 40])
    disp.blit(boost_img, [boost_x, boost_y, 40, 40])
    message = font.render("score:" +  str(score), True, WHITE)
    disp.blit(message, [8, 8])
    pg.display.update()


pg.quit()
quit()
