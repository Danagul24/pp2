import pygame
import random
import time
from enum import Enum
from pygame import mixer

pygame.init()

width=800
height=600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tanks")
font = pygame.font.SysFont('System', 40) 
seconds=1/30

mixer.music.load('back.wav')
mixer.music.play(-1)

bullet_Sound=pygame.mixer.Sound('bullet.wav')
hit_Sound=pygame.mixer.Sound('hit.wav')

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tank:

    def __init__(self, x, y, speed, color, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN,d_pull=pygame.K_RETURN):
        self.x = float(x)
        self.y = float(y)
        self.score=3
        self.speed = float(speed)
        self.color = color
        self.width = 40
        self.direction = Direction.RIGHT

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

        self.KEYPULL=d_pull


    def draw(self):
        tank_c = (int(self.x) + int(self.width / 2), int(self.y) + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (int(self.x) + self.width + int(self.width/2), int(self.y)  + int(self.width/2)), 4)

        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (int(self.x) - int(self.width/2), int(self.y)  + int(self.width/2)), 4)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (int(self.x) + int(self.width/2), int(self.y)  - int(self.width/2)), 4)
        
        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (int(self.x) + int(self.width/2), int(self.y)  + self.width + int(self.width/2)), 4)


    def change_direction(self,direction):
        self.direction = direction

    #CREATE DIRECTION

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed*seconds
        if self.direction == Direction.RIGHT:
            self.x += self.speed*seconds
        if self.direction == Direction.UP:
            self.y -= self.speed*seconds
        if self.direction == Direction.DOWN:
            self.y += self.speed*seconds

        if self.x > screen.get_size()[0]:
            self.x = 0 - self.width
        if self.x < 0 - self.width:
            self.x = screen.get_size()[0]
        if self.y > screen.get_size()[1]:
            self.y = 0 - self.width
        if self.y < 0 - self.width:
            self.y = screen.get_size()[1]
       
        
        self.draw()
    
class Bullet:
    def __init__(self,x=0,y=0,color=(0,0,0),direction=Direction.LEFT,speed=1):
        self.x=x
        self.y=y
        self.color=color
        self.speed=speed
        self.direction=direction
        self.status=True
        self.distance=0
        self.radius=10

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        self.distance+=1
        if self.distance>(2*width):
            self.status=False
        self.draw()

    def draw(self):
        if self.status:
            pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.radius)

def give_coordinates(tank):
    if tank.direction == Direction.RIGHT:
        x=tank.x + tank.width + int(tank.width / 2)
        y=tank.y + int(tank.width / 2)

    if tank.direction == Direction.LEFT:
        x=tank.x - int(tank.width / 2)
        y=tank.y + int(tank.width / 2)

    if tank.direction == Direction.UP:
        x=tank.x + int(tank.width / 2)
        y=tank.y - int(tank.width / 2)

    if tank.direction == Direction.DOWN:
        x=tank.x + int(tank.width / 2)
        y=tank.y + tank.width + int(tank.width / 2)

    p=Bullet(x,y,tank.color,tank.direction)
    bullet.append(p)



def collision():

    #collision of bullet and tank
    for p in bullet:
        
        for tank in tanks:
            
            if (tank.x+tank.width+p.radius > p.x > tank.x - p.radius ) and ((tank.y+tank.width + p.radius > p.y > tank.y - p.radius)) and p.status==True:
                hit_Sound.play()
                p.color=(0,0,0)
                tank.score -= 1
                
                p.status=False
                
                tank.x=random.randint(50,width-70)
                tank.y=random.randint(50,height-70)

            if tanks[1].score == 0:
                font1 = pygame.font.SysFont('System', 40)
                text = font1.render("Game Over. Red tank won", 1, (255, 0, 0))
                place = text.get_rect(center = (400, 300))
                screen.blit(text, place)
            if tanks[0].score == 0:
                font2 = pygame.font.SysFont('System', 40)
                text = font2.render("Game Over. Blue tank won", 1, (50, 0, 100))
                place = text.get_rect(center = (400, 300))
                screen.blit(text, place)
                
def score():
    score1= tanks[1].score
    score2= tanks[0].score
    res = font.render(str(score1), True, (50, 0, 100))
    res1 = font.render(str(score2), True, (255, 0, 0))
    screen.blit(res, (30,30))
    screen.blit(res1, (750,30))

mainloop = True
tank1 = Tank(350,350,4,(255, 0, 0))
tank2 = Tank(100,100,4,(50, 0, 100),pygame.K_d,pygame.K_a,pygame.K_w,pygame.K_s,pygame.K_SPACE)

bullet1=Bullet()
bullet2=Bullet()

tanks = [tank1, tank2]
bullet = [bullet1,bullet2]

while mainloop:
    
    screen.fill((255, 255, 255))
    
    score()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                quit()
            pressed = pygame.key.get_pressed()
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])

                if event.key in tank.KEY.keys():
                    tank.move()
                
                if pressed[tank.KEYPULL]:
                    bullet_Sound.play()
                    give_coordinates(tank)
                        
    collision()

    for p in bullet:
        p.move()
    
    for tank in tanks:
        tank.draw() 
    tank1.move()
    tank2.move()
   
    pygame.display.flip()

pygame.quit()
