import pygame, sys, random

pygame.init() 

screen = pygame.display.set_mode((640, 480))

# setup a new font
font = pygame.font.Font(None, 36)

score = 0

ball = pygame.image.load("ball.bmp")
ball_x = 10
ball_y = 10
ball_x_speed = 7
ball_y_speed = 7

bat = pygame.image.load("bat.bmp")
bat_x = 260
bat_y = 430

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    score += 1

    #check for arrow key presses
    #and move bat accordingly
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and bat_x < 512:
        bat_x += 15
    if pressed[pygame.K_LEFT] and bat_x > 0:
        bat_x -= 15

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    #collision detction code
    if ball_x > bat_x and ball_x < bat_x + 112 and ball_y >400:
        ball_y_speed = -(random.randint(5,15))
    
    if ball_x > 610: ball_x_speed = -(random.randint(5, 15))
    if ball_y > 450: break
    if ball_x < 0: ball_x_speed = random.randint(5, 15)
    if ball_y < 0: ball_y_speed = random.randint(5, 15)

    screen.fill((240, 255, 255))

    #generate and render score text
    scoretext = font.render("Score:" + str(score), 1, (30, 30, 30))
    screen.blit(scoretext, (10, 10))

    screen.blit(ball, (ball_x, ball_y))
    screen.blit(bat, (bat_x, bat_y))

    pygame.display.flip() 
    pygame.time.wait(10)

print("Your score was:", score)



