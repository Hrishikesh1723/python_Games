# includes pause
import pygame
import sys
import random

pygame.init()
FPS = 15
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
VELOCITY = 10
SNAKE_WIDTH = 15
APPLE_SIZE = 20
TOP_WIDTH = 40
small_font = pygame.font.SysFont('Courier New', 25)
medium_font = pygame.font.SysFont('Courier New', 20, True)
large_font = pygame.font.SysFont('Courier New', 40, True, True)
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
snake_img = pygame.image.load('head.png')
apple_img = pygame.image.load('apple2.png')
tail_img = pygame.image.load('tail1.png')
apple_img_rect = apple_img.get_rect()


def start_game():
    canvas.fill(BLACK)
    start_font1 = large_font.render("Welcome to snake game", True, BLUE)
    start_font2 = medium_font.render("Play Game", True, BLACK, GREEN)
    start_font3 = medium_font.render("Instructions", True, BLACK, GREEN)
    start_font4 = medium_font.render("Quit", True, RED, GREEN)

    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()

    start_font1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
    start_font2_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 50)
    start_font3_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 100)
    start_font4_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 150)

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        start_inst(start_font1, start_font1_rect)
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def start_inst(start_font1, start_font1_rect):
    canvas.fill(BLACK)
    canvas.blit(start_font1, start_font1_rect)
    start_inst1 = small_font.render("--> Do not cross the edges, else you will be dead", True, BLUE)
    start_inst2 = small_font.render("--> Keep eating the red apples", True, BLUE)
    start_inst3 = small_font.render("--> Do not cross over yourself", True, BLUE)
    start_inst4 = small_font.render("--> Keep playing......", True, BLUE)
    start_inst5 = medium_font.render("<<BACK", True, RED, YELLOW)
    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (WINDOW_WIDTH-100, WINDOW_HEIGHT - 100)

    canvas.blit(start_inst1, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2))
    canvas.blit(start_inst2, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2 + 30))
    canvas.blit(start_inst3, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2 + 60))
    canvas.blit(start_inst4, (WINDOW_WIDTH/8, WINDOW_HEIGHT/2 + 90))
    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()


def gameover():
    #canvas.fill(BLACK)

    font_gameover1 = large_font.render('GAME OVER', True, GREEN)
    font_gameover2 = medium_font.render("Play Again", True, RED, YELLOW)
    font_gameover3 = medium_font.render("Quit", True, RED, YELLOW)

    font_gameover1_rect = font_gameover1.get_rect()
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover3_rect = font_gameover3.get_rect()


    font_gameover1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100)
    font_gameover2_rect.center = (WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 20)
    font_gameover3_rect.center = (WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 70)


    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > font_gameover2_rect.left and x < font_gameover2_rect.right:
                    if y > font_gameover2_rect.top and y < font_gameover2_rect.bottom:
                        gameloop()
                if x > font_gameover3_rect.left and x < font_gameover3_rect.right:
                    if y > font_gameover3_rect.top and y < font_gameover3_rect.bottom:
                        pygame.quit()
                        sys.exit()


        pygame.display.update()


def snake(snakelist, direction):

    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        tail = pygame.transform.rotate(tail_img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
        tail = pygame.transform.rotate(tail_img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        tail = pygame.transform.rotate(tail_img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    canvas.blit(tail, snakelist[0])

    for XnY in snakelist[1:-1]:
        pygame.draw.rect(canvas, BLUE, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))


def game_paused():
    # canvas.fill(BLACK)
    paused_font1 = large_font.render("Game Paused", True, RED)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(paused_font1, paused_font_rect1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        return
        pygame.display.update()


def gameloop():

    while True:

        LEAD_X = 0
        LEAD_Y = 100
        direction = 'right'
        score = small_font.render("Score:0", True, YELLOW)
        APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
        APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
        snakelist = []
        snakelength = 3
        pause_font = medium_font.render('II', True, RED)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                            pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            game_paused()
            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    gameover()
            if direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > WINDOW_HEIGHT - SNAKE_WIDTH:
                    gameover()
            if direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > WINDOW_WIDTH - SNAKE_WIDTH:
                    gameover()
            if direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    gameover()

            snakehead = []
            snakehead.append(LEAD_X)
            snakehead.append(LEAD_Y)
            snakelist.append(snakehead)

            snake_head_rect = pygame.Rect(LEAD_X, LEAD_Y, SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)


            if len(snakelist) > snakelength:
                del snakelist[0]
            for point in snakelist[:-1]:
                if point == snakehead:
                    gameover()

            canvas.fill(BLACK)

            snake(snakelist, direction)
            if snake_head_rect.colliderect(apple_rect):
                APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
                APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
                snakelength += 1
                score = small_font.render("Score:" + str(snakelength - 3), True, YELLOW)

            canvas.blit(score, (20, 10))
            pygame.draw.line(canvas, GREEN, (0, TOP_WIDTH), (WINDOW_WIDTH, TOP_WIDTH))
            pygame.draw.line(canvas, YELLOW, (WINDOW_WIDTH - 60, 0), (WINDOW_WIDTH - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, YELLOW, (WINDOW_WIDTH - 60, 0, 60, TOP_WIDTH))
            canvas.blit(pause_font, (WINDOW_WIDTH - 45, 10))
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            pygame.display.update()

            clock.tick(FPS)


start_game()
gameloop()
