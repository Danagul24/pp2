import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
 
screen_width = 600
screen_height = 400
 
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
 
snake_size = 10
speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def myScore(score):
    value = score_font.render("Score: " + str(score), True, black)
    screen.blit(value, [0, 0])
 
 
def Snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_size, snake_size])

 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 8, screen_height / 3])
 
 
def game():
    game_over = False
    game_close = False
 
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    snake_lenght = 1
 
    foodx = round(random.randrange(0, screen_width) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height) / 10.0) * 10.0
 
    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("You Lost! To Play Again - press C, to quit - press Q", red)
            myScore(snake_lenght - 1)
            pygame.display.flip()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
                elif event.key == pygame.K_q:
                    game_over = True
                    game_close = False
            
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > snake_lenght:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True
 
        Snake(snake_size, snake_List)
        myScore(snake_lenght - 1)
 
        pygame.display.flip()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            snake_lenght += 1
 
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
game()
