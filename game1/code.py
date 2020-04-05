
pygame.init()

screen = pygame.display.set_mode((600, 600))

done = False
backgroundImage = pygame.image.load("background.jpg")
playerImage = pygame.image.load("player.png")
player_x = 200
player_y = 500

enemyImage = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 536)
enemy_y = random.randint(20, 50)

enemy_dx = 10
enemy_dy = 30

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

while not done:
    for event in pygame.event.get():
        # event on quit
        if event.type == pygame.QUIT: # event.type == pygame.KEYDOWN
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: player_x -= 3
    if pressed[pygame.K_RIGHT]: player_x += 3
        
    # screen.fill((0, 0, 0))

    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 536:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy
    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.flip()
